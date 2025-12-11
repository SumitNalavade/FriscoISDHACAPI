from http.server import BaseHTTPRequestHandler
from urllib import parse
import json

from bs4 import BeautifulSoup
from api._lib.getRequestSession import getRequestSession
from api._lib.parsers import _get_text_or_empty_by_css_selector, _get_text_or_empty_by_id

REGISTRATION_URL = "https://hac.friscoisd.org/HomeAccess/Content/Student/Registration.aspx"
SCHEDULE_URL = "https://hac.friscoisd.org/HomeAccess/Content/Student/Classes.aspx"

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse.urlsplit(self.path).query
        params = dict(parse.parse_qsl(query))

        username = params.get("username")
        password = params.get("password")

        if not username or not password:
            self._send_json(
                {"error": "Missing username or password in query parameters."},
                status=400,
            )
            return

        try:
            session = getRequestSession(username, password)

            # ---- Fetch registration page ----
            reg_resp = session.get(REGISTRATION_URL)
            reg_resp.raise_for_status()
            reg_html = reg_resp.text

            reg_soup = BeautifulSoup(reg_html, "lxml")

            # ---- Extract fields from registration page ----
            student_name = _get_text_or_empty_by_id(
                reg_soup, "plnMain_lblRegStudentName")
            student_birthdate = _get_text_or_empty_by_id(
                reg_soup, "plnMain_lblBirthDate")
            student_counselor = _get_text_or_empty_by_id(
                reg_soup, "plnMain_lblCounselor")
            student_campus = _get_text_or_empty_by_id(
                reg_soup, "plnMain_lblBuildingName")
            student_grade = _get_text_or_empty_by_id(reg_soup, "plnMain_lblGrade")
            student_house_team = _get_text_or_empty_by_id(reg_soup, "plnMain_lblHouseTeam")
            student_calendar = _get_text_or_empty_by_id(reg_soup, "plnMain_lblCalendar")
            student_homeroom = _get_text_or_empty_by_id(reg_soup, "plnMain_lblHomeroom")
            student_language = _get_text_or_empty_by_id(reg_soup, "plnMain_lblLanguage")
            student_homeroom_teacher = _get_text_or_empty_by_css_selector(reg_soup, "#plnMain_lblHomeroomTeacher > a:nth-child(1)")[0]

            # ---- Try to get student id from registration page ----
            student_id = _get_text_or_empty_by_id(
                reg_soup, "plnMain_lblRegStudentID")

            # If not found, fall back to schedule page
            if not student_id:
                sched_resp = session.get(SCHEDULE_URL)
                sched_resp.raise_for_status()
                sched_soup = BeautifulSoup(sched_resp.text, "lxml")
                student_id = _get_text_or_empty_by_id(
                    sched_soup, "plnMain_lblRegStudentID")

            data = {
                "id": student_id,
                "name": student_name,
                "birthdate": student_birthdate,
                "campus": student_campus,
                "grade": student_grade,
                "counselor": student_counselor,
                "house_team": student_house_team,
                "calander": student_calendar,
                "homeroom": student_homeroom,
                "language": student_language,
                "homeroom_teacher": student_homeroom_teacher
            }

            self._send_json(data, status=200)

        except Exception as e:
            self._send_json(
                {"error": "Failed to fetch student info."},
                status=500,
            )

    def _send_json(self, payload, status: int = 200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

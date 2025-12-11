from http.server import BaseHTTPRequestHandler
from urllib import parse
import json

from bs4 import BeautifulSoup
from api._lib.getRequestSession import getRequestSession

ASSIGNMENTS_URL = "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx"

def get_or_none(tds, i):
    """Return tds[i] if present, else None."""
    return tds[i] if i < len(tds) else None

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        query = parse.urlsplit(self.path).query
        params = dict(parse.parse_qsl(query))

        username = params.get("username")
        password = params.get("password")

        if not username or not password:
            return self._send_json(
                {"error": "Missing username or password in query parameters."},
                status=400,
            )

        try:
            session = getRequestSession(username, password)

            resp = session.get(ASSIGNMENTS_URL, timeout=10)
            resp.raise_for_status()
            html = resp.text

            soup = BeautifulSoup(html, "lxml")

            courses = []

            for course_div in soup.find_all("div", class_="AssignmentClass"):
                new_course = {
                    "name": None,
                    "grade": None,
                    "lastUpdated": None,
                    "assignments": [],
                }

                # ---- Header block ----
                header_div = course_div.find("div", class_="sg-header sg-header-square")
                if header_div:

                    # Course name
                    name_tag = header_div.find("a", class_="sg-header-heading")
                    new_course["name"] = name_tag.get_text(strip=True) if name_tag else None

                    # Last updated
                    lu_tag = header_div.find("span", class_="sg-header-sub-heading")
                    if lu_tag:
                        text = lu_tag.get_text(strip=True)
                        text = text.replace("(Last Updated: ", "").replace(")", "").strip()
                        new_course["lastUpdated"] = text

                    # Grade
                    grade_tag = header_div.find("span", class_="sg-header-heading sg-right")
                    if grade_tag:
                        grade_text = grade_tag.get_text(strip=True)
                        grade_text = (
                            grade_text.replace("Student Grades ", "").replace("%", "").strip()
                        )
                        new_course["grade"] = grade_text

                content_div = course_div.find("div", class_="sg-content-grid")
                if content_div:
                    rows = content_div.find_all("tr", class_="sg-asp-table-data-row")

                    for row in rows:
                        tds = [td.get_text(strip=True) for td in row.find_all("td")]

                        assignment_date_due = get_or_none(tds, 0)
                        assignment_date_assigned = get_or_none(tds, 1)
                        assignment_name = get_or_none(tds, 2)
                        assignment_category = get_or_none(tds, 3)
                        assignment_score = get_or_none(tds, 4)
                        assignment_total_points = get_or_none(tds, 5)

                        new_course["assignments"].append({
                            "name": assignment_name,
                            "category": assignment_category,
                            "dateAssigned": assignment_date_assigned,
                            "dateDue": assignment_date_due,
                            "score": assignment_score,
                            "totalPoints": assignment_total_points,
                        })

                courses.append(new_course)

            return self._send_json({"currentClasses": courses}, status=200)

        except Exception as e:
            return self._send_json(
                {"currentClasses": [], "error": "Failed to fetch assignments."},
                status=500,
            )

    def _send_json(self, payload, status=200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

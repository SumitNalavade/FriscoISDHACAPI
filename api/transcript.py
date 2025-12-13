from http.server import BaseHTTPRequestHandler
from urllib import parse
import json

from bs4 import BeautifulSoup
from api._lib.getRequestSession import getRequestSession
from api._lib.parsers import _get_text_or_empty_by_id

TRANSCRIPT_URL = "https://hac.friscoisd.org/HomeAccess/Content/Student/Transcript.aspx"


def _get_text_or_empty(tag, selector=None, **find_kwargs):
    """
    Given a BeautifulSoup Tag, optionally run .find() on it,
    and return stripped text or "" if not found.
    """
    if tag is None:
        return ""
    if selector is not None:
        tag = tag.select_one(selector)
    elif find_kwargs:
        tag = tag.find(**find_kwargs)
    return tag.get_text(strip=True) if tag else ""

def get_or_none(tds, i):
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

            resp = session.get(TRANSCRIPT_URL)
            resp.raise_for_status()
            html = resp.text

            soup = BeautifulSoup(html, "lxml")

            transcript_details = []

            transcript_groups = soup.find_all("td", class_="sg-transcript-group")

            for idx, group in enumerate(transcript_groups):
                # Each group has three tables: header, courses, totals
                inner_tables = group.find_all("table")

                header_table, courses_table, total_credits_table = inner_tables[:3]

                years_attended = _get_text_or_empty(
                    header_table,
                    id=f"plnMain_rpTranscriptGroup_lblYearValue_{idx}",
                    name="span",
                )
                grade_level = _get_text_or_empty(
                    header_table,
                    id=f"plnMain_rpTranscriptGroup_lblGradeValue_{idx}",
                    name="span",
                )
                building = _get_text_or_empty(
                    header_table,
                    id=f"plnMain_rpTranscriptGroup_lblBuildingValue_{idx}",
                    name="span",
                )

                course_details = []
                course_rows = courses_table.find_all("tr", class_="sg-asp-table-data-row")

                for course_row in course_rows:
                    tds = [td.get_text(strip=True) for td in course_row.find_all("td")]

                    course_details.append({
                        "courseCode":    get_or_none(tds, 0),
                        "courseName":    get_or_none(tds, 1),
                        "sem1Grade":     get_or_none(tds, 2),
                        "sem2Grade":     get_or_none(tds, 3),
                        "finalGrade":    get_or_none(tds, 4),
                        "courseCredits": get_or_none(tds, 5),
                    })

                total_credits = _get_text_or_empty(
                    total_credits_table,
                    id=f"plnMain_rpTranscriptGroup_LblTCreditValue_{idx}",
                    name="label",
                )

                transcript_details.append({
                    "yearsAttended": years_attended,
                    "gradeLevel":    grade_level,
                    "building":      building,
                    "totalCredits":  total_credits,
                    "courses":       course_details,
                })
            
            student_weighted_gpa = _get_text_or_empty_by_id(
                soup, "plnMain_rpTranscriptGroup_lblGPACum1")
            student_unweighted_gpa = _get_text_or_empty_by_id(
                soup, "plnMain_rpTranscriptGroup_lblGPACum2")
            student_rank = _get_text_or_empty_by_id(
                soup, "plnMain_rpTranscriptGroup_lblGPARank1")

            return self._send_json({
                "studentTranscript": transcript_details,
                "weightedGPA": student_weighted_gpa,
                "unweightedGPA": student_unweighted_gpa,
                "rank": student_rank,
            }, status=200)

        except Exception:
            return self._send_json(
                {"studentTranscript": [], "error": "Failed to fetch transcript."},
                status=500,
            )

    def _send_json(self, payload, status=200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

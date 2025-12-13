from http.server import BaseHTTPRequestHandler
from urllib import parse
import json

from bs4 import BeautifulSoup
from api._lib.getRequestSession import getRequestSession


SCHEDULE_URL = "https://hac.friscoisd.org/HomeAccess/Content/Student/Classes.aspx"

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

            resp = session.get(SCHEDULE_URL)
            resp.raise_for_status()
            html = resp.text

            soup = BeautifulSoup(html, "lxml")

            schedule = []
            # Find all schedule rows in the main schedule table
            for row in soup.select("#plnMain_dgSchedule > tr.sg-asp-table-data-row"):
                tds = [td.get_text(strip=True) for td in row.find_all("td")]

                schedule.append({
                    "building":       get_or_none(tds, 7),
                    "courseCode":     get_or_none(tds, 0),
                    "courseName":     get_or_none(tds, 1),
                    "days":           get_or_none(tds, 5),
                    "markingPeriods": get_or_none(tds, 6),
                    "periods":        get_or_none(tds, 2),
                    "room":           get_or_none(tds, 4),
                    "status":         get_or_none(tds, 8),
                    "teacher":        get_or_none(tds, 3),
                })

            return self._send_json({"studentSchedule": schedule}, status=200)

        except Exception:
            return self._send_json(
                {"studentSchedule": [], "error": "Failed to fetch schedule."},
                status=500,
            )

    def _send_json(self, payload, status=200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

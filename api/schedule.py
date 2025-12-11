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
        # --- Parse query parameters ---
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
            # --- Authenticated session ---
            session = getRequestSession(username, password)

            # --- Fetch schedule page ---
            resp = session.get(SCHEDULE_URL, timeout=10)
            resp.raise_for_status()
            html = resp.text

            # --- Parse once ---
            soup = BeautifulSoup(html, "lxml")

            schedule = []
            # Find all schedule rows
            for row in soup.select("#plnMain_dgSchedule > tr.sg-asp-table-data-row"):
                # Directly get <td> cells in this row
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
            # In real code you’d log the exception
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

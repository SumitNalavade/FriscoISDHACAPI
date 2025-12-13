from http.server import BaseHTTPRequestHandler
from urllib import parse
import json
import re
from datetime import datetime

from bs4 import BeautifulSoup
from api._lib.getRequestSession import getRequestSession

ATTENDANCE_URL = "https://hac.friscoisd.org/HomeAccess/Content/Attendance/MonthlyView.aspx"

def format_attendance_entries(attendance):
    if not attendance.get("month") or not attendance.get("year"):
        return []

    month_num = datetime.strptime(attendance["month"], "%B").month
    year = attendance["year"]

    formatted = []

    for entry in attendance.get("entries", []):
        events = entry.get("events", [])
        if not events:
            continue

        day = entry["day"]
        date_str = f"{year}-{month_num:02d}-{day:02d}"

        formatted_events = []
        for e in events:
            period = e.get("period")

            if "status" in e:
                label = e["status"]
            elif "reason" in e:
                label = e["reason"]
            elif "note" in e:
                label = e["note"]
            else:
                continue

            formatted_events.append(f"Period {period}: {label}")

        if formatted_events:
            formatted.append({
                "date": date_str,
                "events": formatted_events
            })

    return formatted


def parse_events(title):
    if not title:
        return []

    lines = [l.strip() for l in title.splitlines() if l.strip()]
    events = []

    i = 0
    while i < len(lines):
        if lines[i].isdigit():
            event = {"period": int(lines[i])}
            i += 1

            if i < len(lines) and not lines[i].isdigit():
                text = lines[i]
                i += 1

                if "present" in text.lower():
                    event["status"] = "Present"
                elif "excused" in text.lower():
                    event["status"] = "Excused"
                    event["reason"] = text
                else:
                    event["note"] = text

            events.append(event)
        else:
            i += 1

    return events


def parse_attendance(html):
    soup = BeautifulSoup(html, "lxml")

    # Month + year
    header = soup.select_one(".sg-asp-calendar-header td[align='center']")
    if not header:
        return {
            "month": None,
            "year": None,
            "entries": []
        }

    header_text = header.get_text(strip=True)
    parts = header_text.split()

    if len(parts) != 2:
        return {
            "month": None,
            "year": None,
            "entries": []
        }

    month, year = parts
    year = int(year)

    entries = []

    # Calendar day cells
    for td in soup.select("td[align='center']"):
        day = td.get_text(strip=True)
        if not day.isdigit():
            continue

        title = td.get("title")
        if not title:
            continue

        date = f"{year}-{month}-{day.zfill(2)}"

        entries.append({
            "day": int(day),
            "rawTitle": title,
            "events": parse_events(title)
        })

    return {
        "month": month,
        "year": int(year),
        "entries": entries
    }


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        params = dict(parse.parse_qsl(parse.urlsplit(self.path).query))
        username = params.get("username")
        password = params.get("password")

        if not username or not password:
            return self._send_json({"error": "Missing username or password"}, 400)

        try:
            session = getRequestSession(username, password)
            resp = session.get(ATTENDANCE_URL)
            resp.raise_for_status()

            attendance = parse_attendance(resp.text)
            formatted = format_attendance_entries(attendance)

            return self._send_json(formatted)



        except Exception as e:
            return self._send_json({"error": str(e)}, 500)

    def _send_json(self, payload, status=200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

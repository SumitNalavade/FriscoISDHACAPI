from http.server import BaseHTTPRequestHandler
from urllib import parse
import json
import re
from datetime import datetime

from bs4 import BeautifulSoup
from api._lib.getRequestSession import getRequestSession

WEEKLY_SCHEDULE_URL = "https://hac.friscoisd.org/HomeAccess/Home/WeekView"

def to_iso(date_str):
    try:
        return datetime.strptime(date_str, "%m/%d/%Y").date().isoformat()
    except Exception:
        return None


def parse_assignment_title_attr(title_attr):
    """
    Parses the multiline title="" attribute HAC uses.
    Returns a dict of metadata.
    """
    meta = {}
    if not title_attr:
        return meta

    for line in title_attr.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip().lower()
        value = value.strip()

        if key == "due date":
            meta["dueDate"] = to_iso(value)
        elif key == "max points":
            try:
                meta["maxScore"] = float(value)
            except:
                meta["maxScore"] = value
        elif key == "category":
            meta["category"] = value
        elif key == "type":
            meta["type"] = value
        elif key == "can be dropped":
            meta["canBeDropped"] = value.upper() == "Y"
        elif key == "extra credit":
            meta["extraCredit"] = value.upper() == "Y"
        elif key == "has attachments":
            meta["hasAttachments"] = value.upper() == "Y"

    return meta


def parse_grade(text):
    if not text:
        return {}

    t = text.strip()

    # CNS, X, etc.
    if re.fullmatch(r"[A-Za-z]+", t):
        return {"status": t}

    # numeric grade
    m = re.match(r"([0-9]+(?:\.[0-9]+)?)\s*/\s*([0-9]+(?:\.[0-9]+)?)", t)
    if m:
        return {
            "score": float(m.group(1)),
            "maxScore": float(m.group(2)),
            "gradeText": t
        }

    return {"gradeText": t}


def parse_weekly_schedule(html):
    soup = BeautifulSoup(html, "lxml")

    table = soup.select_one(".sg-homeview-table")
    if not table:
        return {"days": {}}

    # -------------------------
    # Parse header (days)
    # -------------------------
    days = []
    for td in table.select("thead td.sg-cell-width"):
        text = td.get_text("\n", strip=True)

        weekday = None
        cycle = None
        full_date = None

        for line in text.splitlines():
            if line in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
                weekday = line
            elif "Day:" in line:
                cycle = line.replace("Day:", "").strip()

        a = td.find("a", href=True)
        if a:
            m = re.search(r"'(\d{2}/\d{2}/\d{4})'", a["href"])
            if m:
                full_date = to_iso(m.group(1))

        if full_date:
            days.append({
                "date": full_date,
                "weekday": weekday,
                "cycle": cycle
            })

    result = {
        "days": {
            d["date"]: {
                "weekday": d["weekday"],
                "classes": []
            }
            for d in days
        }
    }

    # -------------------------
    # Parse body (rows)
    # -------------------------
    for row in table.select("tbody > tr"):
        tds = row.find_all("td", recursive=False)
        if not tds:
            continue

        # ---- course info ----
        course_td = tds[0]
        name_el = course_td.select_one("a.sg-font-larger")
        teacher_el = course_td.select_one("#staffName")
        period_text = course_td.find(string=re.compile(r"Per:"))

        if not name_el:
            continue

        course_name = name_el.get_text(strip=True)
        teacher = teacher_el.get_text(strip=True) if teacher_el else None
        period = period_text.replace(
            "Per:", "").strip() if period_text else None

        # ---- per-day cells ----
        for i, day in enumerate(days):
            cell_index = i + 1
            if cell_index >= len(tds):
                continue

            cell = tds[cell_index]

            if "sg-home-table-cell-disabled" in cell.get("class", []):
                continue

            items = []

            # notes
            for span in cell.select("span[style]"):
                items.append({
                    "type": "note",
                    "text": span.get_text(strip=True)
                })

            # assignments
            for span in cell.select("span.sg-assignment-description"):
                title_el = span.find("a")
                if not title_el:
                    continue

                assignment = {
                    "title": title_el.get_text(strip=True)
                }

                # metadata from title=""
                meta = parse_assignment_title_attr(span.get("title"))
                assignment.update(meta)

                # grade / status
                grade_el = span.select_one(".sg-right")
                if grade_el:
                    assignment.update(parse_grade(grade_el.get_text()))

                items.append(assignment)

            result["days"][day["date"]]["classes"].append({
                "name": course_name,
                "period": period,
                "teacher": teacher,
                "items": items
            })

    return result

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse.urlsplit(self.path).query
        params = dict(parse.parse_qsl(query))

        username = params.get("username")
        password = params.get("password")
        startDate = params.get("startdate")

        url = WEEKLY_SCHEDULE_URL

        if(startDate):
            url += f"?startDate={startDate}"

        if not username or not password:
            return self._send_json(
                {"error": "Missing username or password."},
                status=400
            )

        try:
            session = getRequestSession(username, password)

            resp = session.get(url, timeout=15)
            resp.raise_for_status()

            schedule = parse_weekly_schedule(resp.text)

            return self._send_json(
                {"studentSchedule": schedule},
                status=200
            )

        except Exception as e:
            return self._send_json(
                {"error": str(e)},
                status=500
            )

    def _send_json(self, payload, status=200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

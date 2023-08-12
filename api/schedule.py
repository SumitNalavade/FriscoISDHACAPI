from http.server import BaseHTTPRequestHandler
from bs4 import BeautifulSoup
import json
import lxml
from urllib import parse

from api._lib.getRequestSession import getRequestSession

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        dic = dict(parse.parse_qsl(parse.urlsplit(self.path).query))

        username = dic["username"]
        password = dic["password"]

        session = getRequestSession(username, password)

        schedulePageContent = session.get(
            "https://hac.friscoisd.org/HomeAccess/Content/Student/Classes.aspx").text

        parser = BeautifulSoup(schedulePageContent, "lxml")

        schedule = []

        courses = parser.find_all("tr", "sg-asp-table-data-row")

        for row in courses:
            parser = BeautifulSoup(f"<html><body>{row}</body></html>", "lxml")
            tds = [x.text.strip() for x in parser.find_all("td")]

            if(len(tds) > 3):
                schedule.append({
                    "building": tds[7],
                    "courseCode": tds[0],
                    "courseName": tds[1],
                    "days": tds[5],
                    "markingPeriods": tds[6],
                    "periods": tds[2],
                    "room": tds[4],
                    "status": tds[8],
                    "teacher": tds[3],
                })

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({
            "studentSchedule": schedule,
        }).encode(encoding="utf_8"))

        return

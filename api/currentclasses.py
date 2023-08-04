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

        coursesPageContent = session.get(
            "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx").text

        parser = BeautifulSoup(coursesPageContent, "lxml")

        courses = []

        courseContainer = parser.find_all("div", "AssignmentClass")

        for container in courseContainer:
            newCourse = {
                "name": "",
                "grade": "",
                "lastUpdated": "",
                "assignments": []
            }
            parser = BeautifulSoup(
                f"<html><body>{container}</body></html>", "lxml")
            headerContainer = parser.find_all(
                "div", "sg-header sg-header-square")
            assignementsContainer = parser.find_all("div", "sg-content-grid")

            for hc in headerContainer:
                parser = BeautifulSoup(
                    f"<html><body>{hc}</body></html>", "lxml")

                newCourse["name"] = parser.find(
                    "a", "sg-header-heading").text.strip()

                newCourse["lastUpdated"] = parser.find(
                    "span", "sg-header-sub-heading").text.strip().replace("(Last Updated: ", "").replace(")", "")

                newCourse["grade"] = parser.find("span", "sg-header-heading sg-right").text.strip(
                ).replace("Student Grades ", "").replace("%", "")

            for ac in assignementsContainer:
                parser = BeautifulSoup(
                    f"<html><body>{ac}</body></html>", "lxml")
                rows = parser.find_all("tr", "sg-asp-table-data-row")
                for assignmentContainer in rows:
                    try:
                        parser = BeautifulSoup(
                            f"<html><body>{assignmentContainer}</body></html>", "lxml")
                        tds = parser.find_all("td")
                        assignmentName = parser.find("a").text.strip()
                        assignmentDateDue = tds[0].text.strip()
                        assignmentDateAssigned = tds[1].text.strip()
                        assignmentCategory = tds[3].text.strip()
                        assignmentScore = tds[4].text.strip()
                        assignmentTotalPoints = tds[5].text.strip()

                        newCourse["assignments"].append(
                            {
                                "name": assignmentName,
                                "category": assignmentCategory,
                                "dateAssigned": assignmentDateAssigned,
                                "dateDue": assignmentDateDue,
                                "score": assignmentScore,
                                "totalPoints": assignmentTotalPoints
                            }
                        )
                    except:
                        pass

                courses.append(newCourse)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({
            "currentClasses": courses,
        }).encode(encoding="utf_8"))

        return

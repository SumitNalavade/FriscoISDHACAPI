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

        schedulePageContent = session.get("https://hac.friscoisd.org/HomeAccess/Content/Student/Transcript.aspx").text

        parser = BeautifulSoup(schedulePageContent, "lxml")

        transcriptGroup = parser.find_all("td", "sg-transcript-group")

        transcriptDetails = []
        for index, transcript in enumerate(transcriptGroup):
            parser = BeautifulSoup(f"<html><body>{transcript}</body></html>", "lxml")
            innerTables = parser.find_all('table')
            
            headerTable = innerTables[0]
            coursesTable = innerTables[1]
            totalCreditsTable = innerTables[2]

            parser = BeautifulSoup(f"<html><body>{headerTable}</body></html>", "lxml")
            yearsAttended = parser.find('span', id=f'plnMain_rpTranscriptGroup_lblYearValue_{index}').text.strip()
            gradeLevel = parser.find('span', id=f'plnMain_rpTranscriptGroup_lblGradeValue_{index}').text.strip()
            building = parser.find('span', id=f'plnMain_rpTranscriptGroup_lblBuildingValue_{index}').text.strip()

            parser = BeautifulSoup(f"<html><body>{coursesTable}</body></html>", "lxml")
            courseRows = parser.find_all('tr', 'sg-asp-table-data-row')

            courseDetails = []

            for courseRow in courseRows:
                parser = BeautifulSoup(f"<html><body>{courseRow}</body></html>", "lxml")
                courseInfo = parser.find_all('td')

                courseCode = courseInfo[0].text.strip()
                courseName = courseInfo[1].text.strip()
                sem1Grade = courseInfo[2].text.strip()
                sem2Grade = courseInfo[3].text.strip()
                finalGrade = courseInfo[4].text.strip()
                courseCredits = courseInfo[5].text.strip()

                courseDetails.append({ 'courseCode': courseCode, 'courseName': courseName, 'sem1Grade': sem1Grade, 'sem2Grade': sem2Grade, 'finalGrade': finalGrade, 'courseCredits': courseCredits })

            parser = BeautifulSoup(f"<html><body>{totalCreditsTable}</body></html>", "lxml")
            totalCredits = parser.find('label', id=f'plnMain_rpTranscriptGroup_LblTCreditValue_{index}').text

            transcriptDetails.append({ 'yearsAttended': yearsAttended, 'gradeLevel': gradeLevel, 'building': building, 'totalCredits': totalCredits, 'courses': courseDetails })
            
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({
            "studentTranscript": transcriptDetails,
        }).encode(encoding="utf_8"))

        return
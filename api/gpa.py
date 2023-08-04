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

        transcriptPageContent = session.get(
            "https://hac.friscoisd.org/HomeAccess/Content/Student/Transcript.aspx").text

        parser = BeautifulSoup(transcriptPageContent, "lxml")

        weightedGpa = parser.find(
            id="plnMain_rpTranscriptGroup_lblGPACum1").text
        unweightedGpa = parser.find(
            id="plnMain_rpTranscriptGroup_lblGPACum2").text
        
        totalCredits = 0

        for i in range(8):
            credits = parser.find(id=f'plnMain_rpTranscriptGroup_LblTCreditValue_{i}')

            if(credits != None):
                totalCredits += float(credits.text)
            
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({
            "weightedGPA": weightedGpa,
            "unweightedGPA": unweightedGpa,
            "totalCredits": str(totalCredits)
        }).encode(encoding="utf_8"))

        return

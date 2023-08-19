from http.server import BaseHTTPRequestHandler
from bs4 import BeautifulSoup
import json
import lxml
import cchardet
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

        rank = None
        weightedGpa = parser.find(
            id="plnMain_rpTranscriptGroup_lblGPACum1").text
        unweightedGpa = parser.find(
            id="plnMain_rpTranscriptGroup_lblGPACum2").text
        
        try:
            rank = parser.find(id='plnMain_rpTranscriptGroup_lblGPARank1').text
        except:
            pass

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({
            "weightedGPA": weightedGpa,
            "unweightedGPA": unweightedGpa,
            'rank': rank
        }).encode(encoding="utf_8"))

        return

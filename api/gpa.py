from http.server import BaseHTTPRequestHandler
from bs4 import BeautifulSoup
import json
import lxml
import cchardet
from urllib import parse

from _lib.getRequestSession import getRequestSession

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    dic = dict(parse.parse_qsl(parse.urlsplit(self.path).query))

    print(f"REQUEST IP: {self.client_address[0]}")

    username = dic["username"]
    password = dic["password"]

    session = getRequestSession(username, password)

    transcriptPageContent = session.get("https://hac.friscoisd.org/HomeAccess/Content/Student/Transcript.aspx").text

    parser =  BeautifulSoup(transcriptPageContent, "lxml")

    weightedGpa = parser.find(id="plnMain_rpTranscriptGroup_lblGPACum1").text
    unweightedGpa = parser.find(id="plnMain_rpTranscriptGroup_lblGPACum2").text

    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps({
      "weightedGPA": weightedGpa,
      "unweightedGPA": unweightedGpa
    }).encode(encoding="utf_8"))

    return

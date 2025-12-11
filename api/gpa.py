from http.server import BaseHTTPRequestHandler
from urllib import parse
import json

from bs4 import BeautifulSoup
from api._lib.getRequestSession import getRequestSession


def _get_text_or_empty_by_id(soup: BeautifulSoup, element_id: str) -> str:
    """Return the stripped text of an element by id, or empty string if missing."""
    el = soup.find(id=element_id)
    return el.get_text(strip=True) if el else ""

TRANSCRIPT_URL = "https://hac.friscoisd.org/HomeAccess/Content/Student/Transcript.aspx"

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse.urlsplit(self.path).query
        params = dict(parse.parse_qsl(query))

        username = params.get("username")
        password = params.get("password")

        if not username or not password:
            self._send_json(
                {"error": "Missing username or password in query parameters."},
                status=400,
            )
            return

        try:
            session = getRequestSession(username, password)

            transcript_page_response = session.get(TRANSCRIPT_URL)
            transcript_page_response.raise_for_status()
            transcript_page_html = transcript_page_response.text

            transcript_page_soup = BeautifulSoup(transcript_page_html, 'lxml')

            student_weighted_gpa = _get_text_or_empty_by_id(
                transcript_page_soup, "plnMain_rpTranscriptGroup_lblGPACum1")
            student_unweighted_gpa = _get_text_or_empty_by_id(
                transcript_page_soup, "plnMain_rpTranscriptGroup_lblGPACum2")
            student_rank = _get_text_or_empty_by_id(
                transcript_page_soup, "plnMain_rpTranscriptGroup_lblGPARank1")

            data = {
                "weightedGPA": student_weighted_gpa,
                "unweightedGPA": student_unweighted_gpa,
                "rank": student_rank
            }

            self._send_json(data, status=200)

        except Exception as e:
            self._send_json(
                {"error": "Failed to fetch student GPAs."},
                status=500,
            )

    def _send_json(self, payload, status: int = 200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

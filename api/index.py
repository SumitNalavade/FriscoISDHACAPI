from http.server import BaseHTTPRequestHandler

from api._lib.getRequestSession import getRequestSession


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"REQUEST IP: {self.client_address[0]}")

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("""
    <h1>Frisco ISD HAC API</h1>
	<p>Documentation:</p>
	<a href="https://friscoisdhacapi.vercel.app/" target="_blank">https://friscoisdhacapi.vercel.app/</a>
    """.encode(encoding="utf_8"))

        return

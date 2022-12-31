from http.server import BaseHTTPRequestHandler

from _lib.sendIp import sendIp

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    sendIp(self.client_address[0])

    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write("""
    <h1>Frisco ISD HAC API</h1>
	<p>Documentation:</p>
	<a href="https://friscoisdhacapidocs.vercel.app/" target="_blank">https://friscoisdhacapidocs.vercel.app/</a>
    """.encode(encoding="utf_8"))

    return

from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
from datetime import datetime

PORT = 8080

class GeoTrackerHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        query = urlparse.parse_qs(parsed_path.query)
        if parsed_path.path == "/logme" and "coords" in query:
            coords = query["coords"][0]
            with open("locations.log", "a") as f:
                f.write(f"{datetime.now()}: {coords}\n")
            print(f"[+] Logged location: {coords}")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Location logged!")
        else:
            super().do_GET()

if __name__ == "__main__":
    print(f"[*] Starting server on http://localhost:{PORT}")
    server = HTTPServer(("0.0.0.0", PORT), GeoTrackerHandler)
    server.serve_forever()

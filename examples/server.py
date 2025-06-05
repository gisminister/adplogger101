import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

PORT = 8000

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
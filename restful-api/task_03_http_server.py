from http.server import HTTPServer, BaseHTTPRequestHandler
import json
""" Developing a simple API using Python with the http.server"""


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """launching a server using port 8000"""
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status_data = {"status": "OK"}
            self.wfile.write(json.dumps(status_data).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    print("servint at port 8000")
    httpd.serve_forever()


"""with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
    """

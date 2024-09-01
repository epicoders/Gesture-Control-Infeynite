from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/callback'):
            query_components = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            code = query_components.get('code')
            if code:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'Authorization code received. You can close this window.')
                print(f'Authorization Code: {code[0]}')
            else:
                self.send_response(400)
                self.wfile.write(b'Error: No code received.')
        else:
            self.send_response(404)
            self.wfile.write(b'Error: Not Found.')

def run(server_class=HTTPServer, handler_class=RequestHandler, port=9000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

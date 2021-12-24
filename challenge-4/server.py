#!/usr/bin/env python3

import http.server
import logging
import socketserver

PORT = 8080
logging.basicConfig(level=logging.INFO)

class GetHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        print(self.headers)

        header_ok = ""
        for h in self.headers:
          if h == 'Challenge' and self.headers[h] == 'intelygenz.com':
             header_ok = True

        if header_ok:
          self.send_response(200)
          self.send_header('Content-type', 'text/html')
          self.end_headers()
          self.wfile.write(b"Everything works!")
        else:
          self.send_response(404)
          self.send_header('Content-type', 'text/html')
          self.end_headers()
          self.wfile.write(b"Wrong header!")


if __name__ == '__main__':
    Handler = GetHandler
    server = socketserver.TCPServer(("", PORT), Handler)
    logging.info(f'Listening on {PORT}...\n')

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()

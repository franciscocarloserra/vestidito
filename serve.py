#!/usr/bin/env python3
"""Static server for index.html + POST /log -> browser console telemetry (jsonl)."""
import http.server, os, sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 7810
LOG = '/tmp/vestidito-console.jsonl'

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class H(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        body = self.rfile.read(int(self.headers.get('Content-Length', 0))).decode(errors='replace')
        with open(LOG, 'a') as f:
            f.write(body.strip() + '\n')
        self.send_response(204)
        self.end_headers()

    def end_headers(self):  # no caching: edits show up on plain reload
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def log_message(self, *a):
        pass

http.server.ThreadingHTTPServer(('127.0.0.1', PORT), H).serve_forever()

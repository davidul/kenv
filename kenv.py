from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import json


class KEnvHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("Get accepted")
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        kv_env = self.getenv()
        kv_sys = self.sysinfo()
        kv = {'sysinfo': kv_sys, 'environment': kv_env}
        self.wfile.write(json.dumps(kv).encode('utf-8'))

    def getenv(self):
        kv = {}
        keys = os.environ.keys()
        for k in keys:
            v = os.environ.get(k)
            kv[k] = v
        return kv

    def sysinfo(self):
        kv = {'os-uname': os.uname(), 'os-name': os.name}
        return kv


def run(server_class=HTTPServer, handler_class=KEnvHandler, port=9090):
    server_address = ('', port)
    server = server_class(server_address, handler_class)
    server.serve_forever()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

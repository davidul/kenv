from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import json
import argparse


class KEnvHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("Get accepted")
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        kv_env = getenv()
        kv_sys = self.sysinfo()
        kv = {'sysinfo': kv_sys, 'environment': kv_env}
        self.wfile.write(json.dumps(kv).encode('utf-8'))

    def sysinfo(self):
        kv = {'os-uname': os.uname(), 'os-name': os.name}
        return kv


def getenv():
    kv = {}
    keys = os.environ.keys()
    for k in keys:
        v = os.environ.get(k)
        kv[k] = v
    return kv


def run(server_class=HTTPServer, handler_class=KEnvHandler, port=9090):
    server_address = ('', port)
    server = server_class(server_address, handler_class)
    server.serve_forever()


def run_local():
    kv_env = {"environment": getenv()}
    print(f"{json.dumps(kv_env, indent=4)}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Kenv options")
    parser.add_argument('--server', dest="server", type=str, help="run http server")
    parser.add_argument('--port', dest="port", type=int, help="http server port", default=9090)
    args = parser.parse_args()

    if args.server:
        run(port=args.port)
    else:
        run_local()

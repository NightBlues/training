import BaseHTTPServer
import socket

import SimpleHTTPServer


class Server(BaseHTTPServer.HTTPServer):
    address_family = socket.AF_INET6


SimpleHTTPServer.test(ServerClass=Server)

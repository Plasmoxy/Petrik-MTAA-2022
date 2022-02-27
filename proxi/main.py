"""
==== SIP proxy ===

1. zadanie z MTAA
Sebastián Petrík
19.2.2022
MTAA

SIP proxy using modified library by Philppe Thirion
Original code: https://github.com/tirfil/PySipFullProxy/blob/master/sipfullproxy.py
Original license: gpl.txt

"""

import pysipfullproxy
import sys
from socketserver import UDPServer
import socket

if __name__ == "__main__":
    print("=== Assignment 1 from MTAA 27.2.2022 Sebastian Petrik ===")
    print("SIP proxy modified to run on python 3.9 with improvements.")
    
    hostn, n, ips = socket.gethostbyname_ex(socket.gethostname())
    print("Select IP for proxy (enter number): ")
    for i in range(len(ips)):
        print(f"{i} = {ips[i]}")
    ipidx = int(input("Enter choice number: "))
    ip = ips[ipidx]
    
    port = 5060
    
    print("ip is ", ip)
    print("port is ", port)
    
    pysipfullproxy.init_module(ip, port)
    server = UDPServer((ip, port), pysipfullproxy.UDPHandler)
    
    print("Starting udp server with proxy handler.")
    server.serve_forever()
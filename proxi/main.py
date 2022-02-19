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

if __name__ == "__main__":
    print("SIP proxy modified by Sebastian Petrik to run on python 3.9, works with zoiper")
    
    ip = sys.argv[1]
    port = 5060
    
    print("ip is ", ip)
    print("port is ", port)
    
    pysipfullproxy.init_module(ip, port)
    server = UDPServer((ip, port), pysipfullproxy.UDPHandler)
    
    print("starting udp server - proxy")
    server.serve_forever()
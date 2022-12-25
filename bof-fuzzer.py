#!/usr/bin/env python

import sys
import socket
import time

data = "A" * 500
max_input = 3300

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("IP-ADDRESS", 2233))

try:
    while len(data) <= max_input:
        increment = "A" * 500
        print("[+] Fuzzing with " + str(len(data)))
        s.send(data.encode())
        time.sleep(0.1)
        data += increment
except BrokenPipeError:
    print("[!] Closing connection!")
    sys.exit()

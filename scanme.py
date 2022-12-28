#!/usr/bin/env python2

'''
Author: autom4il
Date: 28/12/22
Description: During the OSCP labs you may need to take the nmap static binary
                over but in case there is some compatibility issue and nc is to
                slow you can use this python "port scanner" is available on the
                target machine.
'''

import threading
import socket
import sys

def scan_port(host, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    # return 0 if the operation succeeded
    result = sock.connect_ex((host, port))
    if result == 0:
        print('Port %d is open') % port
    sock.close()

def main():

    host = ''
    if len(sys.argv) == 1:
        host = sys.argv[1]
    else:
        print('Usage: ' + sys.argv[0] + ' <target-ip-address>')

    # Ports to scan
    top_ports = [

        80, 443, 22, 21, 23, 25, 53,
        110, 143, 135, 139, 445, 3389,
        8080, 1723, 1080, 554,
        2049, 515, 6667, 514,
        179, 199, 5666, 113, 3306, 1433,
    
    ] 

    threads = []
    for port in top_ports:
        # Wait until there are fewer than 4 active threads
        while threading.active_count() > 2:  
            pass
        t = threading.Thread(target=scan_port, args=(host, port))
        threads.append(t)
        t.start()

if __name__ == '__main__':
    main()

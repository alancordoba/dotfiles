#!/usr/bin/env python3
# SSH helper - Check if hostname belongs to network
# Usage: ipnet.py network hostname
# Example: ipnet.py 172.16.0.0/16 172.16.0.1
# Exit codes: 0 - true, 1 - false
import ipaddress
import socket
import sys
exit(
    int(
        not ipaddress.ip_address(socket.gethostbyname(sys.argv[2]))
            in ipaddress.ip_network(sys.argv[1])
    )
)

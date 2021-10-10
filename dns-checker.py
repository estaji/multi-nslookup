#!/usr/bin/env python3

# By Omid Estaji - estaji.work@gmail.com - 1400/07/16
# Compatible to Python3
# Usage: #python3 dns-checker.py

import socket
import os

dns_server = input('What is your DNS server?\n e.g: ns1.parspack.net\n e.g: 8.8.8.8\n')
domain = input("What is your domain address?\n e.g: 0mid.net\n e.g: mail.0mid.net\n")
record_type = input("Which type of record are you looking for?\n e.g: a\n e.g: ptr\n")

addressInfo = socket.getaddrinfo(dns_server, 80, family=socket.AF_INET, proto=socket.IPPROTO_TCP)
ips = []

for index in addressInfo:
    ip = index[4][0]
    ips.append(index[4][0])

print("----- DNS server %s IPs -----\n %s" % (dns_server, ips))

for ip in ips:
    print('----- Server %s nslookup result -----' % (ip))
    cmd = "nslookup -type=%s %s %s" % (record_type, domain, ip)
    os.system(cmd)

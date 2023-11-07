#!/usr/bin/env python
from re import findall
from sys import argv

if len(argv) < 3:
    print("USAGE: sub-extract <domain> <file>")
    exit()

with open(argv[2]) as file:
    text = file.read()
    subdomains = findall(rf'(.[^:/]+\.)+{argv[1]}', text)
    for subdomain in subdomains:
        subdomain = subdomain.replace("https://","")
        subdomain = subdomain.replace("http://","")
        print(subdomain.replace("/","")+argv[1])
        

#!/usr/bin/env python3
# PyOVER - @mdakh404

import argparse
import dns.resolver
import requests
from requests.api import get
from termcolor import colored

class Subdomain(object):
    def __init__(self, subdomain):
        self.subdomain = subdomain
    
    def get_cname(self):
      try:
           results = dns.resolver.resolve(self.subdomain, 'CNAME')
           for cnameval in results:
               return cnameval.target
                       
      except:
          return 'NX'
        
    def get_status_code(self):
      try:
           req = requests.get(self.subdomain)
           return req.status_code
           
      except:
           return '-'
       
       
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-L', '--List', dest="subdomains", help='List of subdomains', required=True)
    return parser.parse_args()

def banner():
     print("")
     print(colored(" ___       _____   _____ ___ ", "red", attrs=["bold"]))
     print(colored("| _ \_  _ / _ \ \ / / __| _ \\", "red", attrs=["bold"]))
     print(colored("|  _/ || | (_) \ V /| _||   /", "red", attrs=["bold"]))
     print(colored("|_|  \_, |\___/ \_/ |___|_|_\\", "red", attrs=["bold"]))
     print(colored("     |__/      @mdakh404      ", "red", attrs=["bold"]))
     print("")


args = get_arguments()
banner()
print(colored("(+) Getting Live Subdomains", "yellow", attrs=[]))

def get_subdomains():
    subs = []
    with open(args.subdomains) as subdomains:
        for subdomain in subdomains.readlines():
            subdomain = subdomain.strip('\n').strip(' ')
            subs.append(subdomain)
            
    return subs

subdomains = get_subdomains()

print(colored("(+) Getting Started ...", "yellow", attrs=[]))
print("")

def subs_props(subdomains):
    
    for subdomain in subdomains:
        sub = Subdomain(subdomain)
        print(colored("-------------------------------------------", "grey", attrs=[]))
        print(colored("[+] subdomain    : ", "red"), colored(f"{subdomain}", "blue"))
        print(colored("[+] status_code  : ", "red"), colored(f"{sub.get_status_code()}", "green"))
        print(colored("[+] CNAME        : ", "red"), colored(f"{sub.get_cname()}", "white"))
        
subs_props(subdomains)
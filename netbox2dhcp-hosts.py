#!/usr/local/bin/python3.6
# vim: set expandtab sw=4 ts=4:

import django
import requests
from json import dumps
import sys
from config import *

from django.template.loader import get_template
from django.template import Context

settings.configure(TEMPLATES=TEMPLATES)
django.setup()
template = get_template('host.conf')

def hosts( subnet ):
    url = netbox_url + '/ipam/ip-addresses/?parent=%s'%subnet
    while url:
        res = requests.get( url, **requests_opts )
        r = res.json()
        if r:
            for ipaddress in r.get('results'):
                interface_url = ipaddress.get('interface',{}).get('url')
                res = requests.get( interface_url, **requests_opts )
                interface = res.json()
                ip = ipaddress.get('address')
                mac = interface.get('mac_address')
                name = interface.get('device',{}).get('name')
                if ip and mac and name:
                    args = {
                        'address': ip.split('/')[0],
                        'mac': mac.lower(), 
                        'name': name
                        }
                    print(template.render( args ))


            url = r.get('next')
        else:
            url = Noned

for subnet in sys.argv[1:]:
    hosts(subnet)



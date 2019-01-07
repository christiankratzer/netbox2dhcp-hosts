#!/usr/local/bin/python3.6
# vim: set expandtab sw=4 ts=4:

# netbox config
netbox_url = 'https://netbox.foo.bar/api'
netbox_token = 'foobarbaz'

requests_headers={ 
    'accept': 'application/json', 
    'authorization': 'Token {}'.format(netbox_token), 
    }

requests_opts={
    'timeout':3,
    'verify':True,
    'headers': requests_headers
    }

# django config
from django.conf import settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates'],
    }
    ]

# end

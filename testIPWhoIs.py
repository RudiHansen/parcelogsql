#!/usr/bin/python
# coding=utf-8

# Testing IPWhois
# 
from ipwhois import IPWhois
from pprint import pprint
from datetime import datetime
import warnings


warnings.filterwarnings("ignore")

start = datetime.now()
obj = IPWhois('189.123.10.146')
results = obj.lookup_rdap(depth=0)
end = datetime.now()
print((end - start))

countryCode = results['asn_country_code']
description = results['asn_description']

print countryCode
print description
print results
print((end - start))

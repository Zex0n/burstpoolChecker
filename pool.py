#!/usr/bin/env python3

url = 'http://pool.burstcoin.ro/pending2.json'
id = 'Numeric_Account_ID'

import urllib.request
import json
req = urllib.request.Request(url)

##parsing response
r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))
counter = 0

print ('%.2f' % cont['pendingPaymentList'][id])

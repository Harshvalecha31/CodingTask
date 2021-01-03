import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Dasher.settings")
django.setup()

from firstapp.models import Travel
import requests
import json
from requests.structures import CaseInsensitiveDict

url = "https://f0ztti2nsk.execute-api.ap-south-1.amazonaws.com/v1/consignment/fetch"

#apicalls
headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer tTU3gFVUdP"
headers["Content-Type"] = "application/json"
data = '{"email":"temp@gmail.com"}'
resp = requests.post(url, headers=headers, data=data)

#extracted data
data = json.loads(resp.text)
try:
    for i in range(len(data)):
        awb_num = data[i]['awbno']
        carrier = data[i]['carrier']
        cur_status = data[i]['current_status']
        code = data[i]['current_status_code']
        ETD = data[i]['extra_fields']['expected_delivery_date']
        source = data[i]['from']
        destination = data[i]['to']
        scandata = data[i]['scan']# list of data
        s2 = []
        for j in scandata:
            s2.append([j['time'],j['location']])
        s1 = json.dumps(s2)
        t1 = Travel(awb_num = awb_num,carrier = carrier,cur_status = cur_status,code = code,
        ETD = ETD,source = source,destination = destination,scandata = s1)
        t1.save()
        print('ok')
except KeyError:
    print('Done')
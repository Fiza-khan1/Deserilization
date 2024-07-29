import requests
import json
URL = 'http://127.0.0.1:8000/createstudent'

data = {
    "name": "Rahul",
    "roll": 104,
    "address": "Noida",
}
jdata =json.dumps(data)
r = requests.post(url= URL, data=jdata)
data = r.json()
print(data)
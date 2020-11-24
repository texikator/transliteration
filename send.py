import requests
import json

data = {"account_data": "Курбатова Анна", "location": "office"}
str_data = str(data)
data_encoded = str_data.encode('utf8')
headers = {'Content-Type': 'application/json'}
json_data = json.dumps(data)
print(type(json_data))
print(json_data)
url = 'http://localhost:5000/transliterate/api/v1.0/detailed'
#req = requests.post(url,data=data_encoded, headers=headers)
req = requests.post(url, json=data, headers=headers)
print(req)
print(req.status_code)
print(req.content)
print(req.text)

import http.client
import json
from flask import jsonify
from config import MMA_API_KEY, BASE_URL

conn = http.client.HTTPSConnection("v1.mma.api-sports.io")
headers = {
    'x-apisports-key': MMA_API_KEY
}
conn.request("GET", "/fighters?category=Heavyweight", headers=headers)
res = conn.getresponse()
raw_data = res.read().decode("utf-8")
data = json.loads(raw_data)
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

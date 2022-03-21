import requests

r = requests.get("http://ipinfo.io/json")

print(r.text)
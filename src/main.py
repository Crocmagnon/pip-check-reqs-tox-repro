import requests

res = requests.get("https://httpbin.org/get", timeout=2)
print(res.json())
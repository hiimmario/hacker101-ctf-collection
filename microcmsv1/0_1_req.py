import requests

try:
    r = requests.get("http://35.196.135.216/0aebe18f12/page/edit/7")
    print(r.content)
except Exception as e:
    print(e)
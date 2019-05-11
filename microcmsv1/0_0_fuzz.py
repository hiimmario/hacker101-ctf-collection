import requests

for i in range(0, 8000):
    try:
        r = requests.get("http://35.196.135.216/630e529e5c/page/" + str(i))
        print(i)
        print(r.content)
    except Exception as e:
        print(e)

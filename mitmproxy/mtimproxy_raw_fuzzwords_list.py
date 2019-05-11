# based on
# https://github.com/mitmproxy/mitmproxy/blob/v2.0.2/examples

from mitmproxy import io
from mitmproxy.exceptions import FlowReadException
import pprint
import requests
import time
from random import randint
import json

def is_json(subject):
    try:
        json.loads(subject)
    except Exception:
        return False
    return True

def loop_dict(d):
    flat = []
    for k, v in d.items():
        if isinstance(v, dict):
            #print("is dict: {}".format(v))
            loop_dict(v)
        else:
            #print("{} : {}".format(k, v))
            flat.append([k, v])
    return flat

logfile = "rawdump.txt"
flows = []

# pp = pprint.PrettyPrinter(indent=2)
try:
    logfile = open(logfile, "rb")
    freader = io.FlowReader(logfile)
    for f in freader.stream():
        # pp.pprint(f.get_state())
        flows.append(f)
except FlowReadException as e:
    print("Flow file corrupted: {}".format(e))
except IOError as e:
    print("Cant handle file: {}".format(e))

# [[url0, payload0], [url2, payload2]]
post_requests = [[flow.request.pretty_url, flow.request.content] for flow in flows if hasattr(flow, "request") and flow.request.method == "POST"]
fuzzwords = open("fuzzwords.txt").read().splitlines()

print(post_requests)

for req in post_requests:
    r = requests.post(req[0], data=req[1])
    for word in fuzzwords:
        # obfuscation
        # time.sleep(randint(1, 5))
        r = requests.post(req[0], data={"fuzzone": word, "fuzztwo": word})
        print(word, r.status_code, r.text, r.reason, r.request.url, r.request.body)


# TODO - fuzz every single field of payload
for req in post_requests:
    if is_json(req[1]):
        flat_payload = loop_dict(json.loads(req[1]))
        print(flat_payload)

nested_dict = {'dict1': {'key_A': 'value_A'},
                'dict2': {'key_B': 'value_B'}}

flat_dict = loop_dict(nested_dict)

print(nested_dict)
print(flat_dict)

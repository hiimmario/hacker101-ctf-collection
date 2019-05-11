import requests

# f

r = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/Common-PHP-Filenames.txt")
fuzzlist = r.text.splitlines()
fuzzlist_len = len(fuzzlist)
findings = []

for idx, word in enumerate(fuzzlist):
    try:
        r = requests.get("http://35.196.135.216/31f22243f1/" + word[:-4])
        if (r.status_code != 404):
            print("### found something ###")
            findings.append([r.url, r.status_code])
        print("{}/{} GET {}\nstatus_code = {}\n".format(idx+1, fuzzlist_len, r.url, r.status_code))
    except Exception as e:
        print(e)

print("{} findings\n{}".format(str(len(findings)), findings))

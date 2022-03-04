import requests
import json

_banner_ = '''
---------------------------------------------- 
💖💖💖💖💖💖💖💖
💖💖💖💖💖💖💖💖
💖💖💖💖💖💖💖💖
💖💖💖💖💖💖💖💖
---------------------------------------------- 
Github : Github.com/HANNAN0098
Fb : Abdul Hannan Ansari
Note : Use Fresh/New 🙄 Account
'''
user=raw_input('\x1b[1;95m USER/NUM/EMAIL : ')
passw=raw_input('x1b[1;93m PASSWORD : ')
get = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+user+'&locale=en_US&password='+passw+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

up = get.content
pu = json.loads(up)
if "session_key" in up:
    print
    os.system('clear')
    print (_banner_)
    print ('YOUR USERNAME :' + pu['identifier'])
    print ('YOUR ACCESS TOKEN:' + pu["access_token"])
    open(user+'-token.txt', 'a').write(pu["access_token"])
    print
    print ('File saved💖 = '+user+'-token.txt')
else:
    print ('🙂💖🙄ENTER CORRECT PASS/USER')

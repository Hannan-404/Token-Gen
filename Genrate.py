import requests
import json

_banner_ = '''
   +=+=+=+=+=+=+=+=+=+=+=+=+=+=+
  +++=== GET TOKEN FACEBOOK ===+++   
 ++== Cloning Is Not A Crime ==++
+= Its Just War Against The System =+
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

#OWNER : HANNAN ANSARI
#FACEBOOK : Abdul Hannan Ansari
'''
user=raw_input('\033[1;95mUSER/NUM/EMAIL : ')
passw=raw_input('\033[1;93m PASSWORD: ')
get = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+user+'&locale=en_US&password='+passw+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

up = get.content
pu = json.loads(up)
if "session_key" in up:
    print
    print _banner_
    print '\033[1;94mUsername:' + pu['identifier']
    print '\033[1;92mToken:' + pu["access_token"]
    open(user+'-token.txt', 'a').write(pu["access_token"])
    print
    print 'saved file to '+user+'-token.txt'
else:
    print '[ ! ] Incorrect Pass/User[ ! ]  '

import requests,json
import uuid
import os
from time import sleep
from datetime import datetime
from datetime import date
import os, sys, requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
now=datetime.now()
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
lam = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
import os,sys
import pywifi
from requests import session
from colorama import Fore, Style
import requests, random, re
from random import randint
import requests,pystyle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from datetime import date
from datetime import datetime
from time import sleep
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Kiểm tra kết nối internet
if check_internet_connection():
    print(f"{luc}Vui Lòng Chờ!!!")
    sleep(0.1)
else:
    print(f"{do}Vui Lòng Kiểm Tra Kết NốI!!!")
    sys.exit()
def get_location_by_ip():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()

        city = data.get("city")
        region = data.get("region")
        country = data.get("country")
        loc = data.get("loc").split(",")
        latitude, longitude = loc if len(loc) == 2 else (None, None)

        return city, region, country, latitude, longitude
    except Exception as e:
        print(f"Lỗi: {e}")
        return None, None, None, None, None
city, region, country, latitude, longitude = get_location_by_ip()
def get_weather():
    try:
        # Lấy thông tin vị trí từ dịch vụ ipinfo.io
        response = requests.get("https://ipinfo.io")
        data = response.json()
        location = data.get("loc").split(",")
        latitude, longitude = location
        # Lấy thông tin thời tiết từ trang web công cộng
        base_url = f"https://wttr.in/{latitude},{longitude}?format=%t"
        response = requests.get(base_url)
        weather_description = response.text.strip()
        return weather_description
    except Exception as e:
        print(f"Lỗi: {e}")
        return None
weather_description = get_weather()
os.system('cls' if os.name == 'nt' else 'clear')
sleep(0)
banner=f"""
\033[1;33m ██████╗ ███████╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     
\033[1;35m██╔═══██╗██╔════╝██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
\033[1;36m██║   ██║█████╗  █████╗         ██║   ██║   ██║██║   ██║██║     
\033[1;37m██║   ██║██╔══╝  ██╔══╝         ██║   ██║   ██║██║   ██║██║     
\033[1;32m╚██████╔╝██║     ██║            ██║   ╚██████╔╝╚██████╔╝███████╗
\033[1;31m ╚═════╝ ╚═╝     ╚═╝            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝\n
\033[1;97mTool By: \033[1;32mOFF TOOL            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tool\033[1;31m     : \033[1;97m☞ \033[1;31mTTC - Pro5v1\033[1;33m♔ \033[1;97m🔫
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/m@nekosharetool
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32m https://t.me/+Fz2j0ObF2hNiNGJl🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════
"""
for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00)
listuid = []
listcookie = []
class ApiPro5:
    def __init__(self, cookies,fb_dtsg,jazoet,id_page) -> None:
        self.headers = {
                'authority': 'www.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'vi',
                'cookie': cookies,
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'viewport-width': '1366',
            }
        url_profile = requests.get('https://www.facebook.com/me', headers=self.headers).url
        profile = requests.get(url_profile, headers=self.headers).text
        self.fb_dtsg = fb_dtsg
        self.jazoet = jazoet
        self.user_id = id_page
    def join(self, group_id):
        data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoet,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
            'variables': '{"feedType":"DISCUSSION","groupID":"'+group_id+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUPS_ENGAGE_TAB","attribution_id_v2":"GroupsCometCrossGroupFeedRoot.react,comet.groups.feed,tap_tabbar,1667116100089,433821,2361831622,","group_id":"'+group_id+'","group_share_tracking_params":null,"actor_id":"'+self.user_id+'","client_mutation_id":"2"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":false,"scale":1,"source":"GROUPS_ENGAGE_TAB","renderLocation":"group_mall","__relay_internal__pv__GlobalPanelEnabledrelayprovider":false,"__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true}',
            'server_timestamps': 'true',
            'doc_id': '5915153095183264',
        }

        response = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
        return response
    def reaction(self, id_post, reaction):
        try:
            url = requests.get('https://www.facebook.com/'+id_post, headers=self.headers).url
            home = requests.get(url, headers=self.headers).text
            feedback_id = home.split('{"__typename":"CommentComposerLiveTypingBroadcastPlugin","feedback_id":"')[1].split('","')[0]
            data = {
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoet,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
                'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1667106623951,429237,190055527696468,","feedback_id":"'+feedback_id+'","feedback_reaction_id":"'+reaction+'","feedback_source":"PROFILE","is_tracking_encrypted":true,"tracking":["AZXg8_yM_zhwrTY7oSTw1K93G-sycXrSreRnRk66aBJ9mWkbSuyIgNqL0zHEY_XgxepV1XWYkuv2C5PuM14WXUB9NGsSO8pPe8qDZbqCw5FLQlsGTnh5w9IyC_JmDiRKOVh4gWEJKaTdTOYlGT7k5vUcSrvUk7lJ-DXs3YZsw994NV2tRrv_zq1SuYfVKqDboaAFSD0a9FKPiFbJLSfhJbi6ti2CaCYLBWc_UgRsK1iRcLTZQhV3QLYfYOLxcKw4s2b1GeSr-JWpxu1acVX_G8d_lGbvkYimd3_kdh1waZzVW333356_JAEiUMU_nmg7gd7RxDv72EkiAxPM6BA-ClqDcJ_krJ_Cg-qdhGiPa_oFTkGMzSh8VnMaeMPmLh6lULnJwvpJL_4E3PBTHk3tIcMXbSPo05m4q_Xn9ijOuB5-KB5_9ftPLc3RS3C24_7Z2bg4DfhaM4fHYC1sg3oFFsRfPVf-0k27EDJM0HZ5tszMHQ"],"session_id":"'+str(uuid.uuid4())+'","actor_id":"'+self.user_id+'","client_mutation_id":"1"},"useDefaultActor":false,"scale":1}',
                'server_timestamps': 'true',
                'doc_id': '5703418209680126',
            }

            reaction = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
            return {'status': True, 'url': url}
        except:
            return {'status': False, 'url': url}
    def subscribe(self, uid):
        data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoet,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometUserFollowMutation',
            'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1667114418950,431532,190055527696468,","subscribe_location":"PROFILE","subscribee_id":"'+uid+'","actor_id":"'+self.user_id+'","client_mutation_id":"1"},"scale":1}',
            'server_timestamps': 'true',
            'doc_id': '5032256523527306',
        }
        subscribe = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
        return subscribe

    
def get_page(cookie):
    headers = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
        'cache-control': 'max-age=0',
        'cookie': cookie,
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    response = requests.get('https://mbasic.facebook.com/',headers=headers).text
    fb_dtsg = response.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = response.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
    idpef = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data={'fb_dtsg': fb_dtsg,'jazoest': jazoest,'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}','doc_id': '5300338636681652'}).json()
    a = idpef['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
    sl = 0
    for b in a:
        sl +=1
        uid = b['profile']['id']
        name = b['profile']['name']
        delegate_page_id = b['profile']['delegate_page_id']
        print (f"\033[1;37mPAGE : {sl} | ID : {uid} | Name : {name} ")
        print ('\033[1;36m────────────────────────────────────────────────────────────')
    return a
    
def cauhinh(id, cookie,name):
	url = 'https://tuongtaccheo.com/cauhinh/datnick.php'
	data = f'iddat%5B%5D={id}&loai=fb'
	head ={
	'Host':'tuongtaccheo.com',
	'accept':'*/*',
	'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; CPH1912 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36',
	'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
	'cookie':f'{cookie}'
	}
	ve = requests.post(url= url, headers= head , data= data).text
	if ve == '1' :
		print (f' \033[1;32mCấu Hình \033[1;37m| \033[1;32mID : \033[1;33m{id} \033[1;37m | \033[1;32mName : \033[1;33m{name}')
	else :
		print (f' \033[1;31mBạn Chưa Thêm {id} Vào Cấu Hình ')
		exit()
def get_job(loai,cookie):
	head = {
	'Host':'tuongtaccheo.com',
	'accept':'application/json, text/javascript, */*; q=0.01',
	'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; CPH1912 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36',
	'cookie':f'{cookie}',
	'x-requested-with':'XMLHttpRequest'
	}
	get_nv = requests.get(f'https://tuongtaccheo.com/kiemtien{loai}getpost.php',headers=head)
	return get_nv

def nhanxu(cookie,loai,data) :
	url = f'https://tuongtaccheo.com/kiemtien{loai}nhantien.php'
	
	head = {
	'Host':'tuongtaccheo.com',
	'accept':'*/*',
	'x-requested-with':'XMLHttpRequest',
	'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; CPH1912 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36',
	'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
	'referer':f'https://tuongtaccheo.com/kiemtien{loai}',
	'cookie':f'{cookie}'
	}
	
	nhan = requests.post(url= url, headers= head , data= data)
	return nhan
	
def get_cookie_ttc(token) :
	data = {
	'access_token': token
	}
	text_1 = requests.post("https://tuongtaccheo.com/logintoken.php", data= data)
	log = text_1.json()["status"]
	if log == "success" :
		xu = text_1.json()["data"]["sodu"]
		name = text_1.json()["data"]["user"]
		cookie = text_1.headers["Set-Cookie"]
		
	else :
		print (' \033[1;31m Đăng Nhập Thất Bại ')
		exit()
	return cookie
	
def get_data(cookie):
    headers = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': cookie,
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    response = requests.get('https://mbasic.facebook.com/',headers=headers).text
    fb_dtsg = response.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoet = response.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
    return json.dumps({'fb_dtsg':fb_dtsg,'jazoet':jazoet})

def xu_tt(cookie) :
	head = {
	'Host':'tuongtaccheo.com',
	'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; CPH1912 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36',
	'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
	'cookie':cookie
	}
	response = requests.get('https://tuongtaccheo.com/home.php',headers=head).text
	xu = response.split('<li><a>Số dư: <strong style="color: red;" id="soduchinh">')[1].split('<')[0]
	return xu
	
print('\033[1;34m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦')
def chon_job(so,ttt) :
	if ttt == 3 :
		ttt -= 3
	
	if so == 1 :
		loai = "/subcheo/"
	elif so == 2 :
		loai = "/camxuccheo/"
	elif so == 3 :
		loai = "/thamgianhomcheo/"
	else :
		type_5 = ['/subcheo/','/camxuccheo/','/thamgianhomcheo/']
		loai = type_5[ttt]
	return loai


def type_cx(type_1) :
	if type_1 == "LOVE" :
		type_2 = '1678524932434102'
	elif type_1 == "CARE" :
		type_2 = '613557422527858'
	elif type_1 == "WOW" :
		type_2 = '478547315650144'
	elif type_1 == "HAHA" :
		type_2 = '115940658764963'
	elif type_1 == "SAD" :
		type_2 = '908563459236466'
	elif type_1 == "ANGRY" :
		type_2 = '444813342392137'
	return type_2
token = input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;37mNhập Access_token TTC : \033[1;33m ')
cookie_ttc = get_cookie_ttc(token) 
print('\033[1;34m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦')

cookie = input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;37mNhập Cookie Facebook : \033[1;33m')
print('\033[1;34m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦')
#### vào việc
get_tt_page = get_page(cookie)
a = int(input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;37mBạn Muốn Chạy Page Thứ Mấy : \033[1;33m'))
chon = a-1
dl = int(input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;37mNhập Delay : \033[1;33m '))

id_page = get_tt_page[chon]['profile']['id']
name = get_tt_page[chon]['profile']['name']
ck_pro5 = 'sb={}; datr={}; c_user={}; wd={}; xs={}; fr={}; i_user={};'.format(cookie.split('sb=')[1].split(';')[0], cookie.split('datr=')[1].split(';')[0], cookie.split('c_user=')[1].split(';')[0],cookie.split('wd=')[1].split(';')[0], cookie.split('xs=')[1].split(';')[0],cookie.split('fr=')[1].split(';')[0],id_page)
##chọn job
print('\033[1;34m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦')
print ("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;36mNhập 1 Job Follow")
print ("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;36mNhập 2 Job Cảm Xúc")
print ("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;36mNhập 3 Job Group")
print ("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;36mNhập 4 Job Follow + Cảm Xúc + Group ")
so = int(input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;37mChọn Job : \033[1;33m '))
print('\033[1;34m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦')
os.system("clear")
get_cookie_ttc(token) 
print('\033[1;34m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦')
cauhinh(id_page, cookie_ttc, name)
print('\033[1;34m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦')
tt = 0
data = get_data(cookie)
fb_dtsg = json.loads(data)['fb_dtsg']
jazoet = json.loads(data)['jazoet']
fb = ApiPro5(cookies=ck_pro5, fb_dtsg=fb_dtsg, jazoet=jazoet,id_page=id_page)
ttt = 0
while True :
	loai = chon_job(so,ttt) 
	ttt+= 1
	print(" Đang Tìm Job ",end="\r")
	if loai == "/subcheo/" :
		list_job = get_job(loai,cookie_ttc)
		b = list_job.text
		a = list_job.json()
		if b == "[]" :
			print(" Hết Job Follow",end="\r")
		else :
			for list_job_ in a :
				id_job = list_job_["idpost"]
				
				fb.subscribe(id_job)
				data = f'id={id_job}'
				nhan = nhanxu(cookie_ttc,loai,data).json()
				xu_1 = xu_tt(cookie_ttc) 
				try :
					a = nhan["error"]
					print (f" ERROR=> {id_job} ",end="\r")
				except :
					gio = datetime.now().strftime("%H:%M:%S")
					tt += 1
					print (f'\033[1;37m| {tt} | {gio} | Follow | {id_job} | +600 | {xu_1} Xu ' )
					for i in range(dl,-1,-1):
						print(f'[{i}] [DELAY]',end='\r')
						sleep(1)
			
	elif loai == "/thamgianhomcheo/" :
		list_job = get_job(loai,cookie_ttc)
		b = list_job.text
		a = list_job.json()
		if b == "[]" :
			print(" Hết Job Cảm Xúc ",end="\r")
		else :
			for list_job_ in a :
				id_job = list_job_["idpost"]
				lam = fb.join(id_job)
				data = f"id={id_job}"
				nhan = nhanxu(cookie_ttc,loai,data)
				nhan_2 = nhan.json()
				xu_1 = xu_tt(cookie_ttc) 
				
				try :
					a = nhan_2["error"]
					print (f'{id_job} => | GROUP | ERRO ',end="\r")
				except :
					tt += 1
					gio = datetime.now().strftime("%H:%M:%S")
					print (f'\033[1;37m| {tt} | {gio} | GROUP | {id_job} | +1200 | {xu_1} Xu ' )
					for i in range(dl,-1,-1):
						print(f'[{i}] [DELAY]',end='\r')
						sleep(1)
	elif loai == "/camxuccheo/" :
		list_job = get_job(loai,cookie_ttc)
		b = list_job.text
		a = list_job.json()
		if b == "[]" :
			print(" Hết Job Cảm Xúc ",end="\r")
		else :
			for list_job_ in a :
				id_job = list_job_["idpost"]
				
				type_1 = list_job_["loaicx"]
				type_2 = type_cx(type_1) 
				lam = fb.reaction(id_job, type_2)
				data = f"id={id_job}&loaicx={type_1}"
				nhan = nhanxu(cookie_ttc,loai,data)
				nhan_2 = nhan.json()
				xu_1 = xu_tt(cookie_ttc) 
				
				try :
					a = nhan_2["error"]
					print (f'{id_job} => {type_1} | ERROR ',end="\r")
				except :
					tt += 1
					gio = datetime.now().strftime("%H:%M:%S")
					print (f'\033[1;37m| {tt} | {gio} | {type_1} | {id_job} | +400 | {xu_1} Xu ' )
					for i in range(dl,-1,-1):
						print(f'\033[1;37m[{i}] [DELAY]',end='\r')
						sleep(0)
			

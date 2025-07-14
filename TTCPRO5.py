
import requests, base64, uuid, os, json
from random import randint
from pystyle import Write, Colors
from datetime import datetime
from time import sleep
from colorama import Fore, init
from rich.console import Console
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from pystyle import Write, Colors, Colorate
import threading
def play_music():
    os.system("mpv on_top.mp3 --no-video ")

def tai_nhac():
    url = "https://github.com/Cacdume-wq/cac/blob/main/on_top.mp3"  # Link mp3
    if not os.path.exists("on_top.mp3"):
        print("🔊 Đang tải nhạc nền...")
        try:
            r = requests.get(url)
            with open("nhac.mp3", "wb") as f:
                f.write(r.content)
            print("✅ Đã tải xong nhạc.")
        except:
            print("❌ Không thể tải nhạc.")

tai_nhac()
bat_nhac = input("🎵 Bạn có muốn bật nhạc nền không? (y/n): ").strip().lower()
if bat_nhac == "y":
    threading.Thread(target=play_music, daemon=True).start()




os.system('cls' if os.name=='nt' else 'clear')
red    = "\033[38;5;196m"  # Đỏ chói
luc    = "\033[1;32m"   # Xanh lá neon
vang   = "\033[38;5;226m"  # Vàng tươi
cam    = "\033[38;5;208m"  # Cam sáng
tim    = "\033[38;5;201m"  # Tím sáng
lam    = "\033[38;5;51m"   # Xanh dương neon
trang  = "\033[38;5;15m"   # Trắng sáng
listck = []
listjob = []
thanh = f'{red}[{trang}</>{red}] {trang}=>'
do = "\033[1;31m"
xanh = "\033[1;36m"

from datetime import datetime
from colorama import Fore

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(Colorate.Diagonal(Colors.green_to_red, """
    
███╗   ██╗██████╗    ████████╗ ██████╗  ██████╗ ██╗     
████╗  ██║██╔══██╗   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██╔██╗ ██║██████╔╝█████╗██║   ██║   ██║██║   ██║██║     
██║╚██╗██║██╔═══╝ ╚════╝██║   ██║   ██║██║   ██║██║     
██║ ╚████║██║           ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝  ╚═══╝╚═╝           ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
╠═══════════════════════════════════════════════╣
║▶ Nhóm   : \033[38;5;20mhttps://zalo.me/g/vmugmo123              ║
║▶ Zalo : \033[38;5;1204m0394764859                        ║
║▶ Tool Do Tao Code 😆                     ║
║▶ May Anh Dung Bug Tool Em 😭              ║
║▶ Phiên Bản Tool : 1.0 ( VIP )                 ║
╚═══════════════════════════════════════════════╝                                                        

"""))
init(autoreset=True)
console = Console()
    
def getjob(cookie, nv):
    headers = {
        "Host":"tuongtaccheo.com",
        "accept":'application/json, text/javascript, *" . "/" . "*; q=0.01',
        "x-requested-with":"XMLHttpRequest",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
        "cookie": cookie
    }
    get = requests.get(f'https://tuongtaccheo.com/kiemtien/{nv}/getpost.php',headers=headers)
    return get

def decode_base64(encoded_str):
	decoded_bytes = base64.b64decode(encoded_str)
	decoded_str = decoded_bytes.decode('utf-8')
	return decoded_str

def _encode_to_base64(_data):
	byte_representation = _data.encode('utf-8')
	base64_bytes = base64.b64encode(byte_representation)
	base64_string = base64_bytes.decode('utf-8')
	return base64_string

def _delay(value):
	while not(value <= 1):
		value -= 0.123
		print(f'''\033[1;39m[\033[1;36mNP-TOOL\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}\033[1;39m][\033[1;33mX  \033[1;39m ]''', '               ', end = '\r')
		sleep(0.025)
		print(f'''\033[1;39m[\033[1;36mNP-TOOL\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}\033[1;39m][\033[1;33m X   \033[1;39m]''', '               ', end = '\r')
		sleep(0.025)
		print(f'''\033[1;39m[\033[1;36mNP-TOOL\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}[ \033[1;33m  X  \033[1;39m]''', '               ', end = '\r')
		sleep(0.025)
		print(f'''\033[1;39m[\033[1;36mNP-TOOL\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}\033[1;39m][\033[1;33m   X \033[1;39m]''', '               ', end = '\r')
		sleep(0.025)
		print(f'''\033[1;39m[\033[1;36mNP-TOOL\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}\033[1;39m][\033[1;33m    X\033[1;39m]''', '               ', end = '\r')
		sleep(0.025)
def countdown(value):
	while not(value <= 1) :
		value -= 0.123
		print(f'''\033[1;39m[\033[1;36mNP-TOOL\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}\033[1;39m][\033[1;33mX  \033[1;39m ]''', '               ', end = '\r')
		sleep(0.025)
		print(f'''\033[1;39m[\033[1;36mNP-TOOL\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}\033[1;39m][\033[1;33m X   \033[1;39m]''', '               ', end = '\r')
		sleep(0.025)
		print(f'''\033[1;39m[\033[1;36mNP-TOOL\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}[ \033[1;33m  X  \033[1;39m]''', '               ', end = '\r')
		sleep(0.025)
		print(f'''\033[1;39m[\033[1;36mNP-TOOL\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}\033[1;39m][\033[1;33m   X \033[1;39m]''', '               ', end = '\r')
		sleep(0.025)
		print(f'''\033[1;39m[\033[1;36mNP-TOOL\033[1;39m][ \033[1;36mDELAY \033[1;39m][\033[1;36m{str(value)[0:5]}\033[1;39m][\033[1;33m    X\033[1;39m]''', '               ', end = '\r')
		sleep(0.025)

def chongblock(delaybl):
	for i in range(delaybl, -1, -1):
		Write.Print(f'Đang ở chế độ chống block , sẽ chạy lại sau {i} giây  \r',Colors.rainbow,interval=0.0001);sleep(1); print('                                                        ', end = '\r')

def _Infofb(cookie):
    heads={
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7", 
        "content-type": "application/x-www-form-urlencoded", 
        "sec-ch-prefers-color-scheme": "light", 
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"", 
        "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"", 
        "sec-ch-ua-mobile": "?0", 
        "sec-ch-ua-model": "\"\"", 
        "sec-ch-ua-platform": "\"Linux\"", 
        "sec-ch-ua-platform-version": "\"\"", 
        "sec-fetch-dest": "empty", 
        "sec-fetch-mode": "cors", 
        "sec-fetch-site": "same-origin", 
        "x-asbd-id": "129477", 
        "x-fb-friendly-name": "ProfileCometTimelineListViewRootQuery", 
        "x-fb-lsd": "7_RkODA0fo-6ShZlbFpHEW"
    }
    get = requests.get("https://www.facebook.com/me", headers=heads, cookies={"cookie": cookie})
    try:
        get = get.url
        get = requests.get(get, headers=heads, cookies={"cookie": cookie}).text
        _sea = get.split(',"NAME":"')[1].split('",')[0]
        _name = bytes(_sea, "utf-8").decode("unicode_escape")
        _fb1 = get.split('["DTSGInitialData",[],{"token":"')[1].split('"')[0]
        _idfb = cookie.split('c_user=')[1].split(';')[0]
        return [_fb1, _idfb, _name]
    except:
        return False
    
def _Like(cookie, uid, type, fb1, idfb):
    headers = {
        "accept": "*/*", 
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7", 
        "content-type": "application/x-www-form-urlencoded", 
        "sec-ch-prefers-color-scheme": "light", 
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"", 
        "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"", 
        "sec-ch-ua-mobile": "?0", 
        "sec-ch-ua-model": "\"\"", 
        "sec-ch-ua-platform": "\"Linux\"", 
        "sec-ch-ua-platform-version": "\"\"", 
        "sec-fetch-dest": "empty", 
        "sec-fetch-mode": "cors", 
        "sec-fetch-site": "same-origin", 
        "x-asbd-id": "129477", 
        "x-fb-friendly-name": "CometUFIFeedbackReactMutation", 
        "x-fb-lsd": "7_RkODA0fo-6ShZlbFpHEW"
    }
    _reac = {
        "LIKE": "1635855486666999",
        "LOVE": "1678524932434102",
        "CARE": "613557422527858",
        "HAHA": "115940658764963",
        "WOW": "478547315650144",
        "SAD": "908563459236466",
        "ANGRY": "444813342392137"
    }
    _id_reac = _reac.get(type)
    _data = {
        'av': idfb,
        '__usid': r'6-Tsfgotwhb2nus:Psfgosvgerpwk:0-Asfgotw11gc1if-RV=6:F=',
        '__aaid': '0',
        '__user': idfb,
        '__a': '1',
        '__req': '2c',
        '__hs': '19896.HYP:comet_pkg.2.1..2.1',
        'dpr': '1',
        '__ccg': 'EXCELLENT',
        '__rev': '1014402108',
        '__s': '5vdtpn:wbz2hc:8r67q5',
        '__hsi': '7383159623287270781',
        '__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C17xt3odE98K361twYwJyE24wJwpUe8hwaG1sw9u0LVEtwMw65xO2OU7m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewyDwkUe9obrwKxm5oe8464-5pUfEdK261eBx_wHwdG7FoarCwLyES0Io88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13whEeE4WVU-4EdrxG1fy8bUaU','__csr': 'gug_2A4A8gkqTf2Ih6RFnbk9mBqaBaTs8_tntineDdSyWqiGRYCiPi_SJuLCGcHBaiQXtLpXsyjIymm8oFJswG8CSGGLzAq8AiWZ6VGDgyQiiTBKU-8GczE9USmi4A9DBABHgWEK3K9y9prxaEa9KqQV8qUlxW22u4EnznDxSewLxq3W2K16BxiE5VqwbW1dz8qwCwjoeEvwaKVU6q0yo5a2i58aE7W0CE5O0fdw1jim0dNw7ewPBG0688025ew0bki0cow3c8C05Vo0aNF40BU0rmU3LDwaO06hU06RG6U1g82Bw0Gxw6Gw',
        '__comet_req': '15',
        'fb_dtsg': fb1,
        'jazoest': '25509',
        'lsd': '2JgeTE-rDuLtIVUViHpGjH',
        '__spin_r': '1014402108',
        '__spin_b': 'trunk',
        '__spin_t': '1719025807',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
        'variables': fr'{{"input":{{"attribution_id_v2":"CometHomeRoot.react,comet.home,tap_tabbar,1719027162723,322693,4748854339,,","feedback_id":"{_encode_to_base64("feedback:"+str(uid))}","feedback_reaction_id":"{_id_reac}","feedback_source":"NEWS_FEED","is_tracking_encrypted":true,"tracking":["AZWUDdylhKB7Q-Esd2HQq9i7j4CmKRfjJP03XBxVNfpztKO0WSnXmh5gtIcplhFxZdk33kQBTHSXLNH-zJaEXFlMxQOu_JG98LVXCvCqk1XLyQqGKuL_dCYK7qSwJmt89TDw1KPpL-BPxB9qLIil1D_4Thuoa4XMgovMVLAXncnXCsoQvAnchMg6ksQOIEX3CqRCqIIKd47O7F7PYR1TkMNbeeSccW83SEUmtuyO5Jc_wiY0ZrrPejfiJeLgtk3snxyTd-JXW1nvjBRjfbLySxmh69u-N_cuDwvqp7A1QwK5pgV49vJlHP63g4do1q6D6kQmTWtBY7iA-beU44knFS7aCLNiq1aGN9Hhg0QTIYJ9rXXEeHbUuAPSK419ieoaj4rb_4lA-Wdaz3oWiWwH0EIzGs0Zj3srHRqfR94oe4PbJ6gz5f64k0kQ2QRWReCO5kpQeiAd1f25oP9yiH_MbpTcfxMr-z83luvUWMF6K0-A-NXEuF5AiCLkWDapNyRwpuGMs8FIdUJmPXF9TGe3wslF5sZRVTKAWRdFMVAsUn-lFT8tVAZVvd4UtScTnmxc1YOArpHD-_Lzt7NDdbuPQWQohqkGVlQVLMoJNZnF_oRLL8je6-ra17lJ8inQPICnw7GP-ne_3A03eT4zA6YsxCC3eIhQK-xyodjfm1j0cMvydXhB89fjTcuz0Uoy0oPyfstl7Sm-AUoGugNch3Mz2jQAXo0E_FX4mbkMYX2WUBW2XSNxssYZYaRXC4FUIrQoVhAJbxU6lomRQIPY8aCS0Ge9iUk8nHq4YZzJgmB7VnFRUd8Oe1sSSiIUWpMNVBONuCIT9Wjipt1lxWEs4KjlHk-SRaEZc_eX4mLwS0RcycI8eXg6kzw2WOlPvGDWalTaMryy6QdJLjoqwidHO21JSbAWPqrBzQAEcoSau_UHC6soSO9UgcBQqdAKBfJbdMhBkmxSwVoxJR_puqsTfuCT6Aa_gFixolGrbgxx5h2-XAARx4SbGplK5kWMw27FpMvgpctU248HpEQ7zGJRTJylE84EWcVHMlVm0pGZb8tlrZSQQme6zxPWbzoQv3xY8CsH4UDu1gBhmWe_wL6KwZJxj3wRrlle54cqhzStoGL5JQwMGaxdwITRusdKgmwwEQJxxH63GvPwqL9oRMvIaHyGfKegOVyG2HMyxmiQmtb5EtaFd6n3JjMCBF74Kcn33TJhQ1yjHoltdO_tKqnj0nPVgRGfN-kdJA7G6HZFvz6j82WfKmzi1lgpUcoZ5T8Fwpx-yyBHV0J4sGF0qR4uBYNcTGkFtbD0tZnUxfy_POfmf8E3phVJrS__XIvnlB5c6yvyGGdYvafQkszlRrTAzDu9pH6TZo1K3Jc1a-wfPWZJ3uBJ_cku-YeTj8piEmR-cMeyWTJR7InVB2IFZx2AoyElAFbMuPVZVp64RgC3ugiyC1nY7HycH2T3POGARB6wP4RFXybScGN4OGwM8e3W2p-Za1BTR09lHRlzeukops0DSBUkhr9GrgMZaw7eAsztGlIXZ_4"],"session_id":"{uuid.uuid4()}","actor_id":"{idfb}","client_mutation_id":"3"}},"useDefaultActor":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false}}',
        'server_timestamps': 'true',
        'doc_id': '7047198228715224',
    }
    cookies = {
        "cookie": cookie
    }
    _get = requests.post("https://www.facebook.com/api/graphql/",headers=headers, cookies=cookies, params=_data)
    if '{"data":{"feedback_react":{"feedback":{"id":' in _get.text:
        return True
    else:
        return False
    
def _React_Cmt(cookie, idfb, fb1, uid, type):
    _reac = {
        "LIKE": "1635855486666999",
        "LOVE": "1678524932434102",
        "CARE": "613557422527858",
        "HAHA": "115940658764963",
        "WOW": "478547315650144",
        "SAD": "908563459236466",
        "ANGRY": "444813342392137"
    }
    g_now = datetime.now()
    d = g_now.strftime("%Y-%m-%d %H:%M:%S.%f")
    datetime_object = datetime.strptime(d, "%Y-%m-%d %H:%M:%S.%f")
    timestamp = str(datetime_object.timestamp())
    _d  = timestamp.replace('.', '')
    _id_reac = _reac.get(type)
    _headers = {
        "accept": "*/*", 
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7", 
        "content-type": "application/x-www-form-urlencoded", 
        "sec-ch-prefers-color-scheme": "light", 
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"", 
        "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"", 
        "sec-ch-ua-mobile": "?0", 
        "sec-ch-ua-model": "\"\"", 
        "sec-ch-ua-platform": "\"Linux\"", 
        "sec-ch-ua-platform-version": "\"\"", 
        "sec-fetch-dest": "empty", 
        "sec-fetch-mode": "cors", 
        "sec-fetch-site": "same-origin", 
        "x-asbd-id": "129477", 
        "x-fb-friendly-name": "CometUFIFeedbackReactMutation", 
        "x-fb-lsd": "5dCcoMgOrU5CgUwl77gn-C"
    }
    _data = {
        'av': idfb, 
        '__aaid': '0', 
        '__user': idfb, 
        '__a': '1', 
        '__req': '1a', 
        '__hs': '19906.HYP:comet_pkg.2.1..2.1', 
        'dpr': '1', 
        '__ccg': 'GOOD', 
        '__rev': '1014619389', 
        '__s': 'z5ciff:vre7af:23swxc', 
        '__hsi': '7387045920424178191', 
        '__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C1vgS3q2ibwyzE2qwJyE24wJwkEkwUx60GE5O0BU2_CxS320om78-221Rwwwqo462mcwfG12wOx62G5Usw9m1YwBgK7o6C2O0B84G1hx-3m1mzXw8W58jwGzEaE5e3ym2SUbElxm3y11xfxmu3W3rwxwjFovUaU3VBwFKq2-azo2NwwwOg2cwMwhEkxebwHwNxe6Uak0zU8oC1hxB0qo4e16wWwjHDzUiwRK6E4-8wLwHw', 
        '__csr': 'gJ0AH5n4n4PhcQW4Oh4JFsIH4f5ji9iWuzqSltFlETn_trnbH_YIJX9iWiAiQBpeht9uYyhrvOOaiSV9CKmriyF4EzjBGh4XRqy8O4Z4HGypAaDAG8DzE-iKii5bUGaiXyocA22iayUOUG9BKUkxe2vBBxe5898S5k48fogxqQU9oO1bwiU9FpEowOBwYwLCw86u2y0Eo885-1uwFwOwpU1jo7-0IU108iw8i0kq0bVw6gBxa4E1g83tw0_yBw2hE012EoG0uG0gh068w23Q0dlw0wKw68Aw0huU0a7VU0jkw0E-w8W0cPK6U', 
        '__comet_req': '15', 
        'fb_dtsg': fb1, 
        'jazoest': '25446', 
        'lsd': '5dCcoMgOrU5CgUwl77gn-C', 
        '__spin_r': '1014619389', 
        '__spin_b': 'trunk', 
        '__spin_t': '1719930656', 
        'fb_api_caller_class': 'RelayModern', 
        'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation', 
        'variables': '{"input":{"attribution_id_v2":"CometVideoHomeNewPermalinkRoot.react,comet.watch.injection,via_cold_start,1719930662698,975645,2392950137,,","feedback_id":"'+_encode_to_base64("feedback:"+str(uid))+'","feedback_reaction_id":"'+_id_reac+'","feedback_source":"TAHOE","is_tracking_encrypted":true,"tracking":[],"session_id":"'+str(uuid.uuid4())+'","downstream_share_session_id":"'+str(uuid.uuid4())+'","downstream_share_session_origin_uri":"https://fb.watch/t3OatrTuqv/?mibextid=Nif5oz","downstream_share_session_start_time":"'+_d+'","actor_id":"'+idfb+'","client_mutation_id":"1"},"useDefaultActor":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false}', 
        'server_timestamps': 'true', 
        'doc_id': '7616998081714004',
    }
    cookies = {
        "cookie": cookie
    }
    _post = requests.post("https://www.facebook.com/api/graphql/",headers=_headers, cookies=cookies, params=_data)
    if '{"data":{"feedback_react":{"feedback":' in _post.text:
        return True
    else:
        return False
    
def _Follow(cookie, idfb, fb1, uid):
    headers = {
        "accept": "*/*", 
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7", 
        "content-type": "application/x-www-form-urlencoded", 
        "sec-ch-prefers-color-scheme": "light", 
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"", 
        "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"", 
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-model": "\"\"", 
        "sec-ch-ua-platform": "\"Linux\"", 
        "sec-ch-ua-platform-version": "\"\"", 
        "sec-fetch-dest": "empty", 
        "sec-fetch-mode": "cors", 
        "sec-fetch-site": "same-origin", 
        "x-asbd-id": "129477", 
        "x-fb-friendly-name": "CometUserFollowMutation", 
        "x-fb-lsd": "7_RkODA0fo-6ShZlbFpHEW"
    }
    _data = {
        'av': idfb,
        '__aaid': '0',
        '__user': idfb,
        '__a': '1',
        '__req': '3c',
        '__hs': '19904.HYP:comet_pkg.2.1..2.1',
        'dpr': '1',
        '__ccg': 'GOOD',
        '__rev': '1014584891',
        '__s': 'my2e5i:sn3f24:bhs2dd',
        '__hsi': '7386333891453876768',
        '__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C1vgS3q2ibwNw9G2Saw8i2S1DwUx60GE5O0BU2_CxS320om78c87m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewGwkUe9obrwKxm5oe8464-5pUfEe88o4Wm7-2K0-poarCwLyES0Io88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13whEeE4WVU-4EdrxG1fy8bUaU',
        '__csr': 'g652tR6igD6PnsllELEhOn2WthkQARshlfPvfvlRiNePOWPLRFtv8QmQV94jqQ-VfrnZmih4z9Fp8CjBgxrDL-h5ATQaKiiaBBzqytoxartorHiyAES4oly47FUCu5lDzqwFCBxa4EyiQbjJe8Uy78b8izK26m5USu9yUhwAw-xG9wpFp8G4ojwMwr8jxW10wMwYwgEO1iz85i321ZwKwVwrUuBw4Ey8owt8S12wdq0nC0drw8-3C0VUoyUK3G1Hm0oS01ZBw2Lo034MwEw8l01sZ09a1Bw1hq05SU1c8W01aSw0XMg09CU14o3tw2iob80u5w',
        '__comet_req': '15',
        'fb_dtsg': fb1,
        'jazoest': '25183',
        'lsd': 'HaknqmvLIYQBrJ871R18Fg',
        '__spin_r': '1014584891',
        '__spin_b': 'trunk',
        '__spin_t': '1719764873',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'CometUserFollowMutation',
        'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,unexpected,1719765181042,489343,250100865708545,,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,unexpected,1719765155735,648442,391724414624676,,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,tap_search_bar,1719765153341,865155,391724414624676,,","is_tracking_encrypted":false,"subscribe_location":"PROFILE","subscribee_id":"'+str(uid)+'","tracking":null,"actor_id":"'+str(idfb)+'","client_mutation_id":"5"},"scale":1}',
        'server_timestamps': 'true',
        'doc_id': '25581663504782089',
    }
    cookies = {
        "cookie": cookie
    }
    _Post = requests.post("https://www.facebook.com/api/graphql/", headers=headers, cookies=cookies, params=_data)
    if '"subscribe_status":"IS_SUBSCRIBED"' in _Post.text:
        return True
    else:
        return False
    
def CMT(cookie, id, idfb, fb1, msg:str):
    headers = {
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/x-www-form-urlencoded", 
        "sec-ch-prefers-color-scheme": "light", 
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"", 
        "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"", 
        "sec-ch-ua-mobile": "?0", 
        "sec-ch-ua-model": "\"\"", 
        "sec-ch-ua-platform": "\"Linux\"", 
        "sec-ch-ua-platform-version": "\"\"", 
        "sec-fetch-dest": "empty", 
        "sec-fetch-mode": "cors", 
        "sec-fetch-site": "same-origin", 
        "x-asbd-id": "129477", 
        "x-fb-friendly-name": "CometUFIFeedbackReactMutation", 
        "x-fb-lsd": "7_RkODA0fo-6ShZlbFpHEW"
    }
    _data = {
        'av': idfb,
        '__aaid': '0',
        '__user': idfb,
        '__a': '1',
        '__req': '3a',
        '__hs': '19892.HYP:comet_pkg.2.1..2.1',
        'dpr': '1',
        '__ccg': 'GOOD',
        '__rev': '1014295603',
        '__s': 'xrpwhz:69a31q:w9xo5s',
        '__hsi': '7381711750373683802',
        '__dyn': '7AzHK4HwkEng5K8G6EjBAg2owIxu13wFwhUngS3q2ibwNw9G2Saw8i2S1DwUx60GE5O0BU2_CxS320om78c87m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwwwi831wiE567Udo5qfK0zEkxe2GewDG1jwUBwJK2W5olwUwgojUlDw-wUwxwjFovUaU3VBwFKq2-azo2NwwwOg2cwMwhEkxebwHwNxe6Uak0zU8oC1hxB0qo4e16wWwjHDzUiwRK6E4-8wLwHw','__csr': 'gaRMHkaEj4EQgznFON5ifOjsLJA9idO8LqsAHJXeIX48l9lRN4kDmyTAvcKSIAGQtljy9kV4DlGaBAnWUCiqqWmWKA6pBBUymnHBArrCDDKaGaggAQubV8V34iVUCiicoC32Ujm8Ki8H-6UJ1h2KlAyECdg4237CxmQ6F89onXAwjEe8uwxxu5ES2G1qxy3K0xonx21ewnEb8eU2yG2q0hm1yw8G7o7G7oaodU1381T84m0auwdy0dDwb201Z4w2Fo036dg0gYCw2BA0wU7e04WU0qQwlodE04Dq01zOw4Bw51w7hxK',
        '__comet_req': '15',
        'fb_dtsg': fb1,
        'jazoest': '25686',
        'lsd': 'H5eT-P3p1zI2ywmbuNcbRm',
        '__spin_r': '1014295603',
        '__spin_b': 'trunk',
        '__spin_t': '1718688698',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'useCometUFICreateCommentMutation',
        'variables': fr'{{"feedLocation":"DEDICATED_COMMENTING_SURFACE","feedbackSource":110,"groupID":null,"input":{{"client_mutation_id":"4","actor_id":"{idfb}","attachments":null,"feedback_id":"{_encode_to_base64(f"feedback:{id}")}","formatting_style":null,"message":{{"ranges":[],"text":"{msg}"}},"attribution_id_v2":"CometHomeRoot.react,comet.home,via_cold_start,1718688700413,194880,4748854339,,","vod_video_timestamp":null,"feedback_referrer":"/","is_tracking_encrypted":true,"tracking":["AZX1ZR3ETYfGknoE2E83CrSh9sg_1G8pbUK70jA-zjEIcfgLxA-C9xuQsGJ1l2Annds9fRCrLlpGUn0MG7aEbkcJS2ci6DaBTSLMtA78T9zR5Ys8RFc5kMcx42G_ikh8Fn-HLo3Qd-HI9oqVmVaqVzSasZBTgBDojRh-0Xs_FulJRLcrI_TQcp1nSSKzSdTqJjMN8GXcT8h0gTnYnUcDs7bsMAGbyuDJdelgAlQw33iNoeyqlsnBq7hDb7Xev6cASboFzU63nUxSs2gPkibXc5a9kXmjqZQuyqDYLfjG9eMcjwPo6U9i9LhNKoZwlyuQA7-8ej9sRmbiXBfLYXtoHp6IqQktunSF92SdR53K-3wQJ7PoBGLThsd_qqTlCYnRWEoVJeYZ9fyznzz4mT6uD2Mbyc8Vp_v_jbbPWk0liI0EIm3dZSk4g3ik_SVzKuOE3dS64yJegVOQXlX7dKMDDJc7P5Be6abulUVqLoSZ-cUCcb7UKGRa5MAvF65gz-XTkwXW5XuhaqwK5ILPhzwKwcj3h-Ndyc0URU_FJMzzxaJ9SDaOa9vL9dKUviP7S0nnig0sPLa5KQgx81BnxbiQsAbmAQMr2cxYoNOXFMmjB_v-amsNBV6KkES74gA7LI0bo56DPEA9smlngWdtnvOgaqlsaSLPcRsS0FKO3qHAYNRBwWvMJpJX8SppIR1KiqmVKgeQavEMM6XMElJc9PDxHNZDfJkKZaYTJT8_qFIuFJVqX6J9DFnqXXVaFH4Wclq8IKZ01mayFbAFbfJarH28k_qLIxS8hOgq9VKNW5LW7XuIaMZ1Z17XlqZ96HT9TtCAcze9kBS9kMJewNCl-WYFvPCTCnwzQZ-HRVOM04vrQOgSPud7vlA3OqD4YY2PSz_ioWSbk98vbJ4c7WVHiFYwQsgQFvMzwES20hKPDrREYks5fAPVrHLuDK1doffY1hPTWF2KkSt0uERAcZIibeD5058uKSonW1fPurOnsTpAg8TfALFu1QlkcNt1X4dOoGpYmBR7HGIONwQwv5-peC8F758ujTTWWowBqXzJlA2boriCvdZkvS15rEnUN57lyO8gINQ5heiMCQN8NbHMmrY_ihJD3bdM4s2TGnWH4HBC2hi0jaIOJ8AoCXHQMaMdrGE1st7Y3R_T6Obg6VnabLn8Q-zZfToKdkiyaR9zqsVB8VsMrAtEz0yiGpaOF3KdI2sxvii3Q5XWIYN6gyDXsXVykFS25PsjPmXCF8V1mS7x6e9N9PtNTWwT8IGBZp9frOTQN2O52dOhPdsuCHAf0srrBVHbyYfCMYbOqYEEXQG0pNAmG_wqbTxNew9kTsXDRzYKW-NmEJcvy_xh1dDwg8xJc58Cl71e-rau3iP7o8mWhVSaxi4Bi6LAuj4UKVCt3IYCfm9AR1d5LqBFWU9LrJbRZSMlmUYwZf7PlrKmpnCnZvuismiL7DH3cnUjP0lWAvhy3gxZm1MK8KyRzWmHnTNqaVlL37c2xoE4YSyponeOu5D-lRl_Dp_C2PyR1kG6G0TCWS66UbU89Fu1qmwWjeQwYhzj2Jly9LRyClAbe86VJhIZE18YLPB-n1ng78qz7hHtQ8qT4ejY4csEjSRjjnHdz8U-06qErY-CXNNsVtzpYGuzZ1ZaXqzAQkUcREm98KR8c1vaXaQXumtDklMVgs76gLqZyiG1eCRbOQ6_EcQv7GeFnq5UIqoMH_Xzc78otBTvC5j3aCs5Pvf6k3gQ5ZU7E4uFVhZA7xoyD8sPX6rhdGL8JmLKJSGZQM5ccWpfpDJ5RWJp0bIJdnAJQ8gsYMRAI2OBxx2m2c76lNiUnB750dMe2H3pFzFQVkWQLkmGVY37cgmRNHyXboDMQ1U2nlbNH017dmklJCk4jVU8aA9Gpo8oHw","{{\"assistant_caller\":\"comet_above_composer\",\"conversation_guide_session_id\":\"{uuid.uuid4()}\",\"conversation_guide_shown\":null}}"],"feedback_source":"DEDICATED_COMMENTING_SURFACE","idempotence_token":"client:{uuid.uuid4()}","session_id":"{uuid.uuid4()}"}},"inviteShortLinkKey":null,"renderLocation":null,"scale":1,"useDefaultActor":false,"focusCommentID":null}}',
        'server_timestamps': 'true',
        'doc_id': '7994085080671282',
    }
    cookies = {
        "cookie": cookie
    }
    try:
        _get = requests.post("https://www.facebook.com/api/graphql/",headers=headers, cookies=cookies, params=_data)
        if '"errors"' not in _get.text:
            return True
        else:
            return False
    except:
        return False
    
def _Page(cookie, idfb, fb1, id):
    if '_' in id:
        uid = id.split('_')[1]
    else:
        uid = id
    headers = {
        "accept": "*/*", 
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7", 
        "content-type": "application/x-www-form-urlencoded", 
        "sec-ch-prefers-color-scheme": "light", 
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"", 
        "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"", 
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-model": "\"\"", 
        "sec-ch-ua-platform": "\"Linux\"", 
        "sec-ch-ua-platform-version": "\"\"", 
        "sec-fetch-dest": "empty", 
        "sec-fetch-mode": "cors", 
        "sec-fetch-site": "same-origin", 
        "x-asbd-id": "129477", 
        "x-fb-friendly-name": "CometUserFollowMutation", 
        "x-fb-lsd": "7_RkODA0fo-6ShZlbFpHEW"
    }
    _data = {
        'av': idfb,
        '__aaid': '0',
        '__user': idfb,
        '__a': '1',
        '__req': 'v',
        '__hs': '20038.HYP:comet_pkg.2.1..2.1',
        'dpr': '1',
        '__ccg': 'EXCELLENT',
        '__rev': '1018088939',
        '__s': 'z2jloc:ulhc8m:wfcq07',
        '__hsi': '7435892510460455151',
        '__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2CE4i5QdwSwAyUco5S3O2Saw8i2S1DwUx60GE5O0BU2_CxS320qa2OU7m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewyDwkUe9obrwh8lwUwgojUlDw-wUwxwjFovUaU3qxW2-VEbUGdG0HE88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13xe3a3Gfw-Kufxa3mUqwjVqwLwHwea',
        '__csr': 'goMkMmFYnk44OdtsAixBEr5ndERq8jiFnqsLeGayYyWJmqOH9dhJW8XiXZ5GKl2aji8WjAmG8AWlBF5hFtVppFFLhVo-rWiJ4Az-l13hGAy5-qmFGKbp4AS8BBxCWAAz8y8UjyFpAV-cAKchoC8UO2afgmx-lUF1emeCBXyo88C6U8Egz41DK262O788UOfgC3m6oS2-i48Z3E9lxu69U8e2a4o4TwhEdo6q2y1Ywk84W1lweim1jwywj8fE1r80NK053E14aS01LRwuE0d2E02Xbwlo18A0iLg0g5w1f-091w2MU0NK1-w3WE0row0AXw0sNovwOK0lq0EU0nNw208',
        '__comet_req': '15',
        'fb_dtsg': fb1,
        'jazoest': '25235',
        'lsd': 'lhDi8d5JyyeCV7Sav12RwC',
        '__spin_r': '1018088939',
        '__spin_b': 'trunk',
        '__spin_t': '1731303639',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'CometProfilePlusLikeMutation',
        'variables': '{"input":{"is_tracking_encrypted":false,"page_id":"'+str(uid)+'","source":null,"tracking":null,"actor_id":"'+str(idfb)+'","client_mutation_id":"1"},"scale":1}',
        'server_timestamps': 'true',
        'doc_id': '6716077648448761',
    }
    cookies = {
        "cookie": cookie
    }
    _Post = requests.post("https://www.facebook.com/api/graphql/", headers=headers, cookies=cookies, params=_data)
    if '"subscribe_status":"IS_SUBSCRIBED"' in _Post.text:
        return True
    else:
        return False
    
def _Share(cookie, idfb, fb1, uid):
    headers = {
        "accept": "*/*", 
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7", 
        "content-type": "application/x-www-form-urlencoded", 
        "sec-ch-prefers-color-scheme": "light", 
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"", 
        "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"", 
        "sec-ch-ua-mobile": "?0", 
        "sec-ch-ua-model": "\"\"", 
        "sec-ch-ua-platform": "\"Linux\"", 
        "sec-ch-ua-platform-version": "\"\"", 
        "sec-fetch-dest": "empty", 
        "sec-fetch-mode": "cors", 
        "sec-fetch-site": "same-origin", 
        "x-asbd-id": "129477", 
        "x-fb-friendly-name": "CometUFIFeedbackReactMutation", 
        "x-fb-lsd": "5dCcoMgOrU5CgUwl77gn-C"
    }
    _data = {
        'av': idfb,
        '__usid': r'6-Tsftw3x1vqj8dz:Psftw2g2c595x:0-Asftw3x1etit7l-RV=6:F=',
        '__aaid': '0',
        '__user': idfb,
        '__a': '1',
        '__req': '1o',
        '__hs': '19901.HYP:comet_pkg.2.1..2.1',
        'dpr': '1',
        '__ccg': 'EXCELLENT',
        '__rev': '1014511729',
        '__s': '8zktjb:5quia4:fu1x9q',
        '__hsi': '7384980750065440159',
        '__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C17xt3odE98K360CEboG0x8bo6u3y4o2Gwn82nwb-q7oc81xoswMwto886C11wBz83WwgEcEhwGxu782lwv89kbxS1Fwc61awkovwRwlE-U2exi4UaEW2G1jwUBwJK2W5olwUwgojUlDw-wSU8o4Wm7-2K0-poarCwLyES0Io88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13whEeE4WVU-4EdrxG1fy8bUaU',
        '__csr': 'gdk8MPs4dNYQYp4iOSD9sG2fZqN79mKHYBH4qrNP5bifl8IyAF-CDQGFdBdlTmeimHGOWJKhCKRWDLjGmV94uVpprh6FaDD_GcG5F4ECVqgCqhqRAKhd2oGAUBzaUCibGVHy9EFeayEjCxim598oxmmCETxObKuuUyfzF8411e2e7VHyq-dG8AK4oW4ogK69XzEy7U4aFQ4EdE426UKdxm7E98sG15Cw8Oi1awgUaolwvUO8wrU3ewNwt9UOvwko16o1z81uo1gA0cww1pHxGQE2Kw0sv80Ii6E03c4U9olw1N21Cw1eu05rE1oUmxiew0iIU0e5k0m-02jW1RyU2pwPw3uU0u3w4wAo0Xi0Bk',
        '__comet_req': '15',
        'fb_dtsg': fb1,
        'jazoest': '25587',
        'lsd': 'ZHQrlrBiNSI8IArPB91N6b',
        '__spin_r': '1014511729',
        '__spin_b': 'trunk',
        '__spin_t': '1719449821',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'ComposerStoryCreateMutation',
        'variables': '{"input":{"composer_entry_point":"share_modal","composer_source_surface":"feed_story","composer_type":"share","idempotence_token":"'+str(uuid.uuid4())+'_FEED","source":"WWW","attachments":[{"link":{"share_scrape_data":"{\\"share_type\\":22,\\"share_params\\":['+uid+']}"}}],"reshare_original_post":"RESHARE_ORIGINAL_POST","audience":{"privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"}},"is_tracking_encrypted":true,"tracking":["AZWWGipYJ1gf83pZebtJYQQ-iWKc5VZxS4JuOcGWLeB-goMh2k74R1JxqgvUTbDVNs-xTyTpCI4vQw_Y9mFCaX-tIEMg2TfN_GKk-PnqI4xMhaignTkV5113HU-3PLFG27m-EEseUfuGXrNitybNZF1fKNtPcboF6IvxizZa5CUGXNVqLISUtAWXNS9Lq-G2ECnfWPtmKGebm2-YKyfMUH1p8xKNDxOcnMmMJcBBZkUEpjVzqvUTSt52Xyp0NETTPTVW4zHpkByOboAqZj12UuYSsG3GEhafpt91ThFhs7UTtqN7F29UsSW2ikIjTgFPy8cOddclinOtUwaoMaFk2OspLF3J9cwr7wPsZ9CpQxU21mcFHxqpz7vZuGrjWqepKQhWX_ZzmHv0LR8K07ZJLu8yl51iv-Ram7er9lKfWDtQsuNeLqbzEOQo0UlRNexaV0V2m8fYke8ubw3kNeR5XsRYiyr958OFwNgZ3RNfy-mNnO9P-4TFEF12NmNNEm4N6h0_DRZ-g74n-X2nGwx9emPv4wuy9kvQGeoCqc636BfKRE-51w2GFSrHAsOUJJ1dDryxZsxQOEGep3HGrVp_rTsVv7Vk3JxKxlzqt3hnBGDgi6suTZnJw69poVOIz6TPCTthRhj7XUu4heyKBSIeHsjBRC2_s3NwuZ4kKNCQ2JkVuBXz_hsRhDmbAnBi6WUFIJhLHO_bGgKbEASuU4vtj4FNKo_G8p-J1kYmCo0Pi72Csi3EikuocfjHFwfSD3cCbetr3V8Yp6OmSGkqX63FkSqzBoAcHFeD-iyCAkn0UJGqU-0o670ZoR-twkUDcSJPXDN2NYQfqiyb9ZknZ7j04w1ZfAyaE7NCiCc-lDt1ic79XyHunjOyLStgXIW30J4OEw_hAn86LlRHbYVhi-zBBTZWWnEl9piuUz0qtnN-qEd002DjNYaMy0aDAbL9oOYDdN8mHvnXq1aKove9I4Jy0WtlxeN8279ayz7NdDZZ9LrajY_YxIJJqdZtJIuRYTunEeDsFrORpu3RYRbFwpGnQbHeSLH1YvwOyOJRXhYYmVLJEGD2N9r5wkPbgbx2HoWsGjWj_DpkEAyg59eBJy4RYPJHvOsetBQABEWmGI7nhUDYTPdhrzVxqB_g4fQ9JkPzIbEhcoEZjmspGZcR4z4JxUDJCNdAz2aK4lR4P5WTkLtj2uXMDD_nzbl8r_DMcj23bjPiSe0Fubu-VIzjwr7JgPNyQ1FYhp5u4lpqkkBkGtfyAaUjCgFhg4FW-H3d3vPVMO--GxbhK9kN0QAcOE3ZqQR2dRz6NbhcvTyNfDxy0dFTRw-f-vxn04gjJB5ZEG3WfSzQv0VbqDYm6-NFYAzIxbDLoiCu34WAa2lckx5qxncXBhQj6Fro2gXGPXo4d32DvqQg7_RHQ-SF_WLqdxRCXF91NIqxYmFZsOJAuQ5m6TafzuNnQoJB3OQFoknv8Uy5O4FKuwazh1rvLrsj-1QEMi3sTrr9KxJkZy9EKXs92ndlb3edgfycLOffTil-gW2BvxeNiMQzqF1xJqFBKHDyatgwpXDX81HDwxkuMEaGPREIeQLuOlBJrL_20RD1e4Gu4tjQD8vRsb29UNG60DqpDvc-H4Z2oxeppm0KIwQNaCTtGUxxmvT807fXMnuVEf5QI5qTx9YRJh56GiWLoHC_zPMhoikMbAybIVWh9HtVgZGgImDmz0l9P4LgtpKNnKbQj_2ZKn2ZhOYKZLdt1P2Jq2Z2z76MtbRQTrpZpFb14zWVnh1LFCSFPAB7sqC1-u-KQOf2_SjEecztPccso8xZB2nkhLetyPn9aFuO-J_LCZydQeiroXx4Z8NxhDpbLoOpw2MbRCVB_TxfnLGNn1QD0To9TTChxK5AHNRRLDaj3xK1e0jd37uSmHTkT6QJVHFHEYMVLBcuV1MQcoy0wsvc1sRb",null],"logging":{"composer_session_id":"'+str(uuid.uuid4())+'"},"navigation_data":{"attribution_id_v2":"FeedsCometRoot.react,comet.most_recent_feed,tap_bookmark,1719641912186,189404,608920319153834,,"},"event_share_metadata":{"surface":"newsfeed"},"actor_id":"'+idfb+'","client_mutation_id":"3"},"feedLocation":"NEWSFEED","feedbackSource":1,"focusCommentID":null,"gridMediaWidth":null,"groupID":null,"scale":1,"privacySelectorRenderLocation":"COMET_STREAM","checkPhotosToReelsUpsellEligibility":false,"renderLocation":"homepage_stream","useDefaultActor":false,"inviteShortLinkKey":null,"isFeed":true,"isFundraiser":false,"isFunFactPost":false,"isGroup":false,"isEvent":false,"isTimeline":false,"isSocialLearning":false,"isPageNewsFeed":false,"isProfileReviews":false,"isWorkSharedDraft":false,"hashtag":null,"canUserManageOffers":false,"__relay_internal__pv__CometIsAdaptiveUFIEnabledrelayprovider":true,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__IncludeCommentWithAttachmentrelayprovider":true,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":true,"__relay_internal__pv__StoriesRingrelayprovider":false,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":false}',
        'server_timestamps': 'true',
        'doc_id': '8167261726632010'
    }
    cookies = {
        "cookie": cookie
    }
    _post = requests.post("https://www.facebook.com/api/graphql/",headers=headers, cookies=cookies, params=_data)
    if '"errors"' not in _post.text:
        return True
    else:
        return False
    
def _Bypass(cookie, idfb, fb1):
    headers = {
        "accept": "*/*", 
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7", 
        "content-type": "application/x-www-form-urlencoded", 
        "sec-ch-prefers-color-scheme": "light", 
        "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"", 
        "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"", 
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-model": "\"\"", 
        "sec-ch-ua-platform": "\"Linux\"", 
        "sec-ch-ua-platform-version": "\"\"", 
        "sec-fetch-dest": "empty", 
        "sec-fetch-mode": "cors", 
        "sec-fetch-site": "same-origin", 
        "x-asbd-id": "129477", 
        "x-fb-friendly-name": "CometUserFollowMutation", 
        "x-fb-lsd": "7_RkODA0fo-6ShZlbFpHEW"
    }
    data = {
        "av": idfb,
        "__user": idfb,
        "__a": "1",
        "__req": "8",
        "__hs": "20038.HYP:comet_pkg.2.1..2.1",
        "dpr": "1",
        "__ccg": "EXCELLENT",
        "__rev": "1018089718",
        "__s": "mtrukx:3ui1ys:yphvdu",
        "__hsi": "7435940161710523784",
        "__dyn": "7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo19oe8hw2nVE4W099w8G1Dz81s8hwnU2lwv89k2C1Fwc60D8vwRwlE-U2zxe2GewbS361qw8Xwn82Lx-0lK3qazo720Bo2ZwrU6C0hq1Iwqo35wvodo7u2-2K0UE",
        "__csr": "gzl5849ahWFaeU-rK4Uyii9VAmWl6zpUCUgK3K2mi2q2Ki687W08Pyo1yp9Esw14e0OE1u80now05XXw0Dhw0eNi",
        "__comet_req": "15",
        "fb_dtsg": fb1,
        "jazoest": "25487",
        "lsd": "PEkEdpWB34ZUqD6iqvcwMP",
        "__spin_r": "1018089718",
        "__spin_b": "trunk",
        "__spin_t": "1731314734",
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "FBScrapingWarningMutation",
        "variables": "{}",
        "server_timestamps": "true",
        "doc_id": "6339492849481770"
    }
    cookies = {
        "cookie": cookie
    }
    bypass = requests.post('https://www.facebook.com/api/graphql/',headers=headers, cookies=cookies, params=data)
    return bypass.text

def Nhap_Cookie():
    demck = 0
    listck = []
    while True:
        demck += 1
        ck = input(f'{thanh}{luc} Nhập Cookie Facebook Thứ {vang}{demck}: {vang} ')
        if ck == '' and demck > 1:
            break
        _info = _Infofb(ck)
        if _info == False:
            print(f'{Fore.RED}Cookie Facebook Die, Vui Lòng Nhập Lại!!!')
            demck-=1
        else:
            print(f'{luc}NAME FACEBOOK: {vang}{_info[2]}')
            listck.append(ck)
    return listck

def Main():
    dem = 0
    ptool = 0
    banner()
    while True:
        if os.path.exists('configttc.txt'):
            with open('configttc.txt', 'r') as f:
                tk = f.read()
            login = requests.post('https://tuongtaccheo.com/logintoken.php',data={'access_token': tk})
            if login.json()['status'] == 'success':
                cookie = 'PHPSESSID='+(login.cookies)['PHPSESSID']
                user = login.json()['data']['user']
                print(f'{thanh} {luc}Nhập {do}[{vang}1{do}]{luc} Để Log Acc {vang}{user}')
                print(f'{thanh} {luc}Nhập {do}[{vang}2{do}]{luc} Để Thay Access_Token TTC Mới ')
                chon = Write.Input(f'Lựa Chọn Của Bạn: ',Colors.green_to_yellow,interval=0.0001)
                if chon == '2':
                    os.remove('configttc.txt')
                elif chon == '1':
                    pass
                else:
                    print(f'{red}Lựa chọn không xác định !!!')
                    continue
            else:
                os.remove('configttc.txt')
        if not os.path.exists('configttc.txt'):
            tk = input(f'{luc}Nhập Access_token TTC{vang}: ')
            with open('configttc.txt', 'w') as f:
                f.write(tk)
        with open('configttc.txt', 'r') as f:
            tk = f.read()
        login = requests.post('https://tuongtaccheo.com/logintoken.php',data={'access_token': tk})
        if login.json()['status'] == 'success':
            cookie = 'PHPSESSID='+(login.cookies)['PHPSESSID']
            user = login.json()['data']['user']
            sodu = login.json()['data']['sodu']
            print(f"{luc}Tài Khoản: {vang}{user} {luc}| {luc}Xu Hiện Tại: {vang}{sodu}")
            break
        else:
            os.remove ('configttc.txt')
            continue
    while True:
        if os.path.exists('Cookie_FB.txt'):
            os.system("cls" if os.name == "nt" else "clear")
            print(f'{thanh} {luc}Nhập {do}[{vang}1{do}]{luc} Sử Dụng Cookie Facebook Đã Lưu')
            print(f'{thanh} {luc}Nhập {do}[{vang}2{do}]{luc} Nhập Cookie Facebook Mới')
            chon = input(f"{thanh}{luc} Nhập Lựa Chọn : {vang}")
            if chon == '1':
                print('\033[1;32mĐang Lấy Dữ Liệu Đã Lưu')
                sleep(1)
                with open('Cookie_FB.txt', 'r') as f:
                    listck = json.loads(f.read())
                    break
            elif chon == '2':
                print(f"{red}════════════════════════════════════════════════════")
                os.remove('Cookie_FB.txt')
            else:
                print(f'{red}Lựa Chọn Không Xác Định.')
                continue
        if not os.path.exists('Cookie_FB.txt'):
            listck = Nhap_Cookie()
            with open('Cookie_FB.txt', 'w') as f:
                json.dump(listck, f)
                break
    banner()
    print(f"{trang}════════════════════════════════════════════════════")
    print(f"{luc}Tên Tài Khoản: {vang}{user} {luc}")
    print(f"{luc}Xu Hiện Tại: {vang}{sodu}")
    print(f"{trang}════════════════════════════════════════════════════")
    print(f"{thanh} {luc}Nhập {do}[{vang}1{do}]{luc} Để Chạy Nhiệm Vụ Like Vip")
    print(f"{thanh} {luc}Nhập {do}[{vang}2{do}]{luc} Để Chạy Nhiệm Vụ Cảm Xúc Vip")
    print(f"{thanh} {luc}Nhập {do}[{vang}3{do}]{luc} Để Chạy Nhiệm Vụ Cảm Xúc Cmt")
    print(f"{trang}════════════════════════════════════════════════════")
    nhiemvu = input (f'{thanh}{luc} Nhập Nhiệm Vụ Cần Chạy: {vang}')
    min = 0
    max = 5
    nvblock = int(input(f'{thanh}{luc} Sau Bao Nhiêu Nhiệm Vụ Thì Chống Block: {vang}'))
    delaybl = int(input(f'{thanh}{luc} Sau {lam}{nvblock} Nhiệm Vụ Thì Nghỉ Ngơi: {vang}'))
    doinick = int(input(f'{thanh}{luc} Sau Bao Nhiêu Nhiệm Vụ Thì Đổi Nick: {vang}'))
    nhiemvuloi = int(input(f'{thanh}{luc} Lỗi Bao Nhiêu Nhiệm Vụ Thì Xóa Cookie: {vang}'))
    proxy = input(f"{thanh}{luc} Nhập Proxy (hoặc Enter để bỏ qua): {vang}").strip()
    proxies = {"http": proxy, "https": proxy} if proxy else None
    while True:
        if len(listck) == 0:
            print(f'{red}Đã Xoá Tất Cả Cookie, Vui Lòng Nhập Lại')
            listck = Nhap_Cookie()
            with open('Cookie_FB.txt', 'w') as f:
                json.dump(listck, f)
        for ck in listck:
            loilike, loicamxuc, loicxcmt, loifl, loicmt, loishare, loilikepage = 0, 0, 0, 0, 0, 0, 0
            _info = _Infofb(ck)
            if _info != False:
                uidfb = _info[1]
                tenfb = _info[2]
            else:
                uidfb = ck.split('c_user=')[1].split(';')[0]
                print(f'{red}Cookie Tài Khoản {uidfb} Die', end='\r');sleep(3); print('                                     ', end = '\r' )
                listck.remove(ck)
                continue
            headers = {
                'Host': 'tuongtaccheo.com',
                'accept':'*/*',
                'origin':'https://tuongtaccheo.com',
                'x-requested-with':'XMLHttpRequest',
                'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
                'referer':'https://tuongtaccheo.com/cauhinh/facebook.php',
                "cookie": cookie
            }
            data = {
                'iddat[]': uidfb,
                'loai': 'fb'
            }
            cauhinh = requests.post('https://tuongtaccheo.com/cauhinh/datnick.php',headers=headers, data=data, timeout=5).text
            if '1' in cauhinh:
                print(f'{luc}ID Facebook: {vang}{_info[1].encode("utf-8", "replace").decode()} {vang}| {luc}Tên Facebook: {vang}{_info[2].encode("utf-8", "replace").decode()}')
            else:
                print(do+f" Cấu Hình Thất Bại UID FB: {do}{uidfb} {cam}| {cam}Tên FB: {lam}{tenfb}")
                continue
            ptool = 0
            while True:
                nvlikevip = 1 if '1' in nhiemvu else 0
                nvreacvip = 1 if '2' in nhiemvu else 0
                nvreaccmt = 1 if '3' in nhiemvu else 0
                
                if nvlikevip == 1:
                    listlike = getjob(cookie, 'likepostvipcheo')
                    like1 = listlike.text
                    like2 = listlike.json()
                    if like1 == []:
                        print(f'{luc}Hết Nhiệm Vụ Like Vip                            ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                        nvlikevip = 0
                    elif 'error' in like2:
                        print(f'{luc}Delay Get Job 10s                    ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                        countdown(10)
                        nvlikevip = 0
                    else:
                        print(f'{luc}Tìm Thấy {vang}{len(like2)} {luc}Nhiệm Vụ Like Vip                      ', end = '\r')
                        for x in like2:
                            try:
                                idpost = x['idpost']
                                link = x['link']
                            except:
                                countdown(6)
                            getuid = requests.post('https://id.traodoisub.com/api.php',data={'link': link}).json()
                            if 'success' in getuid:
                                uuid = getuid['id']
                            else:
                                print(f'{red}Link bài viết đã bị die, đang đổi link...', end = '\r'); sleep(2); print('                                                       ', end = '\r')
                                countdown(3)
                            like = _Like(ck, uuid, "LIKE", _info[0], _info[1])
                            if like == False:
                                print(f"{red}FAIL LIKE: {lam}{uuid}             ", end = '\r'); sleep(2); print('                                                       ', end = '\r')
                                _Bypass(ck, _info[1], _info[0])
                                loilike += 1
                                countdown(3)
                            else:
                                headers = {
                                    "Host":"tuongtaccheo.com",
                                    "x-requested-with":"XMLHttpRequest",
                                    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
                                    "origin":"https://tuongtaccheo.com",
                                    "cookie": cookie
                                }
                                data = {
                                    'id': idpost
                                }
                                nhan = requests.post('https://tuongtaccheo.com/kiemtien/likepostvipcheo/nhantien.php',headers=headers, data=data).json()
                                if 'mess' in nhan:
                                    headers = {
                                        "Host": "tuongtaccheo.com",
                                        "x-requested-with": "XMLHttpRequest",
                                        "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
                                        "cookie": cookie
                                    }
                                    get = requests.get('https://tuongtaccheo.com/home.php',headers=headers).text
                                    xu = get.split('"soduchinh">')[1].split('<')[0]
                                    dem+=1
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(f'{do}| {vang}{dem}{do} | {xanh}{time}{do} | {vang}LIKE{do} | {trang}{uuid}{do} | {vang}+1100{do} | {luc}{str(format(int(xu),","))} {do}| {xanh}{user}')
                                    loilike = 0
                                    if dem % doinick == 0:
                                        ptool = 1
                                        break
                                    if dem % nvblock == 0:
                                        chongblock(delaybl)
                                    else:
                                        _delay(randint(min, max))

                            if loilike >= nhiemvuloi:
                                _info = _Infofb(ck)
                                if _info !=False:
                                    print(f'{red}Cookie Tài Khoản {vang}{tenfb}{red} Đã Bị Out !!!                ')
                                else:
                                    print(f'{red}Tài Khoản {vang}{tenfb} {red}Đã Bị Block {vang}Like {red}!!!					')
                                listck.remove(ck)
                                ptool = 1
                                break
                
                if ptool == 1:
                    break

                
                if nvreacvip == 1:
                    listcx = getjob(cookie, 'camxucvipcheo')
                    like1 = listcx.text
                    like2 = listcx.json()
                    if like1 == []:
                        print(f'{luc}Hết Nhiệm Vụ Cảm Xúc Vip                            ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                        nvreacvip = 0
                    elif 'error' in like2:
                        print(f'{luc}Lấy nhiệm vụ sau 15 giây                            ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                        countdown(15)
                        nvreacvip = 0
                    else:
                        print(f'{luc}Tìm Thấy {vang}{len(like2)} {luc}Nhiệm Vụ Cảm Xúc Vip                       ', end = '\r')
                        for x in like2:
                            try:
                                idpost = x['idpost']
                                link = x['link']
                                typee = x['loaicx']
                            except:
                                countdown(6)
                            getuid = requests.post('https://id.traodoisub.com/api.php',data={'link': link}).json()
                            if 'success' in getuid:
                                uuid = getuid['id']
                            else:
                                print(f'{red}Link bài viết đã bị die, đang đổi link...', end = '\r'); sleep(2); print('                                                       ', end = '\r')
                                countdown(3)
                            like = _Like(ck, uuid, typee, _info[0], _info[1])
                            if like == False:
                                print(f"{cam}FAIL {lam}{typee}{trang}: {vang}{uuid}             ", end = '\r'); sleep(2); print('                                                       ', end = '\r')
                                _Bypass(ck, _info[1], _info[0])
                                loicamxuc += 1
                                countdown(3)
                            else:
                                headers = {
                                    "Host":"tuongtaccheo.com",
                                    "x-requested-with":"XMLHttpRequest",
                                    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
                                    "origin":"https://tuongtaccheo.com",
                                    "cookie": cookie
                               }
                                data = {
                                    'id': idpost
                                }
                                nhan = requests.post('https://tuongtaccheo.com/kiemtien/camxucvipcheo/nhantien.php',headers=headers, data=data).json()
                                if 'mess' in nhan:
                                    headers = {
                                        "Host": "tuongtaccheo.com",
                                        "x-requested-with": "XMLHttpRequest",
                                        "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
                                        "cookie": cookie
                                    }
                                    get = requests.get('https://tuongtaccheo.com/home.php',headers=headers).text
                                    xu = get.split('"soduchinh">')[1].split('<')[0]
                                    dem+=1
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(f'{do}| {vang}{dem}{do} | {xanh}{time}{do} | {vang}{typee}{do} | {trang}{uuid}{do} | {vang}+1100{do} | {luc}{str(format(int(xu),","))} {do}| {xanh}{user}')
                                    loicamxuc = 0
                                    if dem % doinick == 0:
                                        ptool = 1
                                        break
                                    if dem % nvblock == 0:
                                        chongblock(delaybl)
                                    else:
                                        _delay(randint(min, max))

                            if loicamxuc >= nhiemvuloi:
                                _info = _Infofb(ck)
                                if _info !=False:
                                    print(f'{red}Cookie Tài Khoản {lam}{tenfb}{red} Đã Bị Out !!!                ')
                                else:
                                    print(f'{red}Tài Khoản {lam}{tenfb} {red}Đã Bị Block Cảm Xúc {red}!!!					')
                                listck.remove(ck)
                                ptool = 1
                                break

                if ptool == 1:
                    break

                
                if nvreaccmt == 1:
                    listcxcmt = getjob(cookie, 'camxuccheobinhluan')
                    like1 = listcxcmt.text
                    like2 = listcxcmt.json()
                    if like1 == []:
                        print(f'{cam}Hết Nhiệm Vụ Cảm Xúc Cmt             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                        nvreaccmt = 0
                    elif 'error' in like2:
                        print(f'{cam}Lấy nhiệm vụ sau 15 giây                            ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                        countdown(15)
                        nvreaccmt = 0
                    else:
                        print(f'{luc}Tìm Thấy {vang}{len(like2)} {luc}Nhiệm Vụ Cảm Xúc Cmt                     ', end = '\r')
                        for x in like2:
                            try:
                                idpost = x['idpost']
                                link = x['link']
                                typee = x['loaicx']
                            except:
                                countdown(6)
                            getuid = requests.post('https://id.traodoisub.com/api.php',data={'link': link}).json()
                            if 'success' in getuid:
                                uuid = getuid['id']
                            else:
                                print(f'{red}Link bài viết đã bị die, đang đổi link...', end = '\r'); sleep(2); print('                                                       ', end = '\r')
                                countdown(3)
                            getuid = requests.post('https://id.traodoisub.com/api.php',data={'link': link}).json()
                            uid = 'Ẩn ID'
                            like = _React_Cmt(ck, _info[1], _info[0], uuid, typee)
                            if like == False:
                                print(f"{cam}FAIL {lam}{typee} CMT{trang}: {lam}{uuid}             ", end = '\r'); sleep(2); print('                                                       ', end = '\r')
                                _Bypass(ck, _info[1], _info[0])
                                loicxcmt += 1
                                countdown(3)
                            else:
                                headers = {
                                    "Host":"tuongtaccheo.com",
                                    "x-requested-with":"XMLHttpRequest",
                                    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
                                    "origin":"https://tuongtaccheo.com",
                                    "cookie": cookie
                                }
                                data = {
                                    'id': idpost
                                }
                                nhan = requests.post('https://tuongtaccheo.com/kiemtien/camxuccheobinhluan/nhantien.php',headers=headers, data=data).json()
                                if 'mess' in nhan:
                                    headers = {
                                        "Host": "tuongtaccheo.com",
                                        "x-requested-with": "XMLHttpRequest",
                                        "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
                                        "cookie": cookie
                                    }
                                    get = requests.get('https://tuongtaccheo.com/home.php',headers=headers).text
                                    xu = get.split('"soduchinh">')[1].split('<')[0]
                                    dem+=1
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(f'{do}| {vang}{dem}{do} | {xanh}{time}{do} | {vang}{typee}CMT{do} | {trang}{uuid}{do} | {vang}+600{do} | {luc}{str(format(int(xu),","))} {do}| {xanh}{user}')
                                    loicxcmt = 0
                                    if dem % doinick == 0:
                                        ptool = 1
                                        break
                                    if dem % nvblock == 0:
                                        chongblock(delaybl)
                                    else:
                                        _delay(randint(min, max))

                            if loicxcmt >= nhiemvuloi:
                                _info = _Infofb(ck)
                                if _info !=False:
                                    print(f'{red}Cookie Tài Khoản {lam}{tenfb}{red} Đã Bị Out !!!                ')
                                else:
                                    print(f'{red}Tài Khoản {lam}{tenfb} {red}Đã Bị Block {vang}Cảm Xúc {red}!!!					')
                                listck.remove(ck)
                                ptool = 1
                                break

                if ptool == 1:
                    break

                
                if loilike + loicamxuc + loicxcmt == 0:
                    for i in range(10, 0, -1):
                        Write.Print(f' Tất Cả Các Nhiệm Vụ Đã Hết, Vui Lòng Chờ {i} Giây ',Colors.cyan_to_blue,interval=0.0001, end = '\r');sleep(1); print('                                                        ', end = '\r')

if __name__ == '__main__':
    Main()

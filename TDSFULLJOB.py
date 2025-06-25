import requests, json, base64, os, uuid, re
from time import sleep
from random import randint
from datetime import datetime
import requests, json, base64, os, uuid, re
from time import sleep
from random import randint
from datetime import datetime
import os,sys
red = "\033[1;31m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
trang = "\033[1;37m"
tim = "\033[1;35m"
lam = "\033[1;36m"
hong = "🌸"
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
AQUA = "\033[96m"
LIME = "\033[92m"
thanh = f'{red}[{trang}</>{red}] {trang}=>'
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
listnv = []
listck = []

def read_proxy_file(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except:
        return []
        
def thanhngang(so):
    for i in range(so):
        print(trang+'-',end ='')
    print('')

print("Chờ tí,đợi load tool...")
# Hiệu ứng tải
for i in range(1, 101):
  sys.stdout.write(f"\r{BOLD}{LIME}ĐANG LOADING: {i}% {'█' * (i // 5)}{RESET}")
  sys.stdout.flush()
  sleep(0.03)  # Điều chỉnh thời gian chờ nếu cần
print("Load tool thành công!  Mời bn trải nghiệm 😍")
sleep(1)
def banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner = f"""
\033[32;5;245m\033[1m\033[38;5;39m███╗   ██╗██████╗    ████████╗ ██████╗  ██████╗ ██╗     
\033[32;5;245m\033[1m\033[38;5;39m████╗  ██║██╔══██╗   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
\033[32;5;245m\033[1m\033[38;5;39m██╔██╗ ██║██████╔╝█████╗██║   ██║   ██║██║   ██║██║     
\033[32;5;245m\033[1m\033[38;5;39m██║╚██╗██║██╔═══╝ ╚════╝██║   ██║   ██║██║   ██║██║     
\033[32;5;245m\033[1m\033[38;5;39m██║ ╚████║██║           ██║   ╚██████╔╝╚██████╔╝███████╗
\033[32;5;245m\033[1m\033[38;5;39m╚═╝  ╚═══╝╚═╝           ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
\033[1;36m╠═══════════════════════════════════════════════╣
\033[1;36m║\033[38;5;204m▶ \033[38;5;204mNhóm   : \033[38;5;20mhttps://zalo.me/g/vmugmo123        \033[1;36m║
\033[1;36m║\033[38;5;204m▶ \033[38;5;204mZalo : \033[38;5;1204m0394764859                          \033[1;36m║
\033[1;36m║\033[38;5;204m▶ \033[38;5;204mTool Do Tao Code 😆                      \033[1;36m║
\033[1;36m║\033[38;5;204m▶ \033[38;5;204mMay Anh Dung Bug Tool Em 😭                \033[1;36m║
\033[1;36m║\033[38;5;204m▶ \033[38;5;204mPhiên Bản Tool : 1.0 ( VIP )                 \033[1;36m║
\033[1;36m╚═══════════════════════════════════════════════╝                                                        
"""
    print(banner)
    thanhngang(65)
    print(f'''{thanh} {luc}Admin{luc}: {tim}{hong}NP-TOOL
{thanh} {luc} Code By{trang}: {tim}{hong}Đàm Hữu Phước
{thanh} {luc}Link Box{trang}: {tim}{hong}https://zalo.me/g/vmugmo123
{thanh} {luc}Bạn Đang Sử Dụng Tool{trang}: {vang}{hong}Trao Đổi Sub Facebook ''')
    thanhngang(65)
def Delay(value):
	while not(value <= 1):
		value -= 0.123
		print(f'''{trang}[{hong}NTOOL{tim}] [{hong}DELAY{trang}] [{hong}{str(value)[0:5]}{trang}] [{vang}█    {trang}]''', '               ', end = '\r')
		sleep(0.010)
		print(f'''{trang}[{hong}NTOOL{tim}] [{hong}DELAY{trang}] [{hong}{str(value)[0:5]}{trang}] [ {vang}█   {trang}]''', '               ', end = '\r')
		sleep(0.010)
		print(f'''{trang}[{hong}NTOOL{tim}] [{hong}DELAY{trang}] [{hong}{str(value)[0:5]}{trang}] [  {vang}█  {trang}]''', '               ', end = '\r')
		sleep(0.010)
		print(f'''{trang}[{hong}NTOOL{tim}] [{hong}DELAY{trang}] [{hong}{str(value)[0:5]}{trang}] [   {vang}█ {trang}]''', '               ', end = '\r')
		sleep(0.010)
		print(f'''{trang}[{hong}NTOOL{tim}] [{hong}DELAY{trang}] [{hong}{str(value)[0:5]}{trang}] [    {vang}█{trang}]''', '               ', end = '\r')
		sleep(0.010)
def decode_base64(encoded_str):
	decoded_bytes = base64.b64decode(encoded_str)
	decoded_str = decoded_bytes.decode('utf-8')
	return decoded_str

def encode_to_base64(_data):
	byte_representation = _data.encode('utf-8')
	base64_bytes = base64.b64encode(byte_representation)
	base64_string = base64_bytes.decode('utf-8')
	return base64_string
()
class Facebook_Api(object):
    def __init__(self, cookie, proxy=None):
        try:
            self.lsd = ''
            self.fb_dtsg = ''
            self.jazoest = ''
            self.cookie = cookie
            self.actor_id = self.cookie.split('c_user=')[1].split(';')[0]
            self.proxies = None
            self.headers = {
                'authority': 'www.facebook.com',
                'accept': '*/*',
                'cookie': self.cookie,
                'origin': 'https://www.facebook.com',
                'referer': 'https://www.facebook.com/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin'
            }
            if proxy:
                try:
                    proxy_parts = proxy.strip().split(':')
                    if len(proxy_parts) == 4:
                        host, port, user, password = proxy_parts
                        self.proxies = {
                            'http': f'http://{user}:{password}@{host}:{port}',
                            'https': f'http://{user}:{password}@{host}:{port}'
                        }
                except Exception as e:
                    print(f"Lỗi khởi tạo proxy: {str(e)}")
                    self.proxies = None
            url = requests.get(f'https://www.facebook.com/{self.actor_id}', headers=self.headers, proxies=self.proxies).url
            response = requests.get(url, headers=self.headers, proxies=self.proxies).text
            matches = re.findall(r'\["DTSGInitialData",\[\],\{"token":"(.*?)"\}', response)
            if len(matches) > 0:
                self.fb_dtsg += matches[0]
                self.jazoest += re.findall(r'jazoest=(.*?)\"', response)[0]
                self.lsd += re.findall(r'\["LSD",\[\],\{"token":"(.*?)"\}', response)[0]
        except:
            pass
    
    def info(self):
        get = requests.get('https://www.facebook.com/me',headers=self.headers, proxies=self.proxies).text
        try:
            name = get.split('<title>')[1].split('</title>')[0]
            return {'success': 200, 'id': self.actor_id, 'name': name}
        except:
            return {'error': 200}
    
    def Checkspam(self):
        data = {
            "av": self.actor_id,
            "__user": self.actor_id,
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
            "fb_dtsg": self.fb_dtsg,
            "jazoest": self.jazoest,
            "lsd": self.lsd,
            "__spin_r": "1018089718",
            "__spin_b": "trunk",
            "__spin_t": "1731314734",
            "fb_api_caller_class": "RelayModern",
            "fb_api_req_friendly_name": "FBScrapingWarningMutation",
            "variables": "{}",
            "server_timestamps": "true",
            "doc_id": "6339492849481770"
        }
        response = requests.post('https://www.facebook.com/api/graphql/',headers=self.headers, data=data, proxies=self.proxies)
        return response.text
        
    def reaction(self, id, type):
        reac = {
            "LIKE": "1635855486666999",
            "LOVE": "1678524932434102",
            "CARE": "613557422527858",
            "HAHA": "115940658764963",
            "WOW": "478547315650144",
            "SAD": "908563459236466",
            "ANGRY": "444813342392137"
        }
        idreac = reac.get(type)
        data = {
            'av': self.actor_id,
            '__usid': r'6-Tsfgotwhb2nus:Psfgosvgerpwk:0-Asfgotw11gc1if-RV=6:F=',
            '__aaid': '0',
            '__user': self.actor_id,
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
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'lsd': self.lsd,
            '__spin_r': '1014402108',
            '__spin_b': 'trunk',
            '__spin_t': '1719025807',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
            'variables': fr'{{"input":{{"attribution_id_v2":"CometHomeRoot.react,comet.home,tap_tabbar,1719027162723,322693,4748854339,,","feedback_id":"{encode_to_base64("feedback:"+str(id))}","feedback_reaction_id":"{idreac}","feedback_source":"NEWS_FEED","is_tracking_encrypted":true,"tracking":["AZWUDdylhKB7Q-Esd2HQq9i7j4CmKRfjJP03XBxVNfpztKO0WSnXmh5gtIcplhFxZdk33kQBTHSXLNH-zJaEXFlMxQOu_JG98LVXCvCqk1XLyQqGKuL_dCYK7qSwJmt89TDw1KPpL-BPxB9qLIil1D_4Thuoa4XMgovMVLAXncnXCsoQvAnchMg6ksQOIEX3CqRCqIIKd47O7F7PYR1TkMNbeeSccW83SEUmtuyO5Jc_wiY0ZrrPejfiJeLgtk3snxyTd-JXW1nvjBRjfbLySxmh69u-N_cuDwvqp7A1QwK5pgV49vJlHP63g4do1q6D6kQmTWtBY7iA-beU44knFS7aCLNiq1aGN9Hhg0QTIYJ9rXXEeHbUuAPSK419ieoaj4rb_4lA-Wdaz3oWiWwH0EIzGs0Zj3srHRqfR94oe4PbJ6gz5f64k0kQ2QRWReCO5kpQeiAd1f25oP9yiH_MbpTcfxMr-z83luvUWMF6K0-A-NXEuF5AiCLkWDapNyRwpuGMs8FIdUJmPXF9TGe3wslF5sZRVTKAWRdFMVAsUn-lFT8tVAZVvd4UtScTnmxc1YOArpHD-_Lzt7NDdbuPQWQohqkGVlQVLMoJNZnF_oRLL8je6-ra17lJ8inQPICnw7GP-ne_3A03eT4zA6YsxCC3eIhQK-xyodjfm1j0cMvydXhB89fjTcuz0Uoy0oPyfstl7Sm-AUoGugNch3Mz2jQAXo0E_FX4mbkMYX2WUBW2XSNxssYZYaRXC4FUIrQoVhAJbxU6lomRQIPY8aCS0Ge9iUk8nHq4YZzJgmB7VnFRUd8Oe1sSSiIUWpMNVBONuCIT9Wjipt1lxWEs4KjlHk-SRaEZc_eX4mLwS0RcycI8eXg6kzw2WOlPvGDWalTaMryy6QdJLjoqwidHO21JSbAWPqrBzQAEcoSau_UHC6soSO9UgcBQqdAKBfJbdMhBkmxSwVoxJR_puqsTfuCT6Aa_gFixolGrbgxx5h2-XAARx4SbGplK5kWMw27FpMvgpctU248HpEQ7zGJRTJylE84EWcVHMlVm0pGZb8tlrZSQQme6zxPWbzoQv3xY8CsH4UDu1gBhmWe_wL6KwZJxj3wRrlle54cqhzStoGL5JQwMGaxdwITRusdKgmwwEQJxxH63GvPwqL9oRMvIaHyGfKegOVyG2HMyxmiQmtb5EtaFd6n3JjMCBF74Kcn33TJhQ1yjHoltdO_tKqnj0nPVgRGfN-kdJA7G6HZFvz6j82WfKmzi1lgpUcoZ5T8Fwpx-yyBHV0J4sGF0qR4uBYNcTGkFtbD0tZnUxfy_POfmf8E3phVJrS__XIvnlB5c6yvyGGdYvafQkszlRrTAzDu9pH6TZo1K3Jc1a-wfPWZJ3uBJ_cku-YeTj8piEmR-cMeyWTJR7InVB2IFZx2AoyElAFbMuPVZVp64RgC3ugiyC1nY7HycH2T3POGARB6wP4RFXybScGN4OGwM8e3W2p-Za1BTR09lHRlzeukops0DSBUkhr9GrgMZaw7eAsztGlIXZ_4"],"session_id":"{uuid.uuid4()}","actor_id":"{self.actor_id}","client_mutation_id":"3"}},"useDefaultActor":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false}}',
            'server_timestamps': 'true',
            'doc_id': '7047198228715224',
        }
        response = requests.post('https://www.facebook.com/api/graphql/',headers=self.headers, data=data, proxies=self.proxies)
        if '{"data":{"feedback_react":{"feedback":{"id":' in response.text:
            return True
        else:
            return False
        
    def reactioncmt(self, id, type):
        reac = {
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
        starttime = timestamp.replace('.', '')
        id_reac = reac.get(type)
        data = {
            'av': self.actor_id, 
            '__aaid': '0', 
            '__user': self.actor_id, 
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
            'fb_dtsg': self.fb_dtsg, 
            'jazoest': self.jazoest, 
            'lsd': self.lsd, 
            '__spin_r': '1014619389', 
            '__spin_b': 'trunk', 
            '__spin_t': '1719930656', 
            'fb_api_caller_class': 'RelayModern', 
            'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation', 
            'variables': '{"input":{"attribution_id_v2":"CometVideoHomeNewPermalinkRoot.react,comet.watch.injection,via_cold_start,1719930662698,975645,2392950137,,","feedback_id":"'+encode_to_base64("feedback:"+str(id))+'","feedback_reaction_id":"'+id_reac+'","feedback_source":"TAHOE","is_tracking_encrypted":true,"tracking":[],"session_id":"'+str(uuid.uuid4())+'","downstream_share_session_id":"'+str(uuid.uuid4())+'","downstream_share_session_origin_uri":"https://fb.watch/t3OatrTuqv/?mibextid=Nif5oz","downstream_share_session_start_time":"'+starttime+'","actor_id":"'+self.actor_id+'","client_mutation_id":"1"},"useDefaultActor":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false}', 
            'server_timestamps': 'true', 
            'doc_id': '7616998081714004',
        }
        response = requests.post('https://www.facebook.com/api/graphql/',headers=self.headers, data=data, proxies=self.proxies)
        if '{"data":{"feedback_react":{"feedback":{"id":' in response.text:
            return True
        else:
            return False
        
    def share(self, id):
        data = {
            'av': self.actor_id,
            '__usid': r'6-Tsftw3x1vqj8dz:Psftw2g2c595x:0-Asftw3x1etit7l-RV=6:F=',
            '__aaid': '0',
            '__user': self.actor_id,
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
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'lsd': self.lsd,
            '__spin_r': '1014511729',
            '__spin_b': 'trunk',
            '__spin_t': '1719449821',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'ComposerStoryCreateMutation',
            'variables': '{"input":{"composer_entry_point":"share_modal","composer_source_surface":"feed_story","composer_type":"share","idempotence_token":"'+str(uuid.uuid4())+'_FEED","source":"WWW","attachments":[{"link":{"share_scrape_data":"{\\"share_type\\":22,\\"share_params\\":['+id+']}"}}],"reshare_original_post":"RESHARE_ORIGINAL_POST","audience":{"privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"}},"is_tracking_encrypted":true,"tracking":["AZWWGipYJ1gf83pZebtJYQQ-iWKc5VZxS4JuOcGWLeB-goMh2k74R1JxqgvUTbDVNs-xTyTpCI4vQw_Y9mFCaX-tIEMg2TfN_GKk-PnqI4xMhaignTkV5113HU-3PLFG27m-EEseUfuGXrNitybNZF1fKNtPcboF6IvxizZa5CUGXNVqLISUtAWXNS9Lq-G2ECnfWPtmKGebm2-YKyfMUH1p8xKNDxOcnMmMJcBBZkUEpjVzqvUTSt52Xyp0NETTPTVW4zHpkByOboAqZj12UuYSsG3GEhafpt91ThFhs7UTtqN7F29UsSW2ikIjTgFPy8cOddclinOtUwaoMaFk2OspLF3J9cwr7wPsZ9CpQxU21mcFHxqpz7vZuGrjWqepKQhWX_ZzmHv0LR8K07ZJLu8yl51iv-Ram7er9lKfWDtQsuNeLqbzEOQo0UlRNexaV0V2m8fYke8ubw3kNeR5XsRYiyr958OFwNgZ3RNfy-mNnO9P-4TFEF12NmNNEm4N6h0_DRZ-g74n-X2nGwx9emPv4wuy9kvQGeoCqc636BfKRE-51w2GFSrHAsOUJJ1dDryxZsxQOEGep3HGrVp_rTsVv7Vk3JxKxlzqt3hnBGDgi6suTZnJw69poVOIz6TPCTthRhj7XUu4heyKBSIeHsjBRC2_s3NwuZ4kKNCQ2JkVuBXz_hsRhDmbAnBi6WUFIJhLHO_bGgKbEASuU4vtj4FNKo_G8p-J1kYmCo0Pi72Csi3EikuocfjHFwfSD3cCbetr3V8Yp6OmSGkqX63FkSqzBoAcHFeD-iyCAkn0UJGqU-0o670ZoR-twkUDcSJPXDN2NYQfqiyb9ZknZ7j04w1ZfAyaE7NCiCc-lDt1ic79XyHunjOyLStgXIW30J4OEw_hAn86LlRHbYVhi-zBBTZWWnEl9piuUz0qtnN-qEd002DjNYaMy0aDAbL9oOYDdN8mHvnXq1aKove9I4Jy0WtlxeN8279ayz7NdDZZ9LrajY_YxIJJqdZtJIuRYTunEeDsFrORpu3RYRbFwpGnQbHeSLH1YvwOyOJRXhYYmVLJEGD2N9r5wkPbgbx2HoWsGjWj_DpkEAyg59eBJy4RYPJHvOsetBQABEWmGI7nhUDYTPdhrzVxqB_g4fQ9JkPzIbEhcoEZjmspGZcR4z4JxUDJCNdAz2aK4lR4P5WTkLtj2uXMDD_nzbl8r_DMcj23bjPiSe0Fubu-VIzjwr7JgPNyQ1FYhp5u4lpqkkBkGtfyAaUjCgFhg4FW-H3d3vPVMO--GxbhK9kN0QAcOE3ZqQR2dRz6NbhcvTyNfDxy0dFTRw-f-vxn04gjJB5ZEG3WfSzQv0VbqDYm6-NFYAzIxbDLoiCu34WAa2lckx5qxncXBhQj6Fro2gXGPXo4d32DvqQg7_RHQ-SF_WLqdxRCXF91NIqxYmFZsOJAuQ5m6TafzuNnQoJB3OQFoknv8Uy5O4FKuwazh1rvLrsj-1QEMi3sTrr9KxJkZy9EKXs92ndlb3edgfycLOffTil-gW2BvxeNiMQzqF1xJqFBKHDyatgwpXDX81HDwxkuMEaGPREIeQLuOlBJrL_20RD1e4Gu4tjQD8vRsb29UNG60DqpDvc-H4Z2oxeppm0KIwQNaCTtGUxxmvT807fXMnuVEf5QI5qTx9YRJh56GiWLoHC_zPMhoikMbAybIVWh9HtVgZGgImDmz0l9P4LgtpKNnKbQj_2ZKn2ZhOYKZLdt1P2Jq2Z2z76MtbRQTrpZpFb14zWVnh1LFCSFPAB7sqC1-u-KQOf2_SjEecztPccso8xZB2nkhLetyPn9aFuO-J_LCZydQeiroXx4Z8NxhDpbLoOpw2MbRCVB_TxfnLGNn1QD0To9TTChxK5AHNRRLDaj3xK1e0jd37uSmHTkT6QJVHFHEYMVLBcuV1MQcoy0wsvc1sRb",null],"logging":{"composer_session_id":"'+str(uuid.uuid4())+'"},"navigation_data":{"attribution_id_v2":"FeedsCometRoot.react,comet.most_recent_feed,tap_bookmark,1719641912186,189404,608920319153834,,"},"event_share_metadata":{"surface":"newsfeed"},"actor_id":"'+self.actor_id+'","client_mutation_id":"3"},"feedLocation":"NEWSFEED","feedbackSource":1,"focusCommentID":null,"gridMediaWidth":null,"groupID":null,"scale":1,"privacySelectorRenderLocation":"COMET_STREAM","checkPhotosToReelsUpsellEligibility":false,"renderLocation":"homepage_stream","useDefaultActor":false,"inviteShortLinkKey":null,"isFeed":true,"isFundraiser":false,"isFunFactPost":false,"isGroup":false,"isEvent":false,"isTimeline":false,"isSocialLearning":false,"isPageNewsFeed":false,"isProfileReviews":false,"isWorkSharedDraft":false,"hashtag":null,"canUserManageOffers":false,"__relay_internal__pv__CometIsAdaptiveUFIEnabledrelayprovider":true,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__IncludeCommentWithAttachmentrelayprovider":true,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":true,"__relay_internal__pv__StoriesRingrelayprovider":false,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":false}',
            'server_timestamps': 'true',
            'doc_id': '8167261726632010'
        }
        response = requests.post("https://www.facebook.com/api/graphql/",headers=self.headers, data=data, proxies=self.proxies)
        if '"errors"' not in response.text:
            return True
        else:
            return False
        
    def like_page(self, id):
        data = {
            'av': self.actor_id,
            '__aaid': '0',
            '__user': self.actor_id,
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
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'lsd': self.lsd,
            '__spin_r': '1018088939',
            '__spin_b': 'trunk',
            '__spin_t': '1731303639',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometProfilePlusLikeMutation',
            'variables': '{"input":{"is_tracking_encrypted":false,"page_id":"'+str(id)+'","source":null,"tracking":null,"actor_id":"'+str(self.actor_id)+'","client_mutation_id":"1"},"scale":1}',
            'server_timestamps': 'true',
            'doc_id': '6716077648448761',
        }
        response = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data, proxies=self.proxies)
        if '"subscribe_status":"IS_SUBSCRIBED"' in response.text:
            return True
        else:
            return False
    
    def group(self, id):
        data = {
            'av': self.actor_id,
            '__user': self.actor_id,
            '__a': '1',
            '__dyn': '7AzHJ16U9ob8ng5K8G6EjBWo2nDwAxu13wsongS3q2ibwyzE2qwJyEiwsobo6u3y4o2Gwfi0LVEtwMw65xO321Rwwwg8a8465o-cwfG12wOKdwGxu782lwv89kbxS2218wc61axe3S1lwlE-U2exi4UaEW2G1jxS6FobrwKxm5oe8464-5pUfEe88o4Wm7-8xmcwfCm2CVEbUGdG1Fwh888cA0z8c84qifxe3u364UrwFg662S26',
            '__csr': 'gadNAIYllhsKOE8IpidFPhcIx34Omy9-O9OO8hZ_8-kAymHGAybJqGlvmWl7nWBWJ7GqaXHz7GFe9oy_KBl7h6h4KVah94QeKVHACDyryqKdF5GuXXBCgNpbJ5jjGm8yQEWrCixl6xWuiih5yo-8wAy84mq4poN0Vzbxe16whAufgO5U8UKi4Eyu4EjwGK78527o8411wgocU5u1MwSwFyU8Uf8igaElw8e9xK2GewNgy5o5m1nDwLwrokm16www8G03cy0arw0Zyw0aaC0mG0eJzl8ow2Jw6tw44w4uzo045W1UgSeg0z-07X81-E0cNo0By1Wwi8fE0lYw2h81a8gw9u',
            '__req': 'k',
            '__hs': '19363.HYP:comet_pkg.2.1.0.2.1',
            'dpr': '2',
            '__ccg': 'EXCELLENT',
            '__rev': '1006794317',
            '__s': 'gtlvj8:fxbzro:f2kk19',
            '__hsi': '7185658639628512803',
            '__comet_req': '15',
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'lsd': self.lsd,
            '__aaid': '1576489885859472',
            '__spin_r': '1006794317',
            '__spin_b': 'trunk',
            '__spin_t': '1673041526',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
            'variables': '{"feedType":"DISCUSSION","groupID":"'+id+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1673041528761,114928,2361831622,","group_id":"'+id+'","group_share_tracking_params":{"app_id":"2220391788200892","exp_id":"null","is_from_share":false},"actor_id":"'+self.actor_id+'","client_mutation_id":"1"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":true,"scale":2,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true,"__relay_internal__pv__GlobalPanelEnabledrelayprovider":false}',
            'server_timestamps': 'true',
            'doc_id': '5853134681430324',
            'fb_api_analytics_tags': '["qpl_active_flow_ids=431626709"]',
        }
        response = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data, proxies=self.proxies)
        if self.actor_id in response.text:
            return True
        else:
            return False
    
    def follow(self, id):
        data = {
            'av': self.actor_id,
            '__aaid': '0',
            '__user': self.actor_id,
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
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'lsd': self.lsd,
            '__spin_r': '1014584891',
            '__spin_b': 'trunk',
            '__spin_t': '1719764873',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometUserFollowMutation',
            'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,unexpected,1719765181042,489343,250100865708545,,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,unexpected,1719765155735,648442,391724414624676,,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,tap_search_bar,1719765153341,865155,391724414624676,,","is_tracking_encrypted":false,"subscribe_location":"PROFILE","subscribee_id":"'+str(id)+'","tracking":null,"actor_id":"'+str(self.actor_id)+'","client_mutation_id":"5"},"scale":1}',
            'server_timestamps': 'true',
            'doc_id': '25581663504782089',
        }
        response = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data, proxies=self.proxies)
        if '"subscribe_status":"IS_SUBSCRIBED"' in response.text:
            return True
        else:
            return False
        
class NextCaptcha:
    def __init__(self, apikey):
        self.apikey = apikey
        self.create_task_url = "https://api.3xcaptcha.com/createTask"
        self.get_result_url = "https://api.3xcaptcha.com/getTaskResult"

    def recaptchav2(self, sitekey, siteurl):
        data = {
            "clientKey": self.apikey,
            "task": {
                "type": "RecaptchaV2TaskProxyless",
                "websiteURL": siteurl,
                "websiteKey": sitekey
            }
        }
        try:
            response = requests.post(self.create_task_url, json=data, timeout=10).json()
            if response.get("errorId", 0) != 0:
                print(f"Lỗi tạo task: {response}")
                return False, None
            return True, response.get("taskId")
        except requests.RequestException as e:
            print(f"Lỗi khi gửi yêu cầu tạo task: {e}")
            return False, None

    def get_result(self, task_id, max_retries=10, delay=0):
        data = {
            "clientKey": self.apikey,
            "taskId": task_id
        }
        
        for x in range(max_retries):
            try:
                response = requests.post(self.get_result_url, json=data, timeout=10).json()
                if response.get("errorId", 0) != 0:
                    print(f"Lỗi lấy kết quả: {response}")
                    return False, None
                if response.get("status") == "ready":
                    return True, response["solution"]["gRecaptchaResponse"]
                sleep(delay)
            except requests.RequestException as e:
                print(f"Lỗi khi lấy kết quả Captcha: {e}")
                return False, None
        
        print("Hết số lần thử, không có kết quả.")
        return False, None

class TraoDoiSub_Api(object):
    def __init__(self, username, password, proxy=None) -> None:
        self.username = username
        self.password = password
        self.proxies = None
        self.session = requests.Session()
        self.headers = {'authority': 'traodoisub.com', 'accept': 'application/json, text/javascript, */*; q=0.01', 'cache-control': 'max-age=0', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://traodoisub.com', 'referer': 'https://traodoisub.com/', 'x-requested-with': 'XMLHttpRequest'}
        if proxy:
            try:
                proxy_parts = proxy.strip().split(':')
                if len(proxy_parts) == 4:
                    host, port, user, password = proxy_parts
                    self.proxies = {
                        'http': f'http://{user}:{password}@{host}:{port}',
                        'https': f'http://{user}:{password}@{host}:{port}'
                    }
            except Exception as e:
                print(f"Lỗi khởi tạo proxy: {str(e)}")
                self.proxies = None
    
    def info(self):
        response = self.session.post('https://traodoisub.com/scr/login.php', headers=self.headers, data={'username': self.username, 'password': self.password}, proxies=self.proxies)
        if 'success' in response.text:
            self.cookie = response.headers['Set-cookie']
            headers = {
                'authority': 'traodoisub.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9',
                'cookie': self.cookie,
                'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
                'x-requested-with': 'XMLHttpRequest',
            }
            response = self.session.get('https://traodoisub.com/view/setting/load.php', headers=headers).json()
            self.token = response['tokentds']
            self.xu = response['xu']
            self.name = response['user']
            return True, self.name, self.xu, self.token
        else:
            return False, None
        
    def facebook_configuration(self, id):
        try:
            response = self.session.post('https://traodoisub.com/scr/datnick.php', headers=self.headers, data={'iddat': id}, proxies=self.proxies).text
            return True if '1' in response else False
        except:
            return False

    def add_uid(self, id, g_recaptcha_response):
        headers = {
            'authority': 'traodoisub.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': self.cookie,
            'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
            'x-requested-with': 'XMLHttpRequest',
        }
        response = self.session.post('https://traodoisub.com/scr/add_uid.php', headers=headers, data={'idfb': id, 'g-recaptcha-response': g_recaptcha_response}, proxies=self.proxies).text
        if 'success' in response:
            return True, None
        elif 'error' in response:
            return False, response
        else:
            return response

    def get_g_recaptcha_response(self, apikey):
        try:
            response = requests.get('https://traodoisub.com/view/cauhinh/', headers=self.headers, proxies=self.proxies)
            if response.status_code != 200:
                print("Lỗi khi lấy sitekey!")
                return False, None
            sitekey = response.text.split('data-sitekey="')[1].split('"')[0]
            captcha_solver = NextCaptcha(apikey)
            success, task_id = captcha_solver.recaptchav2(sitekey, 'https://traodoisub.com/view/cauhinh/')
            if success:
                success, g_recaptcha_response = captcha_solver.get_result(task_id)
                if success:
                    return True, g_recaptcha_response
        except:
            return False, 'Lỗi khi lấy reCAPTCHA'
        
    def get_nv_vip(self, fields, type):
        try:
            list_nv = self.session.get(f'https://traodoisub.com/api/?fields={fields}&access_token={self.token}&type={type}', proxies=self.proxies).json()
            return list_nv
        except:
            return False
    
    def get_nv_thuong(self, fields):
        try:
            list_nv = self.session.get(f'https://traodoisub.com/api/?fields={fields}&access_token={self.token}', proxies=self.proxies).json()
            return list_nv
        except:
            return False
    
    def get_xu_vip(self, type, id):
        try:
            get_xu = self.session.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}', proxies=self.proxies).json()
            return get_xu
        except:
            return False
    
    def get_xu_thuong(self, type, id):
        try:
            get_xu = self.session.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}', proxies=self.proxies).json()
            return get_xu
        except:
            return False
        
    def cache(self, type, id):
        try:
            cache = self.session.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}', proxies=self.proxies).json()
            return cache
        except:
            return False

def Nhap_Cookie():
    demck = 0
    while True:
        demck += 1
        ck = input(f'{thanh} {luc}Nhập Cookie Facebook Thứ {vang}{demck}{trang}: ')
        if ck == '' and demck > 1:
            break
        fb = Facebook_Api(ck)
        info = fb.info()
        if 'success' in info:
            name = info['name']
            uid = info['id']
            thanhngang(70)
            print(f'{thanh} {luc}Id Facebook{trang}: {vang}{uid} {red}| {luc}Tên Tài Khoản{trang}: {vang}{name}')
            listck.append(ck)
            thanhngang(70)
        else:
            thanhngang(70)
            print(f'''{thanh} {luc}Trạng Thái Acc{trang}: {trang}[{red}DIE{trang}]\n{thanh} {luc}Tin Nhắn{trang}: {luc}Đăng Nhập Thất Bại''')
            demck-=1
            thanhngang(70)
    return listck

def Nhap_Setting():
    apikey = input(f'{thanh} {luc}Nhập Apikey 3xcaptcha Để Auto Add Cấu Hình (Enter để bỏ qua nếu kh có){trang}: {vang}')
    min = int(input(f'{thanh} {luc}Nhập Delay Min{trang}: {vang}'))
    max = int(input(f'{thanh} {luc}Nhập Delay Max{trang}: {vang}'))
    nvblock = int(input(f'{thanh} {luc}Sau Bao Nhiêu Job Thì Chống Block{trang}: {vang}'))
    delaybl = int(input(f'{thanh} {luc}Sau {vang}{nvblock} {luc}Job Thì Nghỉ Ngơi{trang}: {vang}'))
    doinick = int(input(f'{thanh} {luc}Sau Bao Nhiêu Job Thì Đổi Nick{trang}: {vang}'))
    nhiemvuloi = int(input(f'{thanh} {luc}Lỗi Bao Nhiêu Nhiệm Vụ Thì Xóa Cookie{trang}: {vang}'))
    config = {
        "apikey": apikey,
        "min": min,
        "max": max,
        "nvblock": nvblock,
        "delaybl": delaybl,
        "doinick": doinick,
        "nhiemvuloi": nhiemvuloi
    }
    with open('settingch.json', 'w') as f:
        json.dump(config, f)
    return config

def Main():  
    ptool = 0
    dem = 0
    count = 0
    banner()
    print(f'{thanh} {luc}Proxy Dạng{trang}: {vang}username:password@host:port')
    print(red+"-"*70)
    filename = input(f"{thanh} {luc}Nhập File Txt Chứa Proxy (Enter để bỏ qua){trang}: ")
    print(red+"-"*70)
    proxy_list = read_proxy_file(filename)
    proxy_index = 0
    current_proxy = 0
    myip = None
    if proxy_list:
        current_proxy = proxy_list[proxy_index]
        proxy_index = (proxy_index + 1) % len(proxy_list)
        username, password = current_proxy.split('@')[1].split(':')
        host, port = current_proxy.split('@')[0].split(':')
        data = {
            'listProxy': [
                {
                    'username': username,
                    'password': password,
                    'host': host,
                    'port': port
                }
            ]
        }
        check = requests.post('https://api.proxymart.net/api/check-proxy',json=data).json()
        is_live = check['data'][0]['isLive']
        if is_live == False:
            print(f'{luc}Proxy Không Hoạt Động!                            ', end = '\r');sleep(0); print('                                                        ', end = '\r')
            myip = None
        else:
            print(f'{luc}Proxy Hoạt Động!                            ', end = '\r');sleep(0); print('                                                        ', end = '\r')
            myip = check['data'][0]['ip']
    banner()
    while True:
        if os.path.exists('acc_tds_log.txt'):
            with open('acc_tds_log.txt', 'r') as f:
                username, password = f.read().split('_')
            tds = TraoDoiSub_Api(username, password, current_proxy)
            profile = tds.info()
            try:
                print(f'{thanh} {luc}Nhập {red}[{vang}1{red}] {luc}Để Chạy Acc Tài Khoản {vang}{profile[1]}')
                print(f'{thanh} {luc}Nhập {red}[{vang}2{red}] {luc}Nhập Tài Khoản Trao Đổi Sub Mới')
                thanhngang(70)
                chon = input(f'{thanh} {luc}Nhập{trang}: ')
                thanhngang(70)
                if chon == '2':
                    os.remove('acc_tds_log.txt')
                elif chon == '1':
                    pass
		    # Hiệu ứng tải
                    for i in range(1, 101):
                     sys.stdout.write(f"\r{BOLD}{LIME}ĐANG LOADING: {i}% {'█' * (i // 5)}{RESET}")
                     sys.stdout.flush()
                     sleep(0.003)  # Điều chỉnh thời gian chờ nếu cần
                else:
                    print(f'{thanh} {red}Vui Lòng Chọn Đúng')
                    thanhngang(70)
                    continue
            except:
                print(f'''{thanh} {luc}Trạng Thái Acc{trang}: {trang}[{red}DIE{trang}]\n{thanh} {luc}Tin Nhắn{trang}: {luc}Đăng Nhập Thất Bại''')
                os.remove('acc_tds_log.txt')
        if not os.path.exists('acc_tds_log.txt'):
            username, password = input(f'{thanh} {luc}Nhập Tài Khoản TDS{trang}: '), input(f'{thanh} {luc}Nhập Mật Khẩu TDS{trang}: ')
            thanhngang(70)
            with open('acc_tds_log.txt', 'w') as f:
                f.write(f'{username}_{password}')
        with open('acc_tds_log.txt', 'r') as f:
            username, password = f.read().split('_')
        tds = TraoDoiSub_Api(username, password, current_proxy)
        profile = tds.info()
        try:
            user = profile[1]
            xu = profile[2]
            print(f'''{thanh} {luc}Trạng Thái Acc{trang}: {trang}[{luc}Acc còn sống{trang}]\n{thanh} {luc}Tin Nhắn{trang}: {luc}Đăng Nhập Thành Công''')
            break
        except:
            print(f'''{thanh} {luc}Trạng Thái Acc{trang}: {trang}[{red}Bị fb cho cút{trang}]\n{thanh} {luc}Tin Nhắn{trang}: {do}Đăng Nhập Thất Bại''')
            thanhngang(70)
            os.remove('acc_tds_log.txt')
    thanhngang(70)
    while True:
        if os.path.exists('cookiefb.txt'):
            print(f'{thanh} {luc}Nhập {red}[{vang}1{red}] {luc}Để log cookie fb cũ 🔫')
            print(f'{thanh} {luc}Nhập {red}[{vang}2{red}] {luc}Để thay cookie mới 🔫')
            thanhngang(70)
            chon = input(f'{thanh} {luc}Nhập{trang}: ')
            thanhngang(70)
            if chon == '1':
                print(f'{luc}Đang Lấy Dữ Liệu Đã Lưu...')
		    # Hiệu ứng tải
                for i in range(1, 101):
                 sys.stdout.write(f"\r{BOLD}{LIME}ĐANG LOADING: {i}% {'█' * (i // 5)}{RESET}")
                 sys.stdout.flush()
                 sleep(0.003)  # Điều chỉnh thời gian chờ nếu cần
                with open('cookiefb.txt', 'r') as f:
                    listck = json.loads(f.read())
                    break
            elif chon == '2':
                os.remove('cookiefb.txt')
            else:
                print(f'{thanh} {red}Mù à?Nhập lại')
                thanhngang(70)
                continue
        if not os.path.exists('cookiefb.txt'):
            listck = Nhap_Cookie()
            with open('cookiefb.txt', 'w') as f:
                json.dump(listck, f)
            break
    banner()
    print(f'{thanh} {luc}Tên Tài khoản TDS{trang}: {vang}{user}')
    print(f'{thanh} {luc}Xu Hiện Tại Đang Có{trang}: {vang}{str(format(int(xu),","))}')
    print(f'{thanh} {luc}Số Cookie Facebook Đã Nhập{trang}: {vang}{len(listck)}')
    print(f'{thanh} {luc}Trạng Thái Proxy{trang}: {vang}{myip}')
    thanhngang(70)
    print(f'{thanh} {luc}Nhập {red}[{vang}1{red}] {luc}Để Chạy Job REACTIONXUCAO')
    print(f'{thanh} {luc}Nhập {red}[{vang}2{red}] {luc}Để Chạy Job REACTIONCMT')
    print(f'{thanh} {luc}Nhập {red}[{vang}3{red}] {luc}Để Chạy Job SHAREXUCAO')
    print(f'{thanh} {luc}Nhập {red}[{vang}4{red}] {luc}Để Chạy Job FOLLOWXUCAO')
    print(f'{thanh} {luc}Nhập {red}[{vang}5{red}] {luc}Để Chạy Job LIKEPAGECAO')
    print(f'{thanh} {luc}Nhập {red}[{vang}6{red}] {luc}Để Chạy Job GROUPXUCAO')
    print(f'{thanh} {luc}Nhập {red}[{vang}7{red}] {luc}Để Chạy Job SHARETHUONG')
    print(f'{thanh} {luc}Nhập {red}[{vang}8{red}] {luc}Để Chạy Job LIKEPAGETHUONG')
    print(f'{thanh} {luc}Nhập {red}[{vang}9{red}] {luc}Để Chạy Job LIKETHUONG')
    print(f'{thanh} {luc}Nhập {red}[{vang}0{red}] {luc}Để Chạy Job REACTIONTHUONG')
    print(f'{thanh} {lam}Có Thể Chọn Nhiều Nhiệm Vụ (Ví Dụ: 123...)')
    thanhngang(70)
    nhap = input(f'{thanh} {luc}Nhập Số Để Chọn JOB {luc}: ')
    if '' in nhap:
        nhap = nhap.replace('','')
    listnv.append(nhap)
    thanhngang(70)
    if os.path.exists('settingch.json'):
        with open('settingch.json', 'r') as f:
            config = json.load(f)
            apikey = config['apikey']
            min = config['min']
            max = config['max']
            nvblock = config['nvblock']
            delaybl = config['delaybl']
            doinick = config['doinick']
            nhiemvuloi = config['nhiemvuloi']
            print(f'{thanh} {luc}Đã Thấy Cấu Hình Cũ')
            print(f'{thanh} {luc}Api Key 3xCapcha{trang}: {vang}{apikey}')
            print(f'{thanh} {luc} Min{trang}: {vang}{min}')
            print(f'{thanh} {luc} Max{trang}: {vang}{max}')
            print(f'{thanh} {luc}Sau {vang}{nvblock} {luc} Job Thì Chống Block')
            print(f'{thanh} {luc}Sau {vang}{nvblock} {luc} Job Thì Nghỉ Ngơi {vang}{delaybl}')
            print(f'{thanh} {luc}Sau {vang}{doinick} {luc} Job Thì Đổi Nick')
            print(f'{thanh} {luc}Lỗi {vang}{nhiemvuloi} {luc}Bao Nhiêu Job Thì Đổi Job Khác')
        chon = input(f'{thanh} {luc}Bạn Có Muốn Sử Dụng Cấu Hình Lúc Trước? {red}({vang}y/n{red}){trang}: {vang}')
        if chon == 'y':
            apikey = config['apikey']
            min = config['min']
            max = config['max']
            nvblock = config['nvblock']
            delaybl = config['delaybl']
            doinick = config['doinick']
            nhiemvuloi = config['nhiemvuloi']
        else:
            print(f'{thanh} {luc}Đã Xóa Cấu Hình Cũ')
            thanhngang(70)
            os.remove('settingch.json')
            config = Nhap_Setting()
            apikey = config['apikey']
            min = config['min']
            max = config['max']
            nvblock = config['nvblock']
            delaybl = config['delaybl']
            doinick = config['doinick']
            nhiemvuloi = config['nhiemvuloi']
    else:
        config = Nhap_Setting()
        apikey = config['apikey']
        min = config['min']
        max = config['max']
        nvblock = config['nvblock']
        delaybl = config['delaybl']
        doinick = config['doinick']
        nhiemvuloi = config['nhiemvuloi']
    chonan = input(f'{thanh} {luc}Bạn Muốn Ẩn ID Fb Không?{red}({vang}y/n{red}){trang}: {vang}')
    thanhngang(70)
    while True:
        if len(listck) == 0:
            print(f'{red}Đã Xoá Tất Cả Cookie Do Cookie Die Hoặc Acc Ch Thêm Cấu Hình, Vui Lòng Nhập Lại Cookie Mới')
            listck = Nhap_Cookie()
            with open('Cookie_FB.txt', 'w') as f:
                json.dump(listck, f)
        for ck in listck:
            nhiemvu = listnv[0]
            loireaction, loicxcmt, loishare, loifollow, loipage, loigr, loilike, loiliket, loisharet, loiliket = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            proxy_list = read_proxy_file(filename)
            proxy_index = 0
            current_proxy
            myip = None
            if proxy_list:
                current_proxy = proxy_list[proxy_index]
                proxy_index = (proxy_index + 1) % len(proxy_list)
                username, password = current_proxy.split('@')[0].split(':')
                host, port = current_proxy.split('@')[1].split(':')
                data = {
                    'listProxy': [
                        {
                            'username': username,
                            'password': password,
                            'host': host,
                            'port': int(port)
                        }
                    ]
                }
                check = requests.post('https://api.proxymart.net/api/check-proxy',json=data).json()
                is_live = check['data'][0]['isLive']
                if is_live == False:
                    print(f'{luc}Proxy Không Hoạt Động!                            ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                    myip = None
                else:
                    print(f'{luc}Proxy Hoạt Động!                            ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                    myip = check['data'][0]['ip']
            fb = Facebook_Api(ck, current_proxy)
            info = fb.info()
            if 'success' in info:
                name = info['name']
                uid = info['id']
            else:
                uid = ck.split('c_user=')[1].split(';')[0]
                print(f'{red}Cookie Tài Khoản {uid} Bị Mark Cho Cút', end='\r');sleep(0); print('                                     ', end = '\r' )
                listck.remove(ck)
                continue
            if chonan == 'y':
                uid2 = uid[:4]+'#'*(len(uid)-6)+uid[-4:]
            else:
                uid2 = uid
            cauhinh = tds.facebook_configuration(uid)
            if cauhinh == True:
                print(f'{luc}Id FB{trang}: {vang}{uid2} {red}| {luc}Tên FB{trang}: {vang}{name}')
            else:
                if apikey:
                    print(f'{luc}Đang Thêm Id FB{trang}: {vang}{uid} {red}| {luc}Tên FB{trang}: {vang}{name}')
                    get_g_recaptcha_response = tds.get_g_recaptcha_response(apikey)
                    if get_g_recaptcha_response[0] == True:
                        # print(f"DEBUG: Kết quả reCAPTCHA: {get_g_recaptcha_response}")
                        add_uid = tds.add_uid(uid, get_g_recaptcha_response[1])
                        if add_uid[0] == True:
                            cauhinh = tds.facebook_configuration(uid)
                            if cauhinh == True:
                                print(f'{luc}Id FB{trang}: {vang}{uid2} {red}| {luc}Tên FB{trang}: {vang}{name}')
                            else:
                                print(f'{luc}Cấu Hình Đéo Dc Id FB{trang}: {vang}{uid} {red}| {luc}Tên FB {trang}: {vang}{name}')
                                listck.remove(ck)
                                continue
                        else:
                            print(f'{luc}Thêm Cấu Hình Đéo Dc Id FB{trang}: {vang}{uid} {red}| {luc}Tên FB {trang}: {vang}{name}')
                            listck.remove(ck)
                            continue
                    else:
                        print(f'{luc}Thêm Cấu Hình Đéo Dc Id FB{trang}: {vang}{uid} {red}| {luc}Tên FB {trang}: {vang}{name}')
                        listck.remove(ck)
                        continue
                else:
                    print(f'{luc}Cấu Hình Đéo Đc Id FB{trang}: {vang}{uid} {red}| {luc}Tên FB{trang}: {vang}{name}')
                    listck.remove(ck)
                    continue
            ptool = 0
            while True:
                if ptool == 1:
                    break

                if nhiemvu == '':
                    print(f'{red}Tài Khoản {vang}{name} {red}Đã Bị Mark Block Full, Nuôi Dc Rồi!{red}')
                    listck.remove(ck)
                    ptool = 1
                    break

                if '1' in nhiemvu:
                    listcx = tds.get_nv_vip('facebook_reaction', 'ALL')
                    if listcx == False:
                        print(f'{luc}Không Get Được Nhiệm Vụ Cảm Xúc                           ', end = '\r');sleep(2); print('                                                        ', end = '\r')
                    elif 'error' in listcx:
                        if listcx['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listcx['countdown']
                            print(f'{luc}Đang Get Nhiệm Vụ {vang}Cảm Xúc, {luc}COUNTDOWN: {str(round(count, 3))}              ', end = '\r'); sleep(0); print('                                                       ', end = '\r')
                            Delay(count)
                        else:
                            print(listcx['error'], end = '\r'); sleep(0); print('                                                       ', end = '\r')
                    else:
                        list_nv = listcx['data']
                        if len(list_nv) == 0:
                            print(f'{luc}Cạn Bà Nhiệm Vụ Cảm Xúc Rồi...                         ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                        else:
                            print(f'{luc}Tìm Thấy {vang}{len(list_nv)} {luc}Nhiệm Vụ Cảm Xúc  🤑💸🔫                   ', end = '\r')
                            for x in list_nv:
                                idpost = x['id']
                                id = idpost.split('_')[1] if '_' in idpost else idpost
                                id2 = id[:3]+'#'*(len(id)-6)+id[-3:]
                                code = x['code']
                                type = x['type']
                                like = fb.reaction(id, type)
                                if like == False:
                                    print(f"{luc}FAIL {lam}{type}{trang}: {vang}{id}            ", end = '\r'); sleep(0); print('                                                       ', end = '\r')
                                    Delay(0)
                                    loireaction += 1
                                else:
                                    nhan = tds.get_xu_vip('facebook_reaction', code)
                                    if 'success' in nhan:
                                        xu = nhan['data']['xu']
                                        msg = nhan['data']['msg']
                                        loireaction = 0
                                        dem+=1
                                        time = datetime.now().strftime("%H:%M:%S")
                                        print(f'{red}[{trang}{dem}{red}][{lam}{time}{red}][{vang}{type}{red}][{trang}{id2}{red}][{luc}{msg}{red}][{vang}{str(format(int(xu),","))}{red}][{trang}{myip}{red}]')
                                        if dem % doinick == 0:
                                            ptool = 1
                                            break
                                        if dem % nvblock == 0:
                                            Delay(delaybl)
                                        else:
                                            Delay(randint(min, max))

                                if loireaction >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(f'{red}Cookie Tài Khoản {vang}{name} {red}Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(f'{red}Tài Khoản {vang}{name} {red}Đã Bị Bé Mark Cho Block {vang}Cảm Xúc:(( {red}                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                                        nhiemvu = nhiemvu.replace('1','')
                                        break
                
                if ptool == 1:
                    break

                if '2' in nhiemvu:
                    listcxcmt = tds.get_nv_vip('facebook_reactioncmt', 'ALL')
                    if listcxcmt == False:
                        print(f'{luc}Không Get Được Nhiệm Vụ Cảm Xúc Cmt                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                    elif 'error' in listcxcmt:
                        if listcxcmt['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listcxcmt['countdown']
                            print(f'{luc}Đang Get Nhiệm Vụ {vang}Follow, {luc}COUNTDOWN: {str(round(count, 3))}              ', end = '\r'); sleep(0); print('                                                       ', end = '\r')
                            Delay(count)
                        else:
                            print(listcxcmt['error'], end = '\r'); sleep(0); print('                                                       ', end = '\r')
                    else:
                        list_nv = listcxcmt['data']
                        if len(list_nv) == 0:
                            print(f'{luc}Cạn Bà Nhiệm Vụ Cảm Xúc Cmt  Rồi                        ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                        else:
                            print(f'{luc}Tìm Thấy {vang}{len(list_nv)} {luc}Nhiệm Vụ Cảm Xúc Cmt  🤑💸🔫                   ', end = '\r')
                            for x in list_nv:
                                idpost = x['id']
                                id = idpost.split('_')[1] if '_' in idpost else idpost
                                id2 = id[:3]+'#'*(len(id)-6)+id[-3:]
                                code = x['code']
                                type = x['type']
                                like = fb.reactioncmt(id, type)
                                if like == False:
                                    print(f"{luc}FAIL {lam}{type}CMT{trang}: {vang}{id}            ", end = '\r'); sleep(0); print('                                                       ', end = '\r')
                                    Delay(0)
                                    loicxcmt += 1
                                else:
                                    nhan = tds.get_xu_vip('facebook_reactioncmt', code)
                                    if 'success' in nhan:
                                        xu = nhan['data']['xu']
                                        msg = nhan['data']['msg']
                                        loicxcmt = 0
                                        dem+=1
                                        time = datetime.now().strftime("%H:%M:%S")
                                        print(f'{red}[{trang}{dem}{red}][{lam}{time}{red}][{vang}{type}CMT{red}][{trang}{id2}{red}][{luc}{msg}{red}][{vang}{str(format(int(xu),","))}{red}][{trang}{myip}{red}]')
                                        if dem % doinick == 0:
                                            ptool = 1
                                            break
                                        if dem % nvblock == 0:
                                            Delay(delaybl)
                                        else:
                                            Delay(randint(min, max))

                                if loicxcmt >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(f'{red}Cookie Tài Khoản {vang}{name} {red}Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(f'{red}Tài Khoản {vang}{name} {red}Đã Bị Bé Mark Cho Block {vang}Cảm Xúc Cmt:(( {red}                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                                        nhiemvu = nhiemvu.replace('2','')
                                        break

                if ptool == 1:
                    break

                if '3' in nhiemvu:
                    listshare = tds.get_nv_vip('facebook_share', 'ALL')
                    if listshare == False:
                        print(f'{luc}Không Get Được Nhiệm Vụ Share                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                    elif 'error' in listshare:
                        if listshare['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listshare['countdown']
                            print(f'{luc}Đang Get Nhiệm Vụ {vang}Share, {luc}Bú coundown đi e : {str(round(count, 3))}              ', end = '\r'); sleep(0); print('                                                       ', end = '\r')
                            Delay(count)
                        else:
                            print(listshare['error'], end = '\r'); sleep(0); print('                                                       ', end = '\r')
                    else:
                        list_nv = listshare['data']
                        if len(list_nv) == 0:
                            print(f'{luc}Hết Nhiệm Vụ Share                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                        else:
                            print(f'{luc}Tìm Thấy {vang}{len(list_nv)} {luc}Nhiệm Vụ Share  🤑💸🔫                  ', end = '\r')
                        for x in list_nv:
                            idpost = x['id']
                            id = idpost.split('_')[1] if '_' in idpost else idpost
                            id2 = id[:3]+'#'*(len(id)-6)+id[-3:]
                            code = x['code']
                            like = fb.share(id)
                            if like == False:
                                print(f"{luc}FAIL {lam}SHARE{trang}: {vang}{id}            ", end = '\r'); sleep(0); print('                                                       ', end = '\r')
                                Delay(0)
                                loishare += 1
                            else:
                                nhan = tds.get_xu_vip('facebook_share', code)
                                if 'success' in nhan:
                                    xu = nhan['data']['xu']
                                    msg = nhan['data']['msg']
                                    loishare = 0
                                    dem+=1
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(f'{red}[{trang}{dem}{red}][{lam}{time}{red}][{vang}SHARE{red}][{trang}{id2}{red}][{luc}{msg}{red}][{vang}{str(format(int(xu),","))}{red}][{trang}{myip}{red}]')
                                    if dem % doinick == 0:
                                        ptool = 1
                                        break
                                    if dem % nvblock == 0:
                                        Delay(delaybl)
                                    else:
                                        Delay(randint(min, max))

                                if loishare >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(f'{red}Cookie Tài Khoản {vang}{name} {red}Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(f'{red}Tài Khoản {vang}{name} {red}Đã Bị Bé Mark Cho Block{vang}Share:(( {red}                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                                        nhiemvu = nhiemvu.replace('3','')
                                        break

                if ptool == 1:
                    break

                if '4' in nhiemvu:
                    listfl = tds.get_nv_vip('facebook_follow', '')
                    if listfl == False:
                        print(f'{luc}Không Get Được Nhiệm Vụ Follow                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                    elif 'error' in listfl:
                        if listfl['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listfl['countdown']
                            print(f'{luc}Đang Get Nhiệm Vụ {vang}Follow, {luc}Bú countdown đi e: {str(round(count, 3))}              ', end = '\r'); sleep(0); print('                                                       ', end = '\r')
                            Delay(count)
                        else:
                            print(listfl['error'], end = '\r'); sleep(0); print('                                                       ', end = '\r')
                            tds.get_xu_vip('facebook_follow', 'facebook_api')
                    else:
                        list_nv = listfl['data']
                        if len(list_nv) == 0:
                            print(f'{luc}Hết Nhiệm Vụ Follow                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                        else:
                            print(f'{luc}Tìm Thấy {vang}{len(list_nv)} {luc}Nhiệm Vụ Follow                     ', end = '\r')
                            for x in list_nv:
                                idpost = x['id']
                                id = idpost.split('_')[1] if '_' in idpost else idpost
                                id2 = id[:3]+'#'*(len(id)-6)+id[-3:]
                                code = x['code']
                                like = fb.follow(id)
                                if like == False:
                                    print(f"{luc}FAIL {lam}FOLLOW{trang}: {vang}{id}            ", end = '\r'); sleep(0); print('                                                       ', end = '\r')
                                    Delay(0)
                                    loifollow += 1
                                else:
                                    duyet = tds.cache('facebook_follow_cache', code)
                                    cache = duyet['cache']
                                    dem+=1
                                    loifollow = 0
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(f'{red}[{trang}{dem}{red}][{lam}{time}{red}][{vang}FOLLOW{red}][{trang}{id2}{red}][{trang}{cache}{luc}/{vang}5{red}]')
                                    if dem % doinick == 0:
                                        ptool = 1
                                        break
                                    if dem % nvblock == 0:
                                        Delay(delaybl)
                                    else:
                                        Delay(randint(min, max))

                                    if cache >= 5:
                                        nhan = tds.get_xu_vip('facebook_follow', 'facebook_api')
                                        if 'success' in nhan:
                                            loifollow = 0
                                            xu = nhan['data']['xu']
                                            msg = nhan['data']['msg']
                                            job_success = nhan['data']['job_success']
                                            time = datetime.now().strftime("%H:%M:%S")
                                            print(f'{red}[{trang}X{red}][{lam}{time}{red}][{vang}FOLLOW{red}][{luc}NHẬN XU{red}][{trang}{job_success}/{lam}{cache}{red}][{luc}{msg}{red}][{vang}{str(format(int(xu),","))}{red}][{trang}{myip}{red}]')

                                if loifollow >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(f'{red}Cookie Tài Khoản {vang}{name} {red}Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(f'{red}Tài Khoản {vang}{name} {red}Đã Bị Bé Mark Cho Block {vang}Follow {red}                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                                        nhiemvu = nhiemvu.replace('4','')
                                        break

                if ptool == 1:
                    break

                if '5' in nhiemvu:
                    listpage = tds.get_nv_vip('facebook_page', '')
                    if listpage == False:
                        print(f'{luc}Không Get Được Nhiệm Vụ Like Page                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                    elif 'error' in listpage:
                        if listpage['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listpage['countdown']
                            print(f'{luc}Đang Get Nhiệm Vụ {vang}Follow, {luc}Bú countdown đi e: {str(round(count, 3))}              ', end = '\r'); sleep(0); print('                                                       ', end = '\r')
                            Delay(count)
                        else:
                            print(listpage['error'], end = '\r'); sleep(0); print('                                                       ', end = '\r')
                    else:
                        list_nv = listpage['data']
                        if len(list_nv) == 0:
                            print(f'{luc}Hết Nhiệm Vụ Like Page                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                        else:
                            print(f'{luc}Tìm Thấy {vang}{len(list_nv)} {luc}Nhiệm Vụ Like Page  🤑💸🔫                   ', end = '\r')
                            for x in list_nv:
                                idpost = x['id']
                                id = idpost.split('_')[1] if '_' in idpost else idpost
                                id2 = id[:3]+'#'*(len(id)-6)+id[-3:]
                                code = x['code']
                                like = fb.like_page(id)
                                if like == False:
                                    print(f"{luc}FAIL {lam}LIKEPAGE{trang}: {vang}{id}            ", end = '\r'); sleep(0); print('                                                       ', end = '\r')
                                    Delay(0)
                                    loipage+=1
                                else:
                                    duyet = tds.cache('facebook_page_cache', code)
                                    cache = duyet['cache']
                                    dem+=1
                                    loipage = 0
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(f'{red}[{trang}{dem}{red}][{lam}{time}{red}][{vang}LIKEPAGE{red}][{trang}{id2}{red}][{trang}{cache}{luc}/{vang}5{red}]')
                                    if dem % doinick == 0:
                                        ptool = 1
                                        break
                                    if dem % nvblock == 0:
                                        Delay(delaybl)
                                    else:
                                        Delay(randint(min, max))

                                    if cache >= 5:
                                        nhan = tds.get_xu_vip('facebook_page', 'facebook_api')
                                        if 'success' in nhan:
                                            loipage = 0
                                            xu = nhan['data']['xu']
                                            msg = nhan['data']['msg']
                                            job_success = nhan['data']['job_success']
                                            time = datetime.now().strftime("%H:%M:%S")
                                            print(f'{red}[{trang}X{red}][{lam}{time}{red}][{vang}LIKEPAGE{red}][{luc}NHẬN XU{red}][{trang}{job_success}/{lam}{cache}{red}][{luc}{msg}{red}][{vang}{str(format(int(xu),","))}{red}][{trang}{myip}{red}]')

                                if loipage >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(f'{red}Cookie Tài Khoản {vang}{name} {red}Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(f'{red}Tài Khoản {vang}{name} {red}Đã Bị Bé Mark Cho Block {vang}Like Page {red}                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                                        nhiemvu = nhiemvu.replace('5','')
                                        break

                if ptool == 1:
                    break

                if '6' in nhiemvu:
                    listgr = tds.get_nv_thuong('group')
                    if listgr == False:
                        print(f'{luc}Không Get Được Nhiệm Vụ Group                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                    elif 'error' in listgr:
                        if listgr['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listgr['countdown']
                            print(f'{luc}Đang Get Nhiệm Vụ {vang}Group, {luc}Bú countdown đi e: {str(round(count, 3))}              ', end = '\r'); sleep(0); print('                                                       ', end = '\r')
                            Delay(count)
                        else:
                            print(listgr['error'], end = '\r'); sleep(0); print('                                                       ', end = '\r')
                    else:
                        list_nv = listgr
                        if len(list_nv) == 0:
                            print(f'{luc}Hết Nhiệm Vụ Group                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                        else:
                            print(f'{luc}Tìm Thấy {vang}{len(list_nv)} {luc}Nhiệm Vụ Group  🤑💸🔫                  ', end = '\r')
                        for x in list_nv:
                            idpost = x['id']
                            id2 = idpost[:3]+'#'*(len(idpost)-6)+idpost[-3:]
                            like = fb.group(idpost)
                            if like == False:
                                print(f"{luc}FAIL {lam}GROUP{trang}: {vang}{idpost}            ", end = '\r'); sleep(0); print('                                                       ', end = '\r')
                                Delay(0)
                                loigr += 1
                            else:
                                nhan = tds.get_xu_thuong('GROUP', idpost)
                                if 'success' in nhan:
                                    xu = nhan['data']['xu']
                                    msg = nhan['data']['msg']
                                    loigr = 0
                                    dem+=1
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(f'{red}[{trang}{dem}{red}][{lam}{time}{red}][{vang}GROUP{red}][{trang}{id2}{red}][{luc}{msg}{red}][{vang}{str(format(int(xu),","))}{red}][{trang}{myip}{red}]')
                                    if dem % doinick == 0:
                                        ptool = 1
                                        break
                                    if dem % nvblock == 0:
                                        Delay(delaybl)
                                    else:
                                        Delay(randint(min, max))

                                if loigr >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(f'{red}Cookie Tài Khoản {vang}{name} {red}Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(f'{red}Tài Khoản {vang}{name} {red}Đã Bị Bé Mark Cho Block {vang}Group {red}                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                                        nhiemvu = nhiemvu.replace('6','')
                                        break

                if ptool == 1:
                    break

                if '7' in nhiemvu:
                    listshare = tds.get_nv_thuong('share')
                    if listshare == False:
                        print(f'{luc}Không Get Được Nhiệm Vụ Share Thường                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                    elif 'error' in listshare:
                        if listshare['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listshare['countdown']
                            print(f'{luc}Đang Get Nhiệm Vụ {vang}Share Thường, {luc}Bú countdown đi e: {str(round(count, 3))}              ', end = '\r'); sleep(0); print('                                                       ', end = '\r')
                            Delay(count)
                        else:
                            print(listshare['error'], end = '\r'); sleep(0); print('                                                       ', end = '\r')
                    else:
                        list_nv = listshare
                        if len(list_nv) == 0:
                            print(f'{luc}Hết Nhiệm Vụ Share Thường                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                        else:
                            print(f'{luc}Tìm Thấy {vang}{len(list_nv)} {luc}Nhiệm Vụ Share Thường  🤑💸🔫                   ', end = '\r')
                        for x in list_nv:
                            idpost = x['id']
                            id2 = idpost[:3]+'#'*(len(idpost)-6)+idpost[-3:]
                            share = fb.share(idpost)
                            if share == False:
                                print(f"{luc}FAIL {lam}SHARE{trang}: {vang}{idpost}            ", end = '\r'); sleep(0); print('                                                       ', end = '\r')
                                Delay(0)
                                loisharet += 1
                            else:
                                nhan = tds.get_xu_thuong('SHARE', idpost)
                                if 'success' in nhan:
                                    xu = nhan['data']['xu']
                                    msg = nhan['data']['msg']
                                    loisharet = 0
                                    dem+=1
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(f'{red}[{trang}{dem}{red}][{lam}{time}{red}][{vang}SHARE{red}][{trang}{id2}{red}][{luc}{msg}{red}][{vang}{str(format(int(xu),","))}{red}][{trang}{myip}{red}]')
                                    if dem % doinick == 0:
                                        ptool = 1
                                        break
                                    if dem % nvblock == 0:
                                        Delay(delaybl)
                                    else:
                                        Delay(randint(min, max))

                                if loisharet >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(f'{red}Cookie Tài Khoản {vang}{name} {red}Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(f'{red}Tài Khoản {vang}{name} {red}Đã Bị Bé Mark Cho Block {vang}Share {red}                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                                        nhiemvu = nhiemvu.replace('7','')
                                        break

                if ptool == 1:
                    break

                if '8' in nhiemvu:
                    listpage = tds.get_nv_thuong('page')
                    if listpage == False:
                        print(f'{luc}Không Get Được Nhiệm Vụ Like Page Thường                          ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                    elif 'error' in listpage:
                        if listpage['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listpage['countdown']
                            print(f'{luc}Đang Get Nhiệm Vụ {vang}Like Page Thường, {luc}Bú countdown đi e: {str(round(count, 3))}              ', end = '\r'); sleep(0); print('                                                       ', end = '\r')
                            Delay(count)
                        else:
                            print(listpage['error'], end = '\r'); sleep(0); print('                                                       ', end = '\r')
                    else:
                        list_nv = listpage
                        if len(list_nv) == 0:
                            print(f'{luc}Hết Nhiệm Vụ Like Page Thường                          ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                        else:
                            print(f'{luc}Tìm Thấy {vang}{len(list_nv)} {luc}Nhiệm Vụ Like Page Thường 🤑💸🔫                   ', end = '\r')
                            for x in list_nv:
                                idpost = x['id']
                                id2 = idpost[:3]+'*'*(len(idpost)-6)+idpost[-3:]
                                like = fb.like_page(idpost)
                                if like == False:
                                    print(f"{luc}FAIL {lam}LIKEPAGE{trang}: {vang}{idpost}            ", end = '\r'); sleep(0); print('                                                       ', end = '\r')
                                    Delay(0)
                                    loipage+=1
                                else:
                                    nhan = tds.get_xu_thuong('PAGE', idpost)
                                    if 'success' in nhan:
                                        xu = nhan['data']['xu']
                                        msg = nhan['data']['msg']
                                        loipage = 0
                                        dem+=1
                                        time = datetime.now().strftime("%H:%M:%S")
                                        print(f'{red}[{trang}{dem}{red}][{lam}{time}{red}][{vang}LIKEPAGETHUONG{red}][{trang}{id2}{red}][{luc}{msg}{red}][{vang}{str(format(int(xu),","))}{red}][{trang}{myip}{red}]')
                                        if dem % doinick == 0:
                                            ptool = 1
                                            break
                                        if dem % nvblock == 0:
                                            Delay(delaybl)
                                        else:
                                            Delay(randint(min, max))

                                if loipage >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(f'{red}Cookie Tài Khoản {vang}{name} {red}Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(f'{red}Tài Khoản {vang}{name} {red}Đã Bị Bé Mark Cho Block {vang}Like Page {red}                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                                        nhiemvu = nhiemvu.replace('8','')
                                        break
            
                if ptool == 1:
                    break

                if '9' in nhiemvu:
                    listlike = tds.get_nv_thuong('like')
                    if listlike == False:
                        print(f'{luc}Không Get Được Nhiệm Vụ Like Thường                          ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                    elif 'error' in listlike:
                        if listlike['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listlike['countdown']
                            print(f'{luc}Đang Get Nhiệm Vụ {vang}Like Thường, {luc}COUNTDOWN: {str(round(count, 3))}              ', end = '\r'); sleep(0); print('                                                       ', end = '\r')
                            Delay(count)
                        else:
                            print(listlike['error'], end = '\r'); sleep(0); print('                                                       ', end = '\r')
                    else:
                        list_nv = listlike
                        if len(list_nv) == 0:
                            print(f'{luc}Hết Nhiệm Vụ Like Thường                          ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                        else:
                            print(f'{luc}Tìm Thấy {vang}{len(list_nv)} {luc}Nhiệm Vụ Like Thường                    ', end = '\r')
                            for x in list_nv:
                                idpost = x['id']
                                id = idpost.split('_')[1] if '_' in idpost else idpost
                                id2 = id[:3]+'*'*(len(id)-6)+id[-3:]
                                like = fb.reaction(id, 'LIKE')
                                if like == False:
                                    print(f"{luc}FAIL {lam}LIKETHUONG{trang}: {vang}{id}            ", end = '\r'); sleep(0); print('                                                       ', end = '\r')
                                    Delay(0)
                                    loiliket+=1
                                else:
                                    nhan = tds.get_xu_thuong('LIKE', idpost)
                                    if 'success' in nhan:
                                        xu = nhan['data']['xu']
                                        msg = nhan['data']['msg']
                                        loiliket = 0
                                        dem+=1
                                        time = datetime.now().strftime("%H:%M:%S")
                                        print(f'{red}[{trang}{dem}{red}][{lam}{time}{red}][{vang}LIKETHUONG{red}][{trang}{id2}{red}][{luc}{msg}{red}][{vang}{str(format(int(xu),","))}{red}][{trang}{myip}{red}]')
                                        if dem % doinick == 0:
                                            ptool = 1
                                            break
                                        if dem % nvblock == 0:
                                            Delay(delaybl)
                                        else:
                                            Delay(randint(min, max))

                                if loiliket >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(f'{red}Cookie Tài Khoản {vang}{name} {red}Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(f'{red}Tài Khoản {vang}{name} {red}Đã Bị Bé Mark Cho Block {vang}Like {red}                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                                        nhiemvu = nhiemvu.replace('9','')
                                        break
            
                if ptool == 1:
                    break

                if '0' in nhiemvu:
                    listlike = tds.get_nv_thuong('reaction')
                    if listlike == False:
                        print(f'{luc}Không Get Được Nhiệm Vụ Cảm Xúc Thường                          ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                    elif 'error' in listlike:
                        if listlike['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                            count = listlike['countdown']
                            print(f'{luc}Đang Get Nhiệm Vụ {vang}Cảm Xúc Thường, {luc}COUNTDOWN: {str(round(count, 3))}              ', end = '\r'); sleep(0); print('                                                       ', end = '\r')
                            Delay(count)
                        else:
                            print(listlike['error'], end = '\r'); sleep(0); print('                                                       ', end = '\r')
                    else:
                        list_nv = listlike
                        if len(list_nv) == 0:
                            print(f'{luc}Hết Nhiệm Vụ Cảm Xúc Thường                          ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                        else:
                            print(f'{luc}Tìm Thấy {vang}{len(list_nv)} {luc}Nhiệm Vụ Cảm Xúc Thường                    ', end = '\r')
                            for x in list_nv:
                                idpost = x['id']
                                type = x['type']
                                id = idpost.split('_')[1] if '_' in idpost else idpost
                                id2 = id[:3]+'*'*(len(id)-6)+id[-3:]
                                like = fb.reaction(id, type)
                                if like == False:
                                    print(f"{luc}FAIL {lam}{type}{trang}: {vang}{id}            ", end = '\r'); sleep(0); print('                                                       ', end = '\r')
                                    Delay(0)
                                    loiliket+=1
                                else:
                                    nhan = tds.get_xu_thuong(type, idpost)
                                    if 'success' in nhan:
                                        xu = nhan['data']['xu']
                                        msg = nhan['data']['msg']
                                        loiliket = 0
                                        dem+=1
                                        time = datetime.now().strftime("%H:%M:%S")
                                        print(f'{red}[{trang}{dem}{red}][{lam}{time}{red}][{vang}{type}THUONG{red}][{trang}{id2}{red}][{luc}{msg}{red}][{vang}{str(format(int(xu),","))}{red}][{trang}{myip}{red}]')
                                        if dem % doinick == 0:
                                            ptool = 1
                                            break
                                        if dem % nvblock == 0:
                                            Delay(delaybl)
                                        else:
                                            Delay(randint(min, max))

                                if loiliket >= nhiemvuloi:
                                    fb2 = Facebook_Api(ck)
                                    checktt = fb2.info()
                                    if 'error' in checktt:
                                        print(f'{red}Cookie Tài Khoản {vang}{name} {red}Đã Bị Out or Checkpoint !!!                ')
                                        listck.remove(ck)
                                        ptool = 1
                                        break
                                    else:
                                        print(f'{red}Tài Khoản {vang}{name} {red}Đã Bị Bé Mark Cho Block {vang}Cảm Xúc {red}                           ', end = '\r');sleep(0); print('                                                        ', end = '\r')
                                        nhiemvu = nhiemvu.replace('0','')
                                        break
                if ptool == 1:
                    break
     
              
Main()

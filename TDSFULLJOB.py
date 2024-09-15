import os, json, sys, requests 
from sys import platform
from time import sleep
from datetime import datetime
from random import randint
from pystyle import Colors, Colorate
import uuid, re
from bs4 import BeautifulSoup
def banner():
 os.system("cls" if os.name == "nt" else "clear")
 banner = f"""
\033[1;33m ██████╗ ███████╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     
\033[1;35m██╔═══██╗██╔════╝██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
\033[1;36m██║   ██║█████╗  █████╗         ██║   ██║   ██║██║   ██║██║     
\033[1;37m██║   ██║██╔══╝  ██╔══╝         ██║   ██║   ██║██║   ██║██║     
\033[1;32m╚██████╔╝██║     ██║            ██║   ╚██████╔╝╚██████╔╝███████╗
\033[1;31m ╚═════╝ ╚═╝     ╚═╝            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝\n
\033[1;97mTool By: \033[1;32mOFF TOOL            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tool\033[1;31m     : \033[1;97m☞ \033[1;31mTDS - Facebook\033[1;33m♔ \033[1;97m🔫
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/m@nekosharetool
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32m https://t.me/+Fz2j0ObF2hNiNGJl🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)
class Facebook_Api (object):
	def __init__(self, cookie):
		self.cookie = cookie
		self.user_id = cookie.split('c_user=')[1].split(';')[0]
		self.headers = {'authority': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/','accept-language': 'en-US,en;q=0.9','cookie': cookie}
	
	def get_thongtin(self):
		try:
		#if True:
			#url = requests.get('https://mbasic.facebook.com/profile.php',headers=self.headers).url
			home = requests.get('https://mbasic.facebook.com/profile.php',headers=self.headers).text
			self.fb_dtsg = home.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
			self.jazoest = home.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
			ten = home.split('<title>')[1].split('</title>')[0]
			self.user_id = self.cookie.split('c_user=')[1].split(';')[0]
			#print(f'{luc}Tên Facebook: {vang}{ten} {red}| {luc}ID: {vang}{self.user_id} ')
			#print(f'{ten} | {self.user_id} ')
			return ten, self.user_id
		except:
			return 0

	
	def follow(self, id):
		data = {'av':self.user_id,'__user':self.user_id,'__a':'1','__dyn':'7AzHxqUW13xt0mUyEqxenFwLBwopU98nwgU765QdwSxucyU8EW1twYwJyEiwsobo6u3y4o11U2nwb-q7oc81xoswIK1Rwwwg8a8465o-cwfG12wOKdwGxu782lwv89kbxS2218wc61uwZwlo5qfK0zEkxe2GewyDwsoqBwJK2W5olwUwgojUlDw-wSU72m7-8wywdG7FobpEbUGdwb6223908O3216AzUjwTwNxe6Uak1xwJwxw','__csr':'hcp2vsTfcyBblX4JmmZOiFYKx7KWi_qT9jkxbOfKAAlXWmHGGlq8kNsOVanp9WDQKEHXKRWGulGhaAHHy8VeiWGuUGVoyQUFaui54cCHpp-WCxqHyV9qyUx153qzoWE8ql3pEG4p8pyVGCyooCxe5ojBy98aHG4Eb8mG269Vby8be4oGUO9whXxa2q2q49okyoy26q1BwYxe4E6W10y88E467Erzo6-2y5Etxl3UO2GWwaeu3-7o7uaw922t08K026O03iuC04f802PRw4bw2v80za0G80B-0b-e09dBw0Uww2DOw0jP80n7g3Iw1k208bzE1lU8E','__req':'5','__hs':'9362.HYP:comet_pkg.2.1.0.2.1','dpr':'2','__ccg':'GOOD','__rev':'1006788684','__s':'p2x8mf:qj6dvy:bj8e46','__hsi':'7185171904183015509','__comet_req':'15','fb_dtsg':self.fb_dtsg,'jazoest':self.jazoest,'lsd':'afdisHHGuglOo_hNSDt3Fb','__aaid':'775223720487728','__spin_r':'1006788684','__spin_b':'trunk','__spin_t':'1672928199','fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometUserFollowMutation','variables':'{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1672928202199,140922,190055527696468,","subscribe_location":"PROFILE","subscribee_id":"'+id+'","actor_id":"'+self.user_id+'","client_mutation_id":"1"},"scale":2}','server_timestamps':'true','doc_id':'5032256523527306',}
		headers = {"Host": "www.facebook.com","sec-ch-ua": "\"Chromium\";v\u003d\"107\", \"Not\u003dA?Brand\";v\u003d\"24\"","sec-ch-ua-mobile": "?0","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36","viewport-width": "980","content-type": "application/x-www-form-urlencoded","x-fb-lsd": "afdisHHGuglOo_hNSDt3Fb","x-fb-friendly-name": "CometUserFollowMutation","sec-ch-prefers-color-scheme": "dark","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://www.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.facebook.com/"+id,"accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5","cookie":self.cookie}
		try:
			fl = requests.post('https://www.facebook.com/api/graphql/',headers=headers, data=data)
			if 'IS_SUBSCRIBED' in fl.text:
				return True
			else:
				return fl
		except:
			return False 
	
	def page(self,id):
		data = {'av':self.user_id,'__user':self.user_id,'__a':'1','__dyn':'7AzHxqU5a5Q1ryaxG4VuC0BVU98nwgU765QdwSwAyU8EW0CEboG4E762S1DwUx60gu0BU2_CxS320om78bbwto88422y11xmfz83WwgEcHzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK0zEkxe2GewGwkUtxGm2SUbElxm3y11xfxmu3W2i4U72m7-8wywfCm2Sq2-azo2NwwwOg2cwMwhF8-4UdUcojxK2B0oobo8o','__csr':'g8JNc9n2tWr5W4til-I_On8J9rshlR8nZFiELH_Hnij4JfOJLOGiLoxLBlGRuZaGF4CZddQ4L_JfCiDKWVryuiqqFAcy8x6CBtqJkF8ZVExauAbgOtLAG5FUGFptxqfxi4Hzaz8CQ2SaxC9xCi48Wqqq11g8EaoS9g9U4m224oG68sGucx68wyg6G22mfxa4Xxq7EKbwi82LwNxu48c814EC2K3O5U-2WEhCxO1EwioeUiwiE6e3HwTw18C02k-0exw0deO0jV05Swe20bTw5_w1zF03I202po6e07Co0K6Zlw0jjo0E-0qW08ug8UhBw21e0fLw5Ww9K0Z86u','__req':'o','__hs':'19363.HYP:comet_pkg.2.1.0.2.1','dpr':'2','__ccg':'GOOD','__rev':'1006793331','__s':'v80lqo:poayhk:qxdcmk','__hsi':'7185553908092803679','__comet_req':'15','fb_dtsg':self.fb_dtsg,'jazoest':self.jazoest,'lsd':'V64c7kKr5hAtzX2IIDgKp8','__aaid':'775223720487728','__spin_r':'1006793331','__spin_b':'trunk','__spin_t':'1673017141','fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometPageLikeCommitMutation','variables':'{"input":{"attribution_id_v2":"CometSinglePageHomeRoot.react,comet.page,via_cold_start,1673017144344,576155,250100865708545,","is_tracking_encrypted":true,"page_id":"'+id+'","source":"unknown","tracking":[],"actor_id":"'+self.user_id+'","client_mutation_id":"1"},"isAdminView":false}','server_timestamps':'true','doc_id':'5491200487600992',}
		headers = {"Host": "www.facebook.com","sec-ch-ua": "\"Chromium\";v\u003d\"107\", \"Not\u003dA?Brand\";v\u003d\"24\"","sec-ch-ua-mobile": "?0","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36","viewport-width": "980","content-type": "application/x-www-form-urlencoded","x-fb-lsd": "V64c7kKr5hAtzX2IIDgKp8","x-fb-friendly-name": "CometPageLikeCommitMutation","sec-ch-prefers-color-scheme": "dark","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://www.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.facebook.com/"+id,"accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5","cookie":self.cookie}
		try:
			page = requests.post('https://www.facebook.com/api/graphql/',headers=headers, data=data)
			if 'FOLLOW' in page.text:
				return True
			else:
				return page.text
		except:
			return False
	
	def group(self, id):
			headers = {"Host": "www.facebook.com","sec-ch-ua": "\"Not?A_Brand\";v\u003d\"8\", \"Chromium\";v\u003d\"108\", \"Google Chrome\";v\u003d\"108\"","sec-ch-ua-mobile": "?0","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36","viewport-width": "980","content-type": "application/x-www-form-urlencoded","x-fb-lsd": "gKT7R4dxIBjI4wUDUP5ivT","x-fb-friendly-name": "GroupCometJoinForumMutation","sec-ch-prefers-color-scheme": "dark","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://www.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.facebook.com/groups/"+id+"/","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5","cookie":self.cookie}
			data = {'av':self.user_id,'__user':self.user_id,'__a':'1','__dyn':'7AzHJ16U9ob8ng5K8G6EjBWo2nDwAxu13wsongS3q2ibwyzE2qwJyEiwsobo6u3y4o2Gwfi0LVEtwMw65xO321Rwwwg8a8465o-cwfG12wOKdwGxu782lwv89kbxS2218wc61axe3S1lwlE-U2exi4UaEW2G1jxS6FobrwKxm5oe8464-5pUfEe88o4Wm7-8xmcwfCm2CVEbUGdG1Fwh888cA0z8c84qifxe3u364UrwFg662S26','__csr':'gadNAIYllhsKOE8IpidFPhcIx34Omy9-O9OO8hZ_8-kAymHGAybJqGlvmWl7nWBWJ7GqaXHz7GFe9oy_KBl7h6h4KVah94QeKVHACDyryqKdF5GuXXBCgNpbJ5jjGm8yQEWrCixl6xWuiih5yo-8wAy84mq4poN0Vzbxe16whAufgO5U8UKi4Eyu4EjwGK78527o8411wgocU5u1MwSwFyU8Uf8igaElw8e9xK2GewNgy5o5m1nDwLwrokm16www8G03cy0arw0Zyw0aaC0mG0eJzl8ow2Jw6tw44w4uzo045W1UgSeg0z-07X81-E0cNo0By1Wwi8fE0lYw2h81a8gw9u','__req':'k','__hs':'19363.HYP:comet_pkg.2.1.0.2.1','dpr':'2','__ccg':'EXCELLENT','__rev':'1006794317','__s':'gtlvj8:fxbzro:f2kk19','__hsi':'7185658639628512803','__comet_req':'15','fb_dtsg':self.fb_dtsg,'jazoest':self.jazoest,'lsd':'gKT7R4dxIBjI4wUDUP5ivT','__aaid':'1576489885859472','__spin_r':'1006794317','__spin_b':'trunk','__spin_t':'1673041526','fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'GroupCometJoinForumMutation','variables':'{"feedType":"DISCUSSION","groupID":"'+id+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1673041528761,114928,2361831622,","group_id":"'+id+'","group_share_tracking_params":{"app_id":"2220391788200892","exp_id":"null","is_from_share":false},"actor_id":"'+self.user_id+'","client_mutation_id":"1"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":true,"scale":2,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true,"__relay_internal__pv__GlobalPanelEnabledrelayprovider":false}','server_timestamps':'true','doc_id':'5853134681430324','fb_api_analytics_tags':'["qpl_active_flow_ids=431626709"]',}
			try:
				join = requests.post('https://www.facebook.com/api/graphql/',headers=headers, data=data).text
				if self.user_id in join:
					return True
				else:
					return join
			except:
				return False 

	def reac_cmt(self, id, type_react):
		access = ""
		url = requests.get("https://mbasic.facebook.com/"+id, headers=self.headers, proxies="").url
		if id in url:
			return False
		index = 1 if type_react == "LIKE" else 2 if type_react == "LOVE" else 3 if type_react == "CARE" else 4 if type_react == "HAHA" else 5 if type_react == "WOW" else 6 if type_react == "SAD" else 7
		access = requests.get(url, headers=self.headers).text
		while True:
			if id in access:
				find_cmt = access.split(id)[1].split('</a></span></span>')[0].split('/reactions/picker/?')[1].split('"')[0].replace("amp;", "")
				access = requests.get("https://mbasic.facebook.com/reactions/picker/?"+find_cmt, headers=self.headers).text
				ufi = access.split('/ufi/reaction/?')
				hoan_thanh = requests.get("https://mbasic.facebook.com/ufi/reaction/?"+ufi[index].split('"')[0].replace("amp;", ""), headers=self.headers).text
				return True
			else:
				if "/comment/replies/" in url:
					xemthemcmt = access.split('/comment/replies/?')[1].split('"')[0].replace("amp;", "")
					access = requests.get("https://mbasic.facebook.com/comment/replies/?"+xemthemcmt, headers=self.headers).text
				else:
					xemthemcmt = access.split('/story.php?')[1].split('</a></div></div>')[0].replace("amp;", "").split('"')[0]
					access = requests.get("https://mbasic.facebook.com/story.php?"+xemthemcmt, headers=self.headers).text

	def like(self, id, type):
		if '_' in id:
			uid = id.split('_')[1]
		else:
			uid = id
		list = {'LIKE':1, 'LOVE':2, 'CARE':3, 'HAHA':4, 'WOW':5, 'SAD':6, 'ANGRY':7}
		headers = {
        "authority": "mbasic.facebook.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        #"sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        "sec-ch-ua-mobile": "?0",
        'sec-ch-ua-platform': '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "accept-language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
        "cookie":self.cookie
}
		
		try:
			link = 'https://mbasic.facebook.com/reactions/picker/?ft_id='+uid
			data = requests.get(link, headers=headers).text
			get = data.split('<a href="')
			cx = get[list[type]].split('" style="display:block">')[0].replace("amp;", "").replace(";", "&")
			reac = requests.get('https://mbasic.facebook.com'+cx, headers = headers).text
			#print(reac)
			return True
		except:
			return False 
	
	def comment (self, id, msg):
		try:
			#headers = {"authority": "mbasic.facebook.com","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?0",'sec-ch-ua-platform': '"Windows"',"sec-fetch-dest": "document","sec-fetch-mode": "navigate","sec-fetch-site": "none","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",'user-agent: "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","cookie":self.cookie}
			url = requests.get("https://mbasic.facebook.com/"+id, headers=self.headers).url
			access = requests.get(url, headers=self.headers).text
			cmt = re.findall('\/a\/comment.php\?fs=.*?"', access)
			if cmt == []: return False
			hoan_thanh = requests.post("https://mbasic.facebook.com%s"%cmt[0].replace('"', "").replace("amp;", ""), headers=self.headers, data={"fb_dtsg": self.fb_dtsg,"jazoest": self.jazoest, "comment_text": msg}).text
			return hoan_thanh
		except:
			return False
	
	def share(self, id, nd="An Orin"):
		try:
			url = requests.get('https://mbasic.facebook.com/'+id, headers=self.headers).url
			ac = requests.get(url, headers=self.headers).text
			node_share = re.findall('\/composer\/mbasic\/\?c_src=share.*?"', ac)
			if node_share == []:
				return False
			truycapshare = ac.split('/composer/mbasic/?c_src=share')[1].split('"')[0].replace('amp;', '')
			ac = requests.get('https://mbasic.facebook.com/composer/mbasic/?c_src=share'+truycapshare, headers=self.headers).text
			fb = ac.split('name="fb_dtsg" value="')[1].split('"')[0]
			jaz = ac.split('name="jazoest" value="')[1].split('"')[0]
			target = ac.split('name="target" value="')[1].split('"')[0]
			csid = ac.split('name="csid" value="')[1].split('"')[0]
			privacyx = ac.split('name="privacyx" value="')[1].split('"')[0]
			sid = ac.split('name="sid" value="')[1].split('"')[0]

			data = {
           "fb_dtsg": fb,
            "jazoest": jaz,
            "at": "",
            "target": target,
            "csid": csid,
            "c_src": "share",
            "referrer": "feed",
            "ctype": "advanced",
            "cver": "amber_share",
            "users_with": "",
            "album_id": "",
            "waterfall_source": "advanced_composer_timeline",
            "privacyx": privacyx,
            "appid": "0",
            "sid": sid,
            "linkUrl": "",
            "m": "self",
            "xc_message": "",
            "view_post": "Chia sẻ",
            "shared_from_post_id": sid,
        }
			share = ac.split('/composer/mbasic/?csid=')[2].split('"')[0].replace('amp;', '')
			hoan_thanh = requests.post('https://mbasic.facebook.com/composer/mbasic/?csid='+share, headers=self.headers, data=data).text
			return True
		except:
			return False 
class TraoDoiSub_Api (object):
	def __init__ (self, token):
		self.token = token
	
	def main(self):
		try:
			main = requests.get('https://traodoisub.com/api/?fields=profile&access_token='+self.token).json()
			try:
				return main['data']
			except:
				False
		except:
			return False 
	
	def run(self, id):
		try:
			run = requests.get(f'https://traodoisub.com/api/?fields=run&id={id}&access_token={self.token}').json()
			try:
				run['data']['id']
				return True
			except:
				return False
		except:
			return False
	#follow, like, likegiare, likesieure, reaction, comment, share, reactcmt, group, page
	def get_job(self, type):
		try:
			get = requests.get(f'https://traodoisub.com/api/?fields={type}&access_token={self.token}',headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'})
			return get
		except:
			return False 
		
	def nhan_xu(self, type, id):
		try:
			nhan = requests.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}',headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}).json()
			try:
				xu = nhan['data']['xu']
				msg = nhan['data']['msg']
				return msg, xu
			except:
				return nhan
		except:
			return False


def bongoc(so):
	a= "\033[1;31m────"*so
	print(a)
def hoanthanh(dem, id, type, msg, xu):
	uid = id.split('_')[1] if '_' in id else id
	time=datetime.now().strftime("%H:%M:%S")
	print(f'\033[1;31m[\033[1;33m{dem}\033[1;31m] \033[1;31m| \033[1;36m{time} \033[1;31m| \033[1;36m{type} \033[1;31m| \033[1;33m{uid} \033[1;31m| \033[1;32m{msg} \033[1;31m| \033[1;33m{xu} \033[1;31m|')

def error(id, type):
	time=datetime.now().strftime("%H:%M:%S")
	uid = id.split('_')[1] if '_' in id else id
	print(f'\033[1;31m Đang Lỗi Gì Đó Mong Thông Cảm Nhé', end = '\r'); sleep(2); print('                                                   ', end = '\r')

def Nhap_Cookie():
	list_cookie = []
	i = 0
	while True:
		i += 1
		cookie = input(f'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập Cookie Facebook Thứ: \033[1;33m{i}: ')
		if cookie == '' and i > 1:
			break
		fb = Facebook_Api(cookie)
		name = fb.get_thongtin()
		if name != 0:
			ten = name[0]
			print('\033[1;31m────────────────────────────────────────────────────────────')
			print(f'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTên Facebook: {ten}')
			list_cookie.append(cookie)
			print('\033[1;31m────────────────────────────────────────────────────────────')
		else:
			print('Cookie Facebook Die ! Vui Lòng Nhập Lại !!!')
			print('\033[1;31m────────────────────────────────────────────────────────────')
			i-=1
	return list_cookie
def chongblock(delaybl):
	for i in range(delaybl, -1, -1):
		print(f' Đang hoạt động chống block sẽ chạy lại sau {i} giây  ',end = '\r');sleep(1); print('                                                        ', end = '\r')
def nghingoi(delaymin, delaymax):
	delay = randint(delaymin, delaymax)
	for i in range(delay, -1, -1):
		sleep(1)

def main():
	ntool = 0
	dem = 0
	banner()
	while True:
		if os.path.exists('configtds.txt'):
			with open('configtds.txt', 'r') as f:
				token = f.read()
			tds = TraoDoiSub_Api(token)
			data = tds.main()
			try:
				print('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập [\033[1;33m1\033[1;32m] Giữ Lại Tài Khoản '+ data['user'] )
				print('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập [\033[1;33m2\033[1;32m] Nhập Access_Token TDS Mới')
				chon = input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập \033[1;37m===>:\033[1;33m ')
				if chon == '2':
					os.remove('configtds.txt')
				elif chon == '1':
					pass
				else:
					print('Lựa chọn không xác định !!!');bongoc(14)
					continue 
			except:
				os.remove('configtds.txt')
		if not os.path.exists('configtds.txt'):
			token = input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập Access_Token TDS:\033[1;33m ')
			with open('configtds.txt', 'w') as f:
				f.write(token)
		with open('configtds.txt', 'r') as f:
			token = f.read()
		tds = TraoDoiSub_Api(token)
		data = tds.main()
		try:
			xu = data['xu']
			xudie = data['xudie']
			user = data['user']
			break
		except:
			print('Access Token Không Hợp Lệ! Xin Thử Lại ')
			os.remove('configtds.txt')
			continue 
	print('\033[1;31m────────────────────────────────────────────────────────────')
	
	while True:
		if os.path.exists('Cookie_FB.txt'):
			print('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập [\033[1;33m1\033[1;32m] Sử Dụng Cookie Facebook Đã Lưu ')
			print('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập [\033[1;33m2\033[1;32m] Nhập Cookie Facebook Mới')
			chon = input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mVui Lòng Nhập:\033[1;33m ')
			if chon == '1':
				print('\033[1;32mĐang Lấy Dữ Liệu Đã Lưu');sleep(1)
				with open('Cookie_FB.txt', 'r') as f:
					list_cookie = json.loads(f.read())
					break
			elif chon == '2':
				os.remove('Cookie_FB.txt'); bongoc(14)
			else:
				print('Lựa Chọn Không Xác Định.'); bongoc(14); continue
		if not os.path.exists('Cookie_FB.txt'):
			list_cookie = Nhap_Cookie()
			with open('Cookie_FB.txt', 'w') as f:
				json.dump(list_cookie, f)
			break
	banner()
	print(f'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTên Tài Khoản: {user} ')
	print(f'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mXu Hiện Tại: {xu}')
	print(f'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mXu Bị Phạt: {xudie} ')
	print(f'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mSố Cookie: {len(list_cookie)} ')
	print('\033[1;31m────────────────────────────────────────────────────────────')
	print('\033[1;32m[1 : LIKE — 2 : COMMENT — 3 : SHARE — 4 : REACTION]')
	print('\033[1;32m[5 : FOLLOW — 6 : PAGE — 7 : REACTCMT —  8 : GROUP]')
	print('\033[1;31m────────────────────────────────────────────────────────────')
	print('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mCó Thể Chọn Nhiều Nhiệm Vụ (Ví Dụ 123...)')
	nhiemvu = input ('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập Số Để Chạy Nhiệm Vụ: ')
	delaymin = int(input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập Delay Min: '))
	delaymax = int(input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập Delay Max: '))
	print('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mSau ____ Nhiệm Vụ Thì Kích Hoạt Chống Block.',end='\r')
	nvblock = int(input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mSau '))
	print(f'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mSau {nvblock} Nhiệm Vụ Nghỉ Ngơi ____ Giây       ',end='\r')
	delaybl = int(input(f'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mSau {nvblock} Nhiệm Vụ Nghỉ Ngơi '))
	doinick = int(input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mSau Bao Nhiêu Nhiệm Vụ Thì Đổi Nick: '))
	print('\033[1;31m────────────────────────────────────────────────────────────')
	while True:
		if len(list_cookie) == 0:
			print('Đã Xoá Tất Cả Cookie, Vui Lòng Nhập Lại  ')
			list_cookie = Nhap_Cookie()
			with open('Cookie_FB.txt', 'w') as f:
				json.dump(list_cookie, f)
		for cookie in list_cookie:
			loilike, loicmt, loishare, loicx, loifollow, loipage, loicxcmt, loigroup = 0, 0, 0, 0, 0, 0, 0, 0
			fb = Facebook_Api(cookie)
			name = fb.get_thongtin()
			if name != 0:
				ten = name[0]
				id = name[1]
			else:
				id = cookie.split('c_user=')[1].split(';')[0]
				print(f'Cookie Tài Khoản {id} Die', end='\r');sleep(3); print('                                     ', end = '\r' )
				list_cookie.remove(cookie)
				continue
			cau_hinh = tds.run(id)
			if cau_hinh == True:
				print(f'\033[1;33mĐang Cấu Hình ID FB: {id} \033[1;37m| \033[1;32mTên FB: {ten}')
				print('\033[1;31m────────────────────────────────────────────────────────────')
			else:
				print(f'Cấu Hình Thất Bại ID FB: {id} | Tên FB: {ten} ', end = '\r')
				continue
			ntool = 0
			while True:
			
				nvlike = 1 if '1' in nhiemvu else 0
				nvlike2 = 1 if '1' in nhiemvu else 0
				nvlike3 = 1 if '1' in nhiemvu else 0
				nvcmt = 1 if '2' in nhiemvu else 0
				nvshare = 1 if '3' in nhiemvu else 0
				nvcx = 1 if '4' in nhiemvu else 0
				nvfollow = 1 if '5' in nhiemvu else 0
				nvpage = 1 if '6' in nhiemvu else 0
				nvcxcmt = 1 if '7' in nhiemvu else 0
				nvgroup = 1 if '8' in nhiemvu else 0
			######
				
				if nvlike == 1:
					listlike = tds.get_job('like')
					if listlike == False:
						print('Không Get Được Nhiệm Vụ Like              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						nvlike = 0
					elif 'error' in listlike.text:
						if listlike.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
							coun = listlike.json()['countdown']
							print(f'Đang Get Nhiệm Vụ Like, COUNTDOWN: {str(round(coun, 3))}              ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						else:
							print(listlike.json()['error'] , end ='\r')
						nvlike = 0
					else:
						listlike = listlike.json()
						if len(listlike) == 0:
							print('Hết Nhiệm Vụ Like                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							nvlike = 0
						else:
							print(f'\033[1;32mTìm Thấy {len(listlike)} Nhiệm Vụ Like                       ', end = '\r')
							for x in listlike:
								id = x['id']
								like = fb.like(id, 'LIKE')
								if like == False:
									error(id, 'LIKE')
									loilike += 1
								else:
									nhan=tds.nhan_xu('LIKE', id)
									try:
										xu = nhan[1]
										msg = nhan[0] 
										dem+=1
										hoanthanh(dem, id, 'LIKE', msg, xu)
										loilike = 0
										if dem % doinick == 0:
											bongoc(14); print(f'Số Xu Hiện Tại: {xu} | Số Tài Khoản Facebook {len(list_cookie)}'); bongoc(14); ntool = 1; break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											nghingoi(delaymin, delaymax)
									except:
										error(id, 'LIKE')
										loilike += 1
								
								if loilike >= 5:
									name = fb.get_thongtin()
									if name == 0:
										print(f'  Cookie Tài Khoản {ten} Đã Bị Out !!!                ')
									else:
										print(f' Tài Khoản {ten} Đã Bị Block Like !!!					')
									list_cookie.remove(cookie)
									ntool = 1
									break
			
				if ntool == 1:
					break
			
				if nvlike2 == 1:
					listlike2 = tds.get_job('likegiare')
					if listlike2 == False:
						print('Không Get Được Nhiệm Vụ Like 2                        ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						nvlike2 = 0
					elif 'error' in listlike2.text:
						if listlike2.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
							coun = listlike2.json()['countdown']
							print(f'Đang Get Nhiệm Vụ Like 2, COUNTDOWN: {str(round(coun, 3))}                 ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						else:
							print(listlike2.json()['error'] , end ='\r')
						nvlike2 = 0
					else:
						listlike2 = listlike2.json()
						if len(listlike2) == 0:
							print('Hết Nhiệm Vụ Like 2                                  ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							nvlike2 = 0
						else:
							print(f'\033[1;32mTìm Thấy {len(listlike2)} Nhiệm Vụ Like 2                  ', end = '\r')
							for x in listlike2:
								id = x['id']
								like = fb.like(id, 'LIKE')
								if like == False:
									error(id, 'LIKE 2')
									loilike+=1
								else:
									nhan=tds.nhan_xu('LIKEGIARE', id)
									try:
										xu = nhan[1]
										msg = nhan[0] 
										dem+=1
										hoanthanh(dem, id, 'LIKE 2', msg, xu)
										loilike=0
										if dem % doinick == 0:
											bongoc(14); print(f'Số Xu Hiện Tại: {xu} | Số Tài Khoản Facebook {len(list_cookie)}'); bongoc(14); ntool = 1; break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											nghingoi(delaymin, delaymax)
									except:
										error(id, 'LIKE 2')
										loilike+=1
								

								if loilike >= 5:
									name = fb.get_thongtin()
									if name == 0:
										print(f'  Cookie Tài Khoản {ten} Đã Bị Out !!!                ')
									else:
										print(f' Tài Khoản {ten} Đã Bị Block Like !!!					')
									list_cookie.remove(cookie)
									ntool = 1
									break
				if ntool == 1:
					break
			
				if nvlike3 == 1:
					listlike3 = tds.get_job('likesieure')
					if listlike3 == False:
						print('Không Get Được Nhiệm Vụ Like 3                        ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						nvlike3 = 0
					elif 'error' in listlike3.text:
						if listlike3.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
							coun = listlike3.json()['countdown']
							print(f'Đang Get Nhiệm Vụ Like 3, COUNTDOWN: {str(round(coun, 3))}                 ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						else:
							print(listlike3.json()['error'] , end ='\r')
						nvlike3 = 0
					else:
						listlike3 = listlike3.json()
						if len(listlike3) == 0:
							print('Hết Nhiệm Vụ Like 3                                  ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							nvlike3 = 0
						else:
							print(f'\033[1;32mTìm Thấy {len(listlike3)} Nhiệm Vụ Like 2                  ', end = '\r')
							for x in listlike3:
								id = x['id']
								like = fb.like(id, 'LIKE')
								if like == False:
									error(id, 'LIKE 3')
									loilike+=1
								else:
									nhan=tds.nhan_xu('LIKESIEURE', id)
									try:
										xu = nhan[1]
										msg = nhan[0] 
										dem+=1
										hoanthanh(dem, id, 'LIKE 3', msg, xu)
										loilike=0
										if dem % doinick == 0:
											bongoc(14); print(f'Số Xu Hiện Tại: {xu} | Số Tài Khoản Facebook {len(list_cookie)}'); bongoc(14); ntool = 1; break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											nghingoi(delaymin, delaymax)
									except:
										error(id, 'LIKE 3')
										loilike+=1
								

								if loilike >= 5:
									name = fb.get_thongtin()
									if name == 0:
										print(f'  Cookie Tài Khoản {ten} Đã Bị Out !!!                ')
									else:
										print(f' Tài Khoản {ten} Đã Bị Block Like !!!					')
									list_cookie.remove(cookie)
									ntool = 1
									break
				if ntool == 1:
					break
				if nvcmt == 1:
					listcmt = tds.get_job('comment')
					if listcmt == False:
						print('Không Get Được Nhiệm Vụ Comment                     ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						nvcmt = 0
					elif 'error' in listcmt.text:
						if listcmt.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
							coun = listcmt.json()['countdown']
							print(f'Đang Get Nhiệm Vụ Comment, COUNTDOWN: {str(round(coun, 3))}               ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						else:
							print(listcmt.json()['error'] , end ='\r')
						nvcmt = 0
					else:
						listcmt = listcmt.json()
						if len(listcmt) == 0:
							print('Hết Nhiệm Vụ Comment                                 ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							nvcmt = 0
						else:
							print(f'\033[1;32mTìm Thấy {len(listcmt)} Nhiệm Vụ Comment                           ', end = '\r')
							for x in listcmt:
								id = x['id']
								msg = x['msg']
								cmt = fb.comment(id, msg)
								if cmt == False:
									error(id, 'COMMENT')
									loicmt+=1
								else:
									nhan=tds.nhan_xu('COMMENT', id)
									try:
										xu = nhan[1]
										msg = nhan[0] 
										dem+=1
										hoanthanh(dem, id, 'COMMENT', msg, xu)
										loicmt=0
										if dem % doinick == 0:
											bongoc(14); print(f'Số Xu Hiện Tại: {xu} | Số Tài Khoản Facebook {len(list_cookie)}'); bongoc(14); ntool = 1; break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											nghingoi(delaymin, delaymax)
									except:
										error(id, 'COMMENT')
										loicmt+=1
								
								if loicmt >= 5:
									name = fb.get_thongtin()
									if name == 0:
										print(f'  Cookie Tài Khoản {ten} Đã Bị Out !!!                ')
									else:
										print(f' Tài Khoản {ten} Đã Bị Block Comment !!!					')
									list_cookie.remove(cookie)
									ntool = 1
									break

				if ntool == 1:
					break
				if nvshare == 1:
					listshare = tds.get_job('share')
					if listshare == False:
						print('Không Get Được Nhiệm Vụ Share                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						nvshare = 0
					elif 'error' in listshare.text:
						if listshare.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
							coun = listshare.json()['countdown']
							print(f'Đang Get Nhiệm Vụ Share, COUNTDOWN: {str(round(coun, 3))}                ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						else:
							print(listshare.json()['error'] , end ='\r')
						nvshare = 0
					else:
						listshare = listshare.json()
						if len(listshare) == 0:
							print('Hết Nhiệm Vụ Share ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							nvshare = 0
						else:
							print(f'\033[1;32mTìm Thấy {len(listshare)} Nhiệm Vụ Share                           ', end = '\r')
							for x in listshare:
								id = x['id']
								share = fb.share(id)
								if share == False:
									error(id, 'SHARE')
									loishare+=1
								else:
									nhan=tds.nhan_xu('SHARE', id)
									try:
										xu = nhan[1]
										msg = nhan[0] 
										dem+=1
										hoanthanh(dem, id, 'SHARE', msg, xu)
										loishare = 0
										if dem % doinick == 0:
											bongoc(14); print(f'Số Xu Hiện Tại: {xu} | Số Tài Khoản Facebook {len(list_cookie)}'); bongoc(14); ntool = 1; break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											nghingoi(delaymin, delaymax)
									except:
										error(id, 'SHARE')
										loishare+=1
								
								if loishare >= 5:
									name = fb.get_thongtin()
									if name == 0:
										print(f'  Cookie Tài Khoản {ten} Đã Bị Out !!!                ')
									else:
										print(f' Tài Khoản {ten} Đã Bị Block Share !!!					')
									list_cookie.remove(cookie)
									ntool = 1
									break


				if ntool == 1:
					break
				if nvcx == 1:
					listcx = tds.get_job('reaction')
					if listcx == False:
						print('Không Get Được Nhiệm Vụ Cảm Xúc                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						nvcx = 0
					elif 'error' in listcx.text:
						if listcx.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
							coun = listcx.json()['countdown']
							print(f'Đang Get Nhiệm Vụ Cảm Xúc, COUNTDOWN: {str(round(coun, 3))}                 ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						else:
							print(listcx.json()['error'] , end ='\r')
						nvcx = 0
					else:
						listcx = listcx.json()
						if len(listcx) == 0:
							print('Hết Nhiệm Vụ Cảm Xúc                                 ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							nvcx = 0
						else:
							print(f'\033[1;32mTìm Thấy {len(listcx)} Nhiệm Vụ Cảm Xúc                           ', end = '\r')
							for x in listcx:
								id = x['id']
								type = x['type']
								reac = fb.like(id, type)
								if reac == False:
									error(id, type)
									loilike += 1
								else:
									nhan=tds.nhan_xu(type, id)
									try:
										xu = nhan[1]
										msg = nhan[0] 
										dem+=1
										hoanthanh(dem, id, type, msg, xu)
										loilike = 0
										if dem % doinick == 0:
											bongoc(14); print(f'Số Xu Hiện Tại: {xu} | Số Tài Khoản Facebook {len(list_cookie)}'); bongoc(14); ntool = 1; break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											nghingoi(delaymin, delaymax)
									except:
										error(id, type)
										loilike += 1
								
								
								if loilike >= 5:
									name = fb.get_thongtin()
									if name == 0:
										print(f'  Cookie Tài Khoản {ten} Đã Bị Out !!!                ')
									else:
										print(f' Tài Khoản {ten} Đã Bị Block Cảm Xúc !!!					')
									list_cookie.remove(cookie)
									ntool = 1
									break

				if ntool == 1:
					break
				if nvfollow == 1:
					listfollow = tds.get_job('follow')
					if listfollow == False:
						print('Không Get Được Nhiệm Vụ Follow                      ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						nvfollow = 0
						listfollow = []
					elif 'error' in listfollow.text:
						if listfollow.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
							coun = listfollow.json()['countdown']
							print(f'Đang Get Nhiệm Vụ Follow, COUNTDOWN: {str(round(coun, 3))}                     ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						else:
							print(listfollow.json()['error'] , end ='\r')
							sleep(2)
						nvfollow = 0
						listfollow = []
					else:
						listfollow = listfollow.json()
						if len(listfollow) == 0:
							print('Hết Nhiệm Vụ Follow                                    ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							nvfollow = 0
						else:
							print(f'\033[1;32mTìm Thấy {len(listfollow)} Nhiệm Vụ Follow           ', end = '\r')
							for x in listfollow:
								id = x['id']
								follow = fb.follow(id)
								if follow == False:
									error(id, 'FOLLOW')
									loifollow += 1
								else:
									nhan=tds.nhan_xu('FOLLOW', id)
									try:
										xu = nhan[1]
										msg = nhan[0] 
										dem+=1
										hoanthanh(dem, id, 'FOLLOW', msg, xu)
										loifollow=0
										if dem % doinick == 0:
											bongoc(14); print(f'Số Xu Hiện Tại: {xu} | Số Tài Khoản Facebook {len(list_cookie)}'); bongoc(14); ntool = 1; break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											nghingoi(delaymin, delaymax)
									except:
										error(id, 'FOLLOW')
										loifollow += 1
								
								if loifollow >= 5:
									name = fb.get_thongtin()
									if name == 0:
										print(f'  Cookie Tài Khoản {ten} Đã Bị Out !!!                ')
									else:
										print(f' Tài Khoản {ten} Đã Bị Block Follow !!!					')
									list_cookie.remove(cookie)
									ntool = 1
									break

				if ntool == 1:
					break
				if nvpage == 1:
					listpage = tds.get_job('page')
					if listpage == False:
						print('Không Get Được Nhiệm Vụ Like Page                 ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						nvpage = 0
						listpage = []
					elif 'error' in listpage.text:
						if listpage.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
							coun = listpage.json()['countdown']
							print(f'Đang Get Nhiệm Vụ Page, COUNTDOWN: {str(round(coun, 3))}                         ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						else:
							print(listpage.json()['error'] , end ='\r')
						nvpage = 0
						listpage = []
					else:
						listpage = listpage.json()
						if len(listpage) == 0:
							print('Hết Nhiệm Vụ Like Page                                 ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							nvpage = 0
						else:
							print(f'\033[1;32mTìm Thấy {len(listpage)} Nhiệm Vụ Like Page           ', end = '\r')
							for x in listpage:
								id = x['id']
								page = fb.page(id)
								if page == False:
									error(id, 'PAGE')
									loipage+=1
								else:
									nhan=tds.nhan_xu('PAGE', id)
									try:
										xu = nhan[1]
										msg = nhan[0] 
										dem+=1
										hoanthanh(dem, id, 'PAGE', msg, xu)
										loipage = 0
										if dem % doinick == 0:
											bongoc(14); print(f'Số Xu Hiện Tại: {xu} | Số Tài Khoản Facebook {len(list_cookie)}'); bongoc(14); ntool = 1; break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											nghingoi(delaymin, delaymax)
									except:
										error(id, 'PAGE')
										loipage+=1
								
								
								if loipage >= 5:
									name = fb.get_thongtin()
									if name == 0:
										print(f'  Cookie Tài Khoản {ten} Đã Bị Out !!!                ')
									else:
										print(f' Tài Khoản {ten} Đã Bị Block Like Page !!!					')
									list_cookie.remove(cookie)
									ntool = 1
									break
				if ntool == 1:
					break
				if nvcxcmt == 1:
					listcxcmt = tds.get_job('reactcmt')
					if listcxcmt == False:
						print('Không Get Được Nhiệm Vụ Cảm Xúc Comment ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						nvcxcmt = 0
						listcxcmt = []
					elif 'error' in listcxcmt.text:
						if listcxcmt.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
							coun = listcxcmt.json()['countdown']
							print(f'Đang Get Nhiệm Vụ Cảm Xúc Comment, COUNTDOWN: {str(round(coun, 3))}                   ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						else:
							print(listcxcmt.json()['error'] , end ='\r')
						nvcxcmt = 0
						listcxcmt = []
					else:
						listcxcmt = listcxcmt.json()
						if len(listcxcmt) == 0:
							print('Hết Nhiệm Vụ Cảm Xúc Comment                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							listcxcmt = 0
						else:
							print(f'\033[1;32mTìm Thấy {len(listcxcmt)} Nhiệm Vụ Cảm Xúc Comment               ', end = '\r')
							for x in listcxcmt:
								id = x['id']
								type = x['type']
								cxcmt = fb.like(id, type)
								if cxcmt == False:
									error(id, type+'CMT')
									loicxcmt+=1
								else:
									nhan=tds.nhan_xu(type+'CMT', id)
									try:
							#if True:
										xu = nhan[1]
										msg = nhan[0] 
										dem+=1
										hoanthanh(dem, id, type+'CMT', msg, xu)
										loicxcmt=0
										if dem % doinick == 0:
											bongoc(14); print(f'Số Xu Hiện Tại: {xu} | Số Tài Khoản Facebook {len(list_cookie)}'); bongoc(14); ntool = 1; break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											nghingoi(delaymin, delaymax)
									except:
										error(id, type+'CMT')
										loicxcmt+=1
								
								if loicxcmt >= 5:
									name = fb.get_thongtin()
									if name == 0:
										print(f'  Cookie Tài Khoản {ten} Đã Bị Out !!!                ')
									else:
										print(f' Tài Khoản {ten} Đã Bị Block Cảm Xúc CMT !!!					')
									list_cookie.remove(cookie)
									ntool = 1
									break
				if ntool == 1:
					break
				if nvgroup == 1:
					listgroup = tds.get_job('group')
					if listgroup == False:
						print('Không Get Được Nhiệm Vụ Group                               ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						nvgroup = 0
						listgroup = []
					elif 'error' in listgroup.text:
						if listgroup.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
							coun = listgroup.json()['countdown']
							print(f'Đang Get Nhiệm Vụ Group, COUNTDOWN: {str(round(coun, 3))}               ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						else:
							print(listlike.json()['error'] , end ='\r')
						nvgroup = 0
						listgroup = []
					else:
						listgroup = listgroup.json()
						if len(listgroup) == 0:
							print('Hết Nhiệm Vụ Group                                 ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							listgroup = 0
						else:
							print(f'\033[1;32mThấy {len(listgroup)} Nhiệm Vụ Group           ', end = '\r')
						
							for x in listgroup:
								id = x['id']
								gr = fb.group(id)
								if gr == False:
									error(id, 'GROUP')
									loigroup += 1
								else:
									nhan=tds.nhan_xu('GROUP', id)
									try:
										xu = nhan[1]
										msg = nhan[0] 
										dem+=1
										hoanthanh(dem, id, 'GROUP', msg, xu)
										loigroup = 0
										if dem % doinick == 0:
											bongoc(14); print(f'Số Xu Hiện Tại: {xu} | Số Tài Khoản Facebook {len(list_cookie)}'); bongoc(14); ntool = 1; break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											nghingoi(delaymin, delaymax)
									except:
										error(id, 'GROUP')
										loigroup += 1
								
								if loigroup >= 5:
									name = fb.get_thongtin()
									if name == 0:
										print(f'  Cookie Tài Khoản {ten} Đã Bị Out !!!                ')
									else:
										print(f' Tài Khoản {ten} Đã Bị Block Join Group !!!					')
									list_cookie.remove(cookie)
									ntool = 1
									break
				if ntool == 1:
					break
				if nvcx + nvgroup + nvcxcmt + nvpage + nvfollow + nvshare + nvcmt + nvlike == 0:
					for i in range(10, 0, -1):
						print(f' Tất Cả Các Nhiệm Vụ Đã Hết, Vui Lòng Chờ {i} Giây ', end = '\r');sleep(1); print('                                                        ', end = '\r')
	
if __name__ == '__main__':
	main()

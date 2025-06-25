import requests,os, random
from time import sleep
list_clone = []
list_img = []
dem = 0
stt = 0
stt2 = 0
do = "\033[1;91m"
xanhbien = "\033[1;36m"
vang = "\033[0;33m"
hong = "\033[1;35m"
xanhduong = "\033[1;20m"
xanhla = "\033[1;32m"
xanh="\033[1;32m"
cam="\033[1;33m"
blue="\033[1;20m"
lam="\033[1;20m"
tim="\033[1;20m"
syan="\033[1;36m"
xnhac= "\033[1;96m"
den="\033[1;90m"
luc="\033[1;92m"
xduong="\033[1;94m"
trang="\033[1;97m"
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;20m"
lam = "\033[1;36m"
tim = "\033[35m"
hong = "\033[1;95m"
import os, sys
import requests
import os, sys
import time
from time import strftime
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
# =========================== [ CLASS + FUNCTION TOOL ] ===========================
class API_PRO5_ByNgDucPhat:
    def banner(self):
        os.system('title TOOL REG PAGR PRO5 + UP AVT | ĐA LUỒNG')
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
    def ndp_delay_tool(self, p):
        # Vui Lòng Không Được Xóa Dòng Này Để Tôn Trong Tác Giả
        # Nghiêm Cấm Bán Dưới Mọi Hình Thức
        # Nhận Code Tool Theo Yêu Cầu (Trong Khả Năng) 
        # Zalo: 0396735565 - Nguyễn Đức Phát 
        # Tele: @nguyenducphat - Nguyễn Đức Phát
        while(p>1):
            p=p-1
            print(f'[ 🌸\033[1;20mNP-TOOL🌸][|][\033[1;20mLO......][{p}]','     ',end='\r');sleep(1/6)
            print(f'[ 🌸\033[1;20mNP-TOOL🌸][/][\033[1;20mLOA.....][{p}]','     ',end='\r');sleep(1/6)
            print(f'[ 🌸\033[1;20mNP-TOOL🌸][-][\033[1;20mLOAD....][{p}]','     ',end='\r');sleep(1/6)
            print(f'[ 🌸\033[1;20mNP-TOOL🌸][+][\033[1;20mLOADI...][{p}]','     ',end='\r');sleep(1/6)
            print(f'[ 🌸\033[1;20mNP-TOOL🌸][\][\033[1;20mLOADIN..][{p}]','     ',end='\r');sleep(1/6)
            print(f'[ 🌸\033[1;20MNP-TOOL🌸][|][\033[1;20mLOADING.][{p}]','     ',end='\r');sleep(1/6)
    def getthongtinfacebook(self, cookie: str):
        # Vui Lòng Không Được Xóa Dòng Này Để Tôn Trong Tác Giả
        # Nghiêm Cấm Bán Dưới Mọi Hình Thức
        # Nhận Code Tool Theo Yêu Cầu (Trong Khả Năng) 
        # Zalo: 0396735565 - Nguyễn Đức Phát 
        # Tele: @nguyenducphat - Nguyễn Đức Phát
        headers_get = {'authority': 'www.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36','viewport-width': '1184','cookie': cookie}
        try:
            print(f'Đang Tiến Hành Check Live,Chờ 1 Chút...', end="\r")
            url_profile = requests.get('https://www.facebook.com/me', headers = headers_get).url
            get_dulieu_profile = requests.get(url = url_profile, headers = headers_get).text
        except:
            return False
        try:
            uid_get = cookie.split('c_user=')[1].split(';')[0]
            fb_dtsg_get = get_dulieu_profile.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
            jazoest_get = get_dulieu_profile.split('{"name":"jazoest","value":"')[1].split('"},')[0]
            name_get = get_dulieu_profile.split('<title>')[1].split('</title>')[0]
            return name_get,uid_get,fb_dtsg_get,jazoest_get
        except:
            try:
                uid_get = cookie.split('c_user=')[1].split(';')[0]
                fb_dtsg_get = get_dulieu_profile.split(',"f":"')[1].split('","l":null}')[0]
                jazoest_get = get_dulieu_profile.split('&jazoest=')[1].split('","e":"')[0]
                name_get = get_dulieu_profile.split('<title>')[1].split('</title>')[0]
                return name_get,uid_get,fb_dtsg_get,jazoest_get
            except:
                return False
    def UpAvt(self, cookie, id_page, link_anh):
        sleep(5)
        # Vui Lòng Không Được Xóa Dòng Này Để Tôn Trong Tác Giả
        # Nghiêm Cấm Bán Dưới Mọi Hình Thức
        # Nhận Code Tool Theo Yêu Cầu (Trong Khả Năng) 
        # Zalo: 0396735565 - Nguyễn Đức Phát 
        # Tele: @nguyenducphat - Nguyễn Đức Phát
        try:
            json_upavt =  requests.get(f'https://api-ndpcutevcl.000webhostapp.com/api/upavtpage.php?cookie={cookie}&id={id_page}&link_anh={link_anh}').json()
            if json_upavt['status'] == 'success':
                return json_upavt
            else:
                return False
        except:
            return False
    def RegPage(self, cookie, name, uid, fb_dtsg, jazoest):
        # Vui Lòng Không Được Xóa Dòng Này Để Tôn Trong Tác Giả
        # Nghiêm Cấm Bán Dưới Mọi Hình Thức
        # Nhận Code Tool Theo Yêu Cầu (Trong Khả Năng) 
        # Zalo: 0396735565 - Nguyễn Đức Phát 
        # Tele: @nguyenducphat - Nguyễn Đức Phát
        namepage = requests.get('https://story-shack-cdn-v2.glitch.me/generators/vietnamese-name-generator/male?count=2').json()['data'][0]['name']
        global dem
        headers_reg = {'authority': 'www.facebook.com','accept': '*/*','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','origin': 'https://www.facebook.com','referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','viewport-width': '979','x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation','x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY','cookie': cookie}
        data_reg = {'av': uid,'__user': uid,'__a': '1','__dyn': '7AzHxq1mxu1syUbFuC0BVU98nwgU29zEdEc8co5S3O2S7o11Ue8hw6vwb-q7oc81xoswIwuo886C11xmfz81sbzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwuEjUlDw-wUws9ovUaU3qxWm2Sq2-azo2NwkQ0z8c84K2e3u362-2B0oobo','__csr': 'gP4ZAN2d-hbbRmLObkZO8LvRcXWVvth9d9GGXKSiLCqqr9qEzGTozAXiCgyBhbHrRG8VkQm8GFAfy94bJ7xeufz8jK8yGVVEgx-7oiwxypqCwgF88rzKV8y2O4ocUak4UpDxu3x1K4opAUrwGx63J0Lw-wa90eG18wkE7y14w4hw6Bw2-o069W00CSE0PW06aU02Z3wjU6i0btw3TE1wE5u','__req': 't','__hs': '19296.HYP:comet_pkg.2.1.0.2.1','dpr': '1','__ccg': 'EXCELLENT','__rev': '1006496476','__s': '1gapab:y4xv3f:2hb4os','__hsi': '7160573037096492689','__comet_req': '15','fb_dtsg': fb_dtsg,'jazoest': jazoest,'lsd': 'ZM7FAk6cuRcUp3imwqvHTY','__aaid': '800444344545377','__spin_r': '1006496476','__spin_b': 'trunk','__spin_t': '1667200829','fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation','variables': '{"input":{"bio":"reg auto by duykhanh","categories":["181475575221097"],"creation_source":"comet","name":"'+namepage+'","page_referrer":"launch_point","actor_id":"'+uid+'","client_mutation_id":"1"}}','server_timestamps': 'true','doc_id': '5903223909690825',}
        try:
            idpage = requests.post('https://www.facebook.com/api/graphql/', headers=headers_reg, data=data_reg, timeout=20).json()['data']['additional_profile_plus_create']['additional_profile']['id']
            dem+=1
            print(f'{dem} | SUCCESS | NAME FB: {name} | UID PRO5: {idpage} | NAME PRO5: {namepage}')
            return idpage
        except:
            print('Reg Thất Bại Có Vẻ Acc Của Bạn Đã Bị Block!!')
            return False
# =========================== [ START TOOL ] ===========================
dpcutevcl = API_PRO5_ByNgDucPhat()
dpcutevcl.banner()
while True:
    stt+=1
    cookie_fb = input(f'VUI LÒNG NHẬP COOKIE THỨ (ENTER ĐỂ DỪNG) [{stt}]: ')
    if cookie_fb == '':
        break
    checklive = dpcutevcl.getthongtinfacebook(cookie_fb)
    if checklive != False:
        print('Name Facebook: '+checklive[0])
        list_clone.append(f'{cookie_fb}|{checklive[0]}|{checklive[1]}|{checklive[2]}|{checklive[3]}')
        print('─'*50)
    else:
        stt-1
        print('Cookie '+cookie_fb.split('c_user=')[1].split(';')[0]+', Die Or Out Vui Lòng Kiểm Tra Lại!!')
# Tiến Hành Nhập Setting Reg Page
print('─'*50)
luachon = input('BẠN MUỐN REG PAGE XONG UP AVT KHÔNG? [Y/N]: ')
print('─'*50)
print('[ENTER - ĐỂ DỪNG NHẬP]')
while True:
    stt2+=1 
    link_img = input(f'VUI LÒNG NHẬP LINK ẢNH THỨ [{stt2}]: ')
    if link_img == '':
        break
    list_img.append(link_img)
print('─'*50)
slpage = int(input('BẠN MUỐN TẠO BAO NHIÊU PAGE THÌ DỪNG TOOL: '))
print('─'*50)
delay = int(input(' NHẬP DELAY REG PAGE(PHẢI TRÊN 60S TRÁNH BLOCK!): '))
print('─'*50)
# Tiến Hành Chạy Tool
dpcutevcl.banner()
print('─'*50)
print('Đã Tìm Thấy: '+str(len(list_clone))+' Cookie')
print('Đã Tìm Thấy: '+str(len(list_img))+' Link Image')
print('─'*50)
while True:
    for dulieuclone in list_clone:
        idpage = dpcutevcl.RegPage(str(dulieuclone).split('|')[0], str(dulieuclone).split('|')[1], str(dulieuclone).split('|')[2], str(dulieuclone).split('|')[3], str(dulieuclone).split('|')[4])
        if luachon == 'Y' or luachon == 'y':
            link_anh = random.choice(list_img)
            dpcutevcl.UpAvt(str(dulieuclone).split('|')[0], idpage, link_anh)
            if dpcutevcl != False:
                print(f' ╰─> UP_AVT_SUCCESS | [UID PAGE: {idpage}]')
            else:
                print(f' ╰─> UP_AVT_ERROR | [UID PAGE: {idpage}]')
        dpcutevcl.ndp_delay_tool(delay)
        if dem == slpage:
            input(f'SUCCESS {dem}, PAGE </> ENTER ĐỂ OUT TOOL!!!')
            exit()

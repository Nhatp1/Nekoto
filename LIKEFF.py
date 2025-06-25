import requests
import time
import random
import os,sys
try:
	import requests
except:
	input('Enter để tải thư viện cần thiết!! ')
	os.system('pip install requests bs4 pystyle colorama')

from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
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
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
AQUA = "\033[96m"
LIME = "\033[92m"
os.system('cls' if os.name == 'nt' else 'clear')
print(f"\n{BOLD}{GREEN}ĐANG TẢI VUI LÒNG CHỜ TÍ NHA ⏰")
# Hiệu ứng tải
for i in range(1, 101):
 sys.stdout.write(f"\r{BOLD}{LIME}ĐANG LOADING: {i}%[ {'█' * (i // 2)}{RESET}]")
 sys.stdout.flush()
 time.sleep(0.03)  # Điều chỉnh thời gian chờ nếu cần
os.system('cls' if os.name == 'nt' else 'clear')

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
for X in banner:
 sys.stdout.write(X)
 sys.stdout.flush() 
 time.sleep(0.001)

def send_like_request(idgame):
    urllike = f"https://dichvukey.site/likeff.php?uid={idgame}"
    max_retries = 10
    
    for attempt in range(max_retries):
        try:
            response = requests.get(urllike, timeout=15)
            response.raise_for_status()
            data = response.json()
            break  
        except requests.exceptions.RequestException:
            if attempt == max_retries - 1:
                print("Sever quá tải, vui lòng thử lại sau.")
                return
            time.sleep(5)
        except ValueError:
            print("Phản hồi từ server không hợp lệ.")
            return
    
    if isinstance(data, dict) and "status" in data:
        if data["status"] == 2:
            print("⚠️ Bạn đã đạt giới hạn lượt like hôm nay, vui lòng thử lại sau.Vì mỗi người chỉ dc buff 100like/1 ngày!")
            return
        
        reply_text = (
            f"\n👤 {hong}Tên: {data.get('username', 'Không xác định')}\n"
            f"🆔 {do}UID: {data.get('uid', 'Không xác định')}\n"
            f"? {luc}Level: {data.get('level', 'Không xác định')}\n"
            f"👍 {hong}Like trước khi buff: {data.get('likes_before', 'Không xác định')}\n"
            f"✅ {xanhla}Like sau khi buff: {data.get('likes_after', 'Không xác định')}\n"
            f"➕ {vang}Tổng {hong}cộng{xnhac}: {data.get('likes_given', 'Không xác định')} like\n"
        )
    else:
        reply_text = "Không thể xử lý yêu cầu...."
    
    print(reply_text)

if __name__ == "__main__":
    idgame = input("\033[1;94mNhập ID game free fire cần buff like 🤑: ")
    send_like_request(idgame)

from time import sleep
import sys
import base64
from colorama import Fore, Back, Style
import random
import random
import sys
import os
import sys
import time
import json
import os
import sys
import time
import random
import requests
import subprocess
import uuid
import hashlib
from collections import defaultdict    
from datetime import datetime, timedelta, timezone 
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from colorama import init
from pystyle import Colors, Colorate   
from rich.columns import Columns
from rich.segment import Segment
from rich.measure import Measurement
import random
import string
import requests
import base64
import subprocess
import uuid
import hashlib
from collections import defaultdict    
from datetime import datetime, timedelta
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from colorama import init
from pystyle import Colors, Colorate
from time import sleep
from colorama import Fore, Back, Style
import random
import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich import print as rprint
from rich.prompt import Prompt
from time import sleep
from colorama import Fore, Back, Style
import random
import sys
from time import sleep
from colorama import Fore, Back, Style
import requests
import json
from colorama import Fore, Style
from datetime import datetime, timedelta
from pytz import timezone
import requests
import time
import json
import sys
import random
import string
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import threading
from threading import BoundedSemaphore
import threading
import base64
import os
import time
import re
import json
import random
import requests
import socket
import sys
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from datetime import datetime, timedelta
import os
try:
    from faker import Faker
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    import requests
    from rich.table import Table
    from rich.panel import Panel
    from rich import box
    from colorama import init, Fore
    from rich.console import Console
except ImportError:
    os.system('pip install Faker')
    os.system('pip install requests')
    os.system('pip install pycryptodome')
    
from faker import Faker
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests

def encrypt_data(data):
    """Mã hóa dữ liệu bằng AES-CBC"""
    key = b'ThisIsASecretKey'  
    iv = b'ThisIsAnIV123456'      
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data.encode(), AES.block_size)
    encrypted = cipher.encrypt(padded_data)
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt_data(encrypted_data):
    """Giải mã dữ liệu bằng AES-CBC"""
    try:
        key = b'ThisIsASecretKey'  
        iv = b'ThisIsAnIV123456'  
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted = base64.b64decode(encrypted_data)
        decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
        return decrypted.decode('utf-8')
    except Exception as e:
        print(f"Lỗi khi giải mã dữ liệu: {e}")
        return None

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
AQUA = "\033[96m"
LIME = "\033[92m"
xam='\033[1;30m'
black='\033[1;19m'
xam = '\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
import threading
import base64
import os
import time
import re
import json
import random
import requests
import socket
import sys
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

try:
    from faker import Faker
    from requests import session
    from colorama import Fore, Style
    import pystyle
except ImportError:
    os.system("pip install faker requests colorama bs4 pystyle")
    os.system("pip3 install requests pysocks")
    print('__Vui Lòng Chạy Lại Tool__')
    sys.exit()
    
def thanhngang(so):
    for i in range(so):
        print(trang+'\033[1;31m-',end ='')
    print('')
    
os.system('cls' if os.name == 'nt' else 'clear')
print(">> Loading...")
sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)
xoss("\n\033[1;32mVui Lòng Chờ... ")
sleep(1.5)
os.system('cls' if os.name == 'nt' else 'clear')
for i in range(1, 101):
  sys.stdout.write(f"\r{BOLD}{LIME}ĐANG LOAD TOOL + GIT +: [{i}% {'█' * (i // 2)}]{RESET}")
  sys.stdout.flush()
  sleep(0.03)
sleep(1)
import os
os.system("cls" if os.name == "nt" else "clear")
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)
        
xoss('\n\033[1;32m[●] \033[93mĐang \033[96mLoad \033[95mAPI \033[94mTool...');time.sleep(0.10)
xoss('\n\033[1;36m[●] \033[94mkiểm \033[93mtra \033[95msever \033[96mtool...')
xoss('\n\033[1;33m[●] \033[96mkiểm \033[95mtra \033[94mbản \033[93mupdate.. ')
xoss('\n\033[1;34m[●] \033[91mTiến \033[96mhành \033[94mvào \033[95mtool...')
def Update():
    exit('\033[1;31m[●] Đang Tiến Hành Vào Tool...... ')

sleep(1)
colors = [
    "\033[1;37m\033[1m",
    "\033[1;32m\033[1m",
    "\033[1;34m\033[1m", 
    "\033[1m\033[38;5;51m",
    "\033[1;31m\033[1m\033[1m",
    "\033[1;30m\033{1m",
    "\033[1;33m\033[1m",
    "\033[1;35m\033[1m",
    "\033[32;5;245m\033[1m\033[38;5;39m",
]

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
  sleep(0.001)
  
def bes4(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            version_tag = soup.find('span', id='version_vip')
            maintenance_tag = soup.find('span', id='maintenance_vip')
            version = version_tag.text.strip() if version_tag else None
            maintenance = maintenance_tag.text.strip() if maintenance_tag else None
            return version, maintenance
    except requests.RequestException:
        return None, None
    return None, None

def checkver():
    url = 'https://checkserver.hotrommo.com/'
    version, maintenance = bes4(url)
    if maintenance == 'on':
        print("\033[1;31mTool đang được bảo trì. Vui lòng thử lại sau. \nHoặc vào nhóm ZaLo: \033[1;32mhttps://zalo.me/g/vmugmo123")
        sys.exit()
    return version

current_version = checkver()
if current_version:
    print(f"Phiên bản hiện tại: {current_version}")
else:
    print("Không thể lấy thông tin phiên bản hoặc tool đang được bảo trì.")
    sys.exit()

  
def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        ip_address = ip_data['ip']
        return ip_address
    except Exception as e:
        print(f"Lỗi khi lấy địa chỉ IP: {e}")
        return None

def display_ip_address(ip_address):
    if ip_address:
        print(f"\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mĐịa chỉ IP : {ip_address}")
    else:
        print("Không thể lấy địa chỉ IP của thiết bị.")

def luu_thong_tin_ip(ip, key, expiration_date):
    data = {ip: {'key': key, 'expiration_date': expiration_date.isoformat()}}
    encrypted_data = encrypt_data(json.dumps(data))
    with open('ip_key.json', 'w') as file:
        file.write(encrypted_data)

def tai_thong_tin_ip():
    try:
        with open('ip_key.json', 'r') as file:
            encrypted_data = file.read()
        data = json.loads(decrypt_data(encrypted_data))
        return data
    except FileNotFoundError:
        return None

def kiem_tra_ip(ip):
    data = tai_thong_tin_ip()
    if data and ip in data:
        expiration_date = datetime.fromisoformat(data[ip]['expiration_date'])
        if expiration_date > datetime.now():
            return data[ip]['key']
    return None

def generate_key_and_url(ip_address):
    ngay = int(datetime.now().day)
    key1 = str(ngay * 27 + 27)
    ip_numbers = ''.join(filter(str.isdigit, ip_address))
    key = f'NP-{key1}{ip_numbers}'
    expiration_date = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    url = f'http://hvhtool.linkpc.net/?ma={key}'
    return url, key, expiration_date

def da_qua_gio_moi():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    return now >= midnight

def get_shortened_link_phu(url):
    """
    Hàm để rút gọn URL bằng một dịch vụ API.
    """
    try:
        token = "6671b17cc2957c24526bc20d"  
        api_url = f"https://link4m.co/api-shorten/v2?api=6671b17cc2957c24526bc20d&url={url}"
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"status": "error", "message": "Không thể kết nối đến dịch vụ rút gọn URL."}
    except Exception as e:
        return {"status": "error", "message": f"Lỗi khi rút gọn URL: {e}"}

def check_internet_connection():
    try:
        response = requests.get("https://google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def main():
    # Kiểm tra kết nối internet
    if not check_internet_connection():
        print("\033[1;31mCheck Mạng Wifi Hoặc 4G! ")
        sleep(0.5)
        sys.exit()

    ip_address = get_ip_address()
    display_ip_address(ip_address)

    if ip_address:
        existing_key = kiem_tra_ip(ip_address)
        if existing_key:
            print(f"\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mTool còn hạn, mời bạn dùng tool...")
            time.sleep(2)
        else:
            if da_qua_gio_moi():
                print("\033[1;33mQuá giờ sử dụng tool !!!")
                return

            url, key, expiration_date = generate_key_and_url(ip_address)

            with ThreadPoolExecutor(max_workers=2) as executor:
                print("\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;32mNhập 1 Để Lấy Key \033[1;33m( Free )")

                while True:
                    try:
                        choice = input("\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;34mNhập lựa chọn: ")
                        print("\033[97m════════════════════════════════════════════════")
                        if choice == "1":
                            yeumoney_future = executor.submit(get_shortened_link_phu, url)
                            yeumoney_data = yeumoney_future.result()
                            if yeumoney_data and yeumoney_data.get('status') == "error":
                                print(yeumoney_data.get('message'))
                                return
                            else:
                                link_key_yeumoney = yeumoney_data.get('shortenedUrl')
                                print('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mLink Để Vượt Key Là \033[1;36m:', link_key_yeumoney)

                            while True:
                                keynhap = input('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;33mKey Đã Vượt Là: \033[1;32m')
                                if keynhap == key:
                                    print('Key Đúng Mời Bạn Dùng Tool')
                                    sleep(2)
                                    luu_thong_tin_ip(ip_address, keynhap, expiration_date)
                                    break
                                else:
                                    print('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mKey Sai Vui Lòng Vượt Lại Link \033[1;36m:', link_key_yeumoney)
                    except ValueError:
                        print("Vui lòng nhập số hợp lệ.")
                    except KeyboardInterrupt:
                        print("\n\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mCảm ơn bạn đã dùng Tool !!!")
                        sys.exit()

if __name__ == '__main__':
    main()

init(autoreset=True)
console = Console()

os.system('cls' if os.name == 'nt' else 'clear')
for i in range(1, 101):
  sys.stdout.write(f"\r{BOLD} \033[38;5;155mĐANG LOAD MENU : [{i}% {'█' * (i // 2)}]{RESET}")
  sys.stdout.flush()
  sleep(0.003)
sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print(banner)
thanhngang(65)

print (Colorate.Diagonal(Colors.white_to_green, "╔══════════════════════╗         "))
print (Colorate.Diagonal(Colors.white_to_green,"║  Tool Golike         ║          "))
print (Colorate.Diagonal(Colors.white_to_green, "╚══════════════════════╝           "))
print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m1\033[1;39m]\033[1;32m Tool Golike TikTok \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m ADB + Auto Click VIP \033[1;39m]")
print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1 woord \033[1;39m[\033[1;35m2\033[1;39m]\033[1;32m Tool Golike SnapChat \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m ADB + Auto Click VIP \033[1;39m]")
print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m3\033[1;39m]\033[1;32m Tool Golike Twitter ( X ) \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m Cookie VIP \033[1;39m]")
print (Colorate.Diagonal(Colors.white_to_green, "┌───────────────────┐"))
print (Colorate.Diagonal(Colors.white_to_green, "║ TraoDoiSub.com    ║"))
print (Colorate.Diagonal(Colors.white_to_green, "└───────────────────┘"))
print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m4\033[1;39m]\033[1;32m Tool Traodoisub TikTok \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m Auto Click VIP \033[1;39m]")
print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m5\033[1;39m]\033[1;32m Tool Traodoisub Facebook \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m Cookie VIP \033[1;39m]")
print (Colorate.Diagonal(Colors.white_to_green, "┌───────────────────┐"))
print (Colorate.Diagonal(Colors.white_to_green, "║ Tuongtaccheo.com  ║"))
print (Colorate.Diagonal(Colors.white_to_green, "└───────────────────┘"))
print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m6\033[1;39m]\033[1;32m Tool Tuongtaccheo Facebook \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m Cookie VIP \033[1;39m]")
print (Colorate.Diagonal(Colors.white_to_green, "┌───────────────────┐"))
print (Colorate.Diagonal(Colors.white_to_green, "║      Pro5 Fb      ║"))
print (Colorate.Diagonal(Colors.white_to_green, "└───────────────────┘"))
print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m7\033[1;39m]\033[1;32m Tool Reg Page Pro5 Facebook \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m VIP \033[1;39m]")
print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m8\033[1;39m]\033[1;32m Tool Buff Story Pro5 Facebook \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m VIP \033[1;39m]")
print (Colorate.Diagonal(Colors.white_to_green, "┌───────────────────┐"))
print (Colorate.Diagonal(Colors.white_to_green, "║      Tiện Ích     ║"))
print (Colorate.Diagonal(Colors.white_to_green, "└───────────────────┘"))
print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m9\033[1;39m]\033[1;32m Tool Spam SMS + Call \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m VIP \033[1;39m]")
print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m10\033[1;39m]\033[1;32m Tool Vua Thoát Hiểm Xworld \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m Random \033[1;39m]")
print (Colorate.Diagonal(Colors.white_to_green, "┌───────────────────┐"))
print (Colorate.Diagonal(Colors.white_to_green, "║      Buff Vip     ║"))
print (Colorate.Diagonal(Colors.white_to_green, "└───────────────────┘"))
print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m11\033[1;39m]\033[1;32m Tool Buff Follow + Like API Free \033[1;39m[\033[38;5;204m FREE \033[1;39m]")
print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m12\033[1;39m]\033[1;32m Tool Buff Like Free Fire \033[1;39m[\033[1;34m VIP \033[1;39m]")
print (Colorate.Diagonal(Colors.white_to_green, "┌───────────────────┐"))
print (Colorate.Diagonal(Colors.white_to_green, "║    Proxy               ║"))
print (Colorate.Diagonal(Colors.white_to_green, "└───────────────────┘"))
print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m13\033[1;39m]\033[1;32m Tool Đào Proxy \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m VIP \033[1;39m]")
print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m14\033[1;39m]\033[1;32m Tool Lọc Proxy Live/Die \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m VIP \033[1;39m]")
print (Colorate.Diagonal(Colors.white_to_green, "┌───────────────────┐"))
print (Colorate.Diagonal(Colors.white_to_green, "║       Tool PC     ║"))
print (Colorate.Diagonal(Colors.white_to_green, "└───────────────────┘"))
print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m15\033[1;39m]\033[1;32m Tool Zefoy No Auto Captcha ( TỰ GIẢI CAPTCHA ) \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m PC VIP \033[1;39m]")
print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m16\033[1;39m]\033[1;32m Tool Nuôi Acc Tiktok Clone \033[1;39m[\033[38;5;204m BETA + DỄ LỖI \033[1;39m]")
print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m27\033[1;39m]\033[1;32m Tool Golike FB Đa Luồng \033[1;39m[\033[38;5;204m BETA + DỄ LỖI \033[1;39m]")

thanhngang(65)

chon = input("\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[32;5;245m\033[1m\033[38;5;39mNhập \033[1;33mSố \033[1;34mTool \033[38;5;204mMà \033[38;5;155mBạn \033[1;35mCần \033[1;36mChạy : \033[38;5;204m")  

os.system('cls' if os.name == 'nt' else 'clear')
for i in range(1, 101):
  sys.stdout.write(f"\r{BOLD} \033[38;5;204mCHỜ ĐỢI LÀ HẠNH PHÚC: [{i}% {'█' * (i // 2)}]{RESET}")
  sys.stdout.flush()
  sleep(0.03)  
# hàm chống bug mạng tránh mấy a bug lỏd 🤟
if not check_internet_connection():
    print("\033[1;31mCheck Mạng Wifi Hoặc 4G! ")
    sleep(0.5)
    exit()

if chon in [str(i) for i in range(1, 21)]:
    print(f"\033[1;32mĐang chạy tool số {chon}...")
    # TODO
else:
    print("\033[1;31mLựa chọn không hợp lệ!")
    sys.exit()

if chon == "1":
    exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/AutoTikTokv1.py').text)
if chon == "2":
     exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/AUTOSNAPCHAT.py').text)
if chon == "3":
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/AUTOTW.py').text)
if chon == "4":
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/TDSTIKTOK.py').text)
if chon == "5":
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/TDSFULLJOB.py').text)
if chon == "6":
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/TTCPRO5.py').text)
if chon == "0":                                 
# Chỉ thoát tool khi nhập số "0"
	exec(requests.get('https://raw.githubusercontent.com/Khanh23047/thoattool/main/.github/workflows/main.yml').text)
if chon == "7":
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/REGPAGE.py').text)
if chon == "8":
    exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/VIEWSTR.py').text)
if chon == "9":
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/SPAMSMSV1.py').text)
#if chon == "10":
#	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/TX.py').text)
if chon == "10":
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/THAMHIEMXWORD.py').text)
if chon == "11":
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/BUFFTIK.py').text)
if chon == "12":
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/LIKEFF.py').text)
if chon == "13":
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/GETPRX.py').text)
if chon == "14":
	print("Vô tool 13 là có à")
#if chon == "16":
#	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/DAOMAIL.py').text)
#if chon == "17":
#	exec(requests.get('https://raw.githubusercontent.com/Cacdume-wq/cac/refs/heads/main/cc-cccc76655thv%40%2C*%40.py').text)
#if chon == "18":
#	exec(requests.get('https://raw.githubusercontent.com/Cacdume-wq/cac/refs/heads/main/cc-cccc76655thv%40%2C*%40.py').text)
#if chon == "17":
#	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/DECODE.py').text)
if chon == "15":
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/ZEFOY.py').text)
if chon == "16":
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/NUOITIK.py').text)
if chon == "17":
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/GOFBDL.py').text)
# if chon == 

    

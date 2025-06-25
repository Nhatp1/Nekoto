import requests
import os
import colorama
import time
from colorama import Fore
colorama.init(autoreset=True)
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

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])
def makefile():
    linux1 = 'mkdir OUTPUT'
    windows1 = 'mkdir OUTPUT'
    os.system([linux1,windows1][os.name == 'nt'])
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
System.Clear()

def welcome():
    logo =f"""
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
    print(logo)
    print(Fore.CYAN + fr"============================================================================")
    print("\033[1;97m[\033[1;91m•_•\033[1;97m] => \033[1;32mNhập 0 => Out Tool")
    print("\033[1;97m[\033[1;91m•_•\033[1;97m] => \033[1;32mNhập 1 => Get Proxy For Windows")
    print("\033[1;97m[\033[1;91m•_•\033[1;97m] => \033[1;32mNhập 2 => Get Proxy For Kali Linux, Parrot OS,..")

def bannerW():
    print(f"""
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

                                                                                                            """)
    print(Fore.CYAN + fr"================================================================================")
    print("\n")
    print("\033[1;97m[\033[1;91m•_•\033[1;97m] => \033[1;32m1.Back To Menu")
    print("\033[1;97m[\033[1;91m•_•\033[1;97m] => \033[1;32m2.Proxy Socks5")
    print("\033[1;97m[\033[1;91m•_•\033[1;97m] => \033[1;32m3.Proxy Socks4")
    print("\033[1;97m[\033[1;91m•_•\033[1;97m] => \033[1;32m4.Proxy HTTP")
    print("\033[1;97m[\033[1;91m•_•\033[1;97m] => \033[1;32m5.Get All Proxys: Socks5, Socks4 and HTTP")



def get_proxyW():
    cls()
    bannerW()
    you = int(input("\n \033[1;97m[\033[1;91m•_•\033[1;97m] \033[1;36m  \033[1;32mNhập : "))
    path = os.getcwd()
    filep = os.path.join(path)

    if you==1:
        
        url = 'https://openproxylist.xyz/socks5.txt'
        url_1 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=1250&country=all&simplified=true'
        a = requests.get(url,url_1, allow_redirects=True)
        with open(filep + '\OUTPUT\socks5.txt','wb') as file1:
            file1.write(a.content)
            sleep(1)
        #readFile:
        line = open(filep + '\\OUTPUT\\socks5.txt')
        lines = line.readlines()
        line.close()
        for socks5 in lines:
            socks5 = socks5.strip()
            print(Fore.GREEN + socks5)
        print(Fore.GREEN + "\n[+] Succesfully !")
        print(Fore.YELLOW + "\n---> The file was saved as socks5.txt in the 'OUTPUT' folder")

    elif you==2:
        url2 = 'https://openproxylist.xyz/socks4.txt'
        url_2 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=1250&country=all&simplified=true'
        b = requests.get(url2,url_2, allow_redirects=True)
        with open(filep + '\OUTPUT\socks4.txt','wb') as file2:
            file2.write(b.content)
            sleep(1)
        #readFile:
        line2 = open(filep + '\\OUTPUT\\socks4.txt')
        lines2 = line2.readlines()
        line2.close()
        for socks4 in lines2:
            socks4 = socks4.strip()
            print(Fore.GREEN + socks4)
        print(Fore.GREEN + "\n[+] Succesfully !")
        print(Fore.YELLOW + "\n---> The file was saved as socks4.txt in the 'OUTPUT' folder")

    elif you==3:
        url3 = 'https://openproxylist.xyz/http.txt'
        url_3 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=1250&country=all&simplified=true'
        c = requests.get(url3,url_3, allow_redirects=True)
        with open(filep + '\OUTPUT\http.txt','wb') as file3:
            file3.write(c.content)
            sleep(1)
        #readFile:
        line3 = open(filep + '\\OUTPUT\\http.txt')
        lines3 = line3.readlines()
        line3.close()
        for http in lines3:
            http = http.strip()
            print(Fore.GREEN + http)
        print(Fore.GREEN + "\n[+] Succesfully !")
        print(Fore.YELLOW + "\n---> The file was saved as http.txt in the 'OUTPUT' folder")

    elif you==4:
        url_socks5 = 'https://openproxylist.xyz/socks5.txt'
        url_socks5_1 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=1250&country=all&simplified=true'
        
        url_socks4 = 'https://openproxylist.xyz/socks4.txt'
        url_socks4_1 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=1250&country=all&simplified=true'

        url_http = 'https://openproxylist.xyz/http.txt'
        url_http_1 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=1250&country=all&simplified=true'

        all1 = requests.get(url_socks5,url_socks4, allow_redirects=True)
        all2 = requests.get(url_socks5_1,url_socks4_1, allow_redirects=True)
        all3 = requests.get(url_http,url_http_1)
        with open(filep + '\\OUTPUT\\All-Proxy.txt','wb') as file4:
            file4.write(all1.content)
            file4.write(all2.content)
            file4.write(all3.content)
            sleep(1)
        #readFile:
        line4 = open(filep + '\\OUTPUT\\All-Proxy.txt')
        lines4 = line4.readlines()
        line4.close()
        for all_proxy in lines4:
            all_proxy = all_proxy.strip()
            print(Fore.GREEN + all_proxy)
        print(Fore.GREEN + "\n[+] Succesfully !")
        print(Fore.YELLOW + "\n---> The file was saved as All-Proxy.txt in the 'OUTPUT' folder")
    elif you == 0:
       select()
        
    else:
        print(Fore.RED + 'ERROR !!!')

def get_proxyLinux():
    cls()
    bannerW()
    you = int(input("\n >>>  "))
    path = os.getcwd()
    filep = os.path.join(path)

    if you==1:
        url = 'https://openproxylist.xyz/socks5.txt'
        url_1 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=1250&country=all&simplified=true'
        a = requests.get(url,url_1, allow_redirects=True)
        with open(filep + '/OUTPUT/socks5.txt','wb') as file1:
            file1.write(a.content)
            sleep(1)
        #readFile:
        line = open(filep + '/OUTPUT/socks5.txt')
        lines = line.readlines()
        line.close()
        for socks5 in lines:
            socks5 = socks5.strip()
            print(Fore.GREEN + socks5)
        print(Fore.GREEN + "\n[+] Succesfully !")
        print(Fore.YELLOW + "\n---> The file was saved as socks5.txt in the 'OUTPUT' folder")

    elif you==2:
        url2 = 'https://openproxylist.xyz/socks4.txt'
        url_2 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=1250&country=all&simplified=true'
        b = requests.get(url2,url_2, allow_redirects=True)
        with open(filep + '/OUTPUT/socks4.txt','wb') as file2:
            file2.write(b.content)
            sleep(1)
        #readFile:
        line2 = open(filep + '/OUTPUT/socks4.txt')
        lines2 = line2.readlines()
        line2.close()
        for socks4 in lines2:
            socks4 = socks4.strip()
            print(Fore.GREEN + socks4)
        print(Fore.GREEN + "\n[+] Succesfully !")
        print(Fore.YELLOW + "\n---> The file was saved as socks4.txt in the 'OUTPUT' folder")

    elif you==3:
        url3 = 'https://openproxylist.xyz/http.txt'
        url_3 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=1250&country=all&simplified=true'
        c = requests.get(url3,url_3, allow_redirects=True)
        with open(filep + '/OUTPUT/http.txt','wb') as file3:
            file3.write(c.content)
            sleep(1)
        #readFile:
        line3 = open(filep + '/OUTPUT/http.txt')
        lines3 = line3.readlines()
        line3.close()
        for http in lines3:
            http = http.strip()
            print(Fore.GREEN + http)
        print(Fore.GREEN + "\n[+] Succesfully !")
        print(Fore.YELLOW + "\n---> The file was saved as http.txt in the 'OUTPUT' folder")

    elif you==4:
        url_socks5 = 'https://openproxylist.xyz/socks5.txt'
        url_socks5_1 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=1250&country=all&simplified=true'
        
        url_socks4 = 'https://openproxylist.xyz/socks4.txt'
        url_socks4_1 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=1250&country=all&simplified=true'

        url_http = 'https://openproxylist.xyz/http.txt'
        url_http_1 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=1250&country=all&simplified=true'

        all1 = requests.get(url_socks5,url_socks4, allow_redirects=True)
        all2 = requests.get(url_socks5_1,url_socks4_1, allow_redirects=True)
        all3 = requests.get(url_http,url_http_1)
        with open(filep + '/OUTPUT/All-Proxy.txt','wb') as file4:
            file4.write(all1.content)
            file4.write(all2.content)
            file4.write(all3.content)
            sleep(1)
        #readFile:
        line4 = open(filep + '/OUTPUT/All-Proxy.txt')
        lines4 = line4.readlines()
        line4.close()
        for all_proxy in lines4:
            all_proxy = all_proxy.strip()
            print(Fore.GREEN + all_proxy)
        print(Fore.GREEN + "\n[+] Succesfully !")
        print(Fore.YELLOW + "\n---> The file was saved as All-Proxy.txt in the 'OUTPUT' folder")

    elif you == 0:
       select()

    else:
        print(Fore.RED + 'ERROR !!!')

def select():
    while True:
        linux = 'clear'
        windows = 'cls'
        os.system([linux,windows][os.name == 'nt'])
        makefile()
        welcome()
        you = int(input("\n>>> "))
        if you==1:
            get_proxyW()
            exit()
        elif you==2:
            get_proxyLinux()
            exit()
        elif you == 0:
            print(Fore.BLUE + "\n GoodBye, See you again ^^")
            break
        else:
            print(Fore.RED + "\n ERROR !!!")
select()

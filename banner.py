#!/usr/bin/python3

import sys
import requests
import ast
import subprocess
import time
import hashlib
import os
import json
import socket
import threading
import random 
from datetime import datetime, timedelta

chars = " ➤ [«/»] >>>"
pyver = ".".join(sys.version.split(" ")[0].split(".")[:-1])
ip = requests.post('https://api.proxyscrape.com/ip.php').text
ngay = str(time.strftime("%d"))
thang = str(time.strftime("%m"))
nam = str(time.strftime("%Y"))

def install_missing_modules():
    md = open(__file__, 'r').read()
    tree = ast.parse(md)
    imported_modules = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_modules.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            imported_modules.add(node.module)
    for lib in imported_modules:
        try:
            __import__(lib)
        except ImportError:
            print(f"Đang Tiến Hành Cài Đặt Thư Viện: [{lib}]")
            try:
                start_time = time.time()
                process = subprocess.Popen(["pip", "install", lib], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                while True:
                    return_code = process.poll()
                    if return_code is not None:
                        if return_code == 0:
                            print(f"Thành Công .. [{lib}]")
                        else:
                            print(f"Thất Bại .. [{lib}]. Vui Lòng Thử Lại Sau.")
                            print(process.stderr.read().decode())
                        break
                    elapsed_time = time.time() - start_time
                    print(f"Đang Cài Đặt {lib}... [{elapsed_time:.2f}s]", end='\r')
                    time.sleep(0.1)
            except Exception as e:
                print(f"Đã Xảy Ra Lỗi Khi Cài Đặt {lib}: {e}")
                sys.exit(1)
                
def check_connection():
    while True:
        try:
            response = requests.get("https://www.google.com.vn", timeout=5)
        except (requests.exceptions.ReadTimeout, requests.ConnectionError):
            print("Vui Lòng Kiểm Tra Kết Nối Mạng !!!")
            sys.exit()
        except (requests.exceptions.RequestException, Exception) as e:
            print(f"Lỗi: {str(e)}")
        time.sleep(5)    

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    ban = f"""
███╗   ██╗   ████████╗ ██████╗  ██████╗ ██╗     
████╗  ██║   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██╔██╗ ██║█████╗██║   ██║   ██║██║   ██║██║     
██║╚██╗██║╚════╝██║   ██║   ██║██║   ██║██║     
██║ ╚████║      ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝  ╚═══╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                
                © Copyright N-TOOL
════════════════════════════════════════════════════════════
{chars} (((Author : N-TOOL)))
{chars} Contact Me:
{chars}     -> [@NeKo109] [Telegram]
{chars} Group Me:    
{chars}     -> [https://zalo.me/g/addkgf309] [Zalo]
"""
    for i in ban:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.005)

def line(length):
    line = ""
    for i in range(length):
        line += f"═"
    for i in range(len(line)):
        sys.stdout.write(line[i])
        sys.stdout.flush()
        time.sleep(0.005)
    print() 

def custom_delay(types):
    for phase in ['XXXXX', 'XXXX.', 'XXX..', 'XX...', 'X....', '.X...', '..X..', '...X.', '....X', '...XX', '..XXX', '.XXXX', 'XXXXX']:
        print(f'{chars} [N-TOOL][{types}] >>> [{phase}]', end='\r')
        time.sleep(1/13)

def chay_tool(url):
    try:
        exec(requests.get(url).text)
    except (requests.ConnectionError, requests.exceptions.ReadTimeout):
        print("Vui Lòng Kiểm Tra Kết Nối Mạng !!!")
        sys.exit()
    except (requests.exceptions.RequestException, Exception) as e:
        print(f"Lỗi: {str(e)}")        
        
def key_free_by_ngtuw():
    global chars, pyver, ip, ngay, thang, nam 
    file_key = f"File_Key_Ngay_{ngay}.json"
    file_key_cu = f"File_Key_Ngay_{int(ngay)-1}.json"
    file_ip = "saved_ip.json"
    token = "6671b20e704d5f32b2048914"
    alias = "".join(random.sample([chr(i) for i in range(97, 123)], k=5))
    keyfree = [hashlib.md5(f"NTOOL - {ngay}{ip}{pyver}".encode()).hexdigest(), 'NhatDepTrai']
    url = f"https://key.c25tool.net/key.html?key={keyfree[0]}"
    link = None
    def save_ip():
        data = {'ip': ip}
        with open(file_ip, 'w') as f:
            json.dump(data, f)
    def check_ip():
        if os.path.exists(file_ip):
            with open(file_ip, 'r') as f:
                saved_data = json.load(f)
                saved_ip = saved_data.get('ip')
                if saved_ip != ip:
                    print("IP Hiện Tại Không Khớp Với IP Đã Lưu. Vui Lòng Kiểm Tra Lại Mạng.")
                    sys.exit()
        else:
            save_ip()
    check_ip()
    try:
        response = requests.get(f"https://link4m.co/api-shorten/v2?api={token}&url={url}&alias={alias}").json()
        if response['status'] == 'success':
            link = response['shortenedUrl']
        else:
            print(f"Lỗi: {response}")
            return
    except (requests.ConnectionError, requests.exceptions.ReadTimeout):
        print("Vui Lòng Kiểm Tra Kết Nối Mạng !!!")
        sys.exit()
    except (requests.exceptions.RequestException, Exception) as e:
        print(f"Lỗi: {str(e)}")    
    def enter_key():
        if os.path.exists(file_key_cu):
            os.system(f"rm {file_key_cu}")
        line(60)    
        print(f"{chars} Đây Là Tool Free Nên Mỗi Ngày 1 Key Nhé")    
        print(f"{chars} Key Sẽ Ở Sau Phần “key=” Của Url Nhé")    
        print(f"{chars} Hôm Nay Ngày {ngay} Tháng {thang} Năm {nam}")    
        if link:              
            print(f"{chars} Link > {link} <")
        else:
            print(f"{chars} Không Thể Lấy Link Rút Gọn. Vui Lòng Chạy Lại Tool!")
            sys.exit()
        while True:
            line(60)
            inp = input(f"{chars} Nhập Key: ")
            if inp in keyfree:  
                expiration_date = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
                data = {'key': inp, 'expiration_date': expiration_date.isoformat()}
                json.dump(data, open(file_key, 'w'))
                line(60)
                print(f"{chars} Đang Vào Tool Vui Lòng Đợi !")
                info_key = (f"""         >>> Thông Tin Key <<<
{chars} Loại Key (FREE)
{chars} Thời Gian: (1 Ngày) 
{chars} Thời Gian Còn Lại ({expiration_date})""")                  
                break
            else:
                line(60)
                print("Key Sai. Vui Lòng Nhập Lại !!!")
        return info_key       
    if not os.path.exists(file_key):
        info_key = enter_key()
    else:
        if os.path.exists(file_key_cu):
            os.system(f"rm {file_key_cu}")
        data = json.load(open(file_key, 'r'))
        inp = data['key']    
        expiration_date = datetime.fromisoformat(data['expiration_date'])
        start_new_day = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1) + timedelta(seconds=1)  
        if expiration_date <= start_new_day:
            if inp in keyfree:
                line(60)
                print(f"{chars} Đang Vào Tool Vui Lòng Đợi !")               
                info_key = (f"""         >>> Thông Tin Key <<<
{chars} Loại Key (FREE)
{chars} Thời Gian: (1 Ngày) 
{chars} Thời Gian Còn Lại ({expiration_date - datetime.now()})""")   
            else:
                line(60)
                print("Key Sai. Vui Lòng Nhập Lại !!!")
                info_key = enter_key()
        else:
            start_new_day
    return info_key

def tool(info_key):
    global chars, pyver, ip, ngay, thang, nam
    line(60)    
    print(info_key)
    line(60)
    print("         >>> Thông Tin User <<<")
    print(f"{chars} Version Python ({pyver})")
    print(f"{chars} IP ({ip})")
    print(f"{chars} Hôm Nay Ngày {ngay} Tháng {thang} Năm {nam}")     
    line(60)
    print("┌───────────────────┐")
    print("│ TOOL TRAO ĐỔI SUB │")
    print("└───────────────────┘")
    print(f"{chars} Nhập __[ 001 ]__ Tool Trao Đổi Sub Tiktok (Mobile + Computer)")
    print(f"{chars} Nhập __[ 002 ]__ Tool Trao Đổi Sub Facebook (Mobile + Computer)")
    print(f"{chars} Nhập __[ 003 ]__ Tool Trao Đổi Sub Fanpage (Mobile + Computer)")
    print(f"{chars} Nhập __[ 004 ]__ Tool Trao Đổi Sub Instagram (Mobile + Computer)")    
    print("┌─────────────────────┐")
    print("│ TOOL TƯƠNG TÁC CHÉO │")
    print("└─────────────────────┘")
    print(f"{chars} Nhập __[ 101 ]__ Tool Tương Tác Chéo Tiktok (Mobile + Computer)[OffLine]")
    print(f"{chars} Nhập __[ 102 ]__ Tool Tương Tác Chéo Facebook (Mobile + Computer)[OffLine]")
    print(f"{chars} Nhập __[ 103 ]__ Tool Tương Tác Chéo Fanpage (Mobile + Computer)")
    print(f"{chars} Nhập __[ 104 ]__ Tool Tương Tác Chéo Instagram (Mobile + Computer)")
    print("┌─────────────┐")
    print("│ TOOL GOLIKE │")
    print("└─────────────┘")
    print(f"{chars} Nhập __[ 201 ]__ Tool Golike Tiktok (Mobile + Computer)")
    print(f"{chars} Nhập __[ 202 ]__ Tool Golike Tiktok Tự Động (Mobile + Computer)")
    print(f"{chars} Nhập __[ 203 ]__ Tool Golike Instagram (Mobile + Computer)")
    print(f"{chars} Nhập __[ 204 ]__ Tool Golike Twitter (Mobile + Computer)")
    print(f"{chars} Nhập __[ 205 ]__ Tool Golike YouTube (Mobile + Computer)")
    print(f"{chars} Nhập __[ 206 ]__ Tool Golike Thread (Mobile + Computer)")
    print(f"{chars} Nhập __[ 207 ]__ Tool Golike Linkedin (Mobile + Computer)") 
    print("┌─────────────┐")
    print("│ TOOL TIỆN ÍCH│")
    print("└─────────────┘")
    print(f"{chars} Nhập __[ 208 ]__ Tool Tấn Công Web (Mobile + Computer)") 
    print(f"{chars} Nhập __[ 209 ]__ Tool Spam Sms (Mobile + Computer)") 
    print(f"{chars} Nhập __[ 210 ]__ Tool Buff View TikTok (Mobile + Computer)") 
    print(f"{chars} Nhập __[ 211 ]__ Tool Buff FL TikTok (Mobile + Computer)") 
    while True:
        try:
            print("╔══════════════════════════════════════════════════════════╗")
            print("║ Vui Lòng Nhập Số Bạn Muốn Để Vào Tool ")
            choose = input(f"╚➤➤➤➤ ")
            if not choose.isdigit():
                line(60)
                print(f"{chars} Vui Lòng Chỉ Nhập Số !")
                continue   
        except Exception as e:
            print("Lỗi: {str(e)}")
            continue   
        break
    return choose   

def ngtuw_dep_trai_vcl(choose):
    line(60)
    if choose == "001":
        threading.Thread(target=custom_delay, args=("ĐANG VÀO TOOL SỐ ___[ 001 ]___ VUI LÒNG ĐỢI",)).start()
        chay_tool("https://raw.githubusercontent.com/Nhatp1/Nekoto/main/TDSTIKTOK.py")
    elif choose == '002':
        chay_tool("https://raw.githubusercontent.com/Nhatp1/Nekoto/main/TDSFULLJOB.py")
    elif choose == '003':
    	chay_tool("https://raw.githubusercontent.com/Nhatp1/Nekoto/main/TDSPRO5v1.py")
    elif choose == '004':
    	chay_tool("https://raw.githubusercontent.com/Nhatp1/Nekoto/main/TDSIG.py")
    elif choose == '101':
    	chay_tool(" ")
    elif choose == '102':
    	chay_tool(" ")
    elif choose == '103':
    	chay_tool("https://raw.githubusercontent.com/Nhatp1/Nekoto/main/TTCIG.py")
    elif choose == '104':
    	chay_tool("https://raw.githubusercontent.com/Nhatp1/Nekoto/main/TTCPRO5v1.py")
    elif choose == '201':
    	chay_tool("https://raw.githubusercontent.com/Nhatp1/Nekoto/main/AutoTikTokv1.py")
    elif choose == '202':
    	chay_tool("https://raw.githubusercontent.com/Nhatp1/Nekoto/main/AutoTikTokv2.py")
    elif choose == '203':
    	chay_tool("https://raw.githubusercontent.com/Nhatp1/Nekoto/main/AutoIG.py")
    elif choose == '204':
    	chay_tool("https://raw.githubusercontent.com/Nhatp1/Nekoto/main/AutoX.py")
    elif choose == '205':
    	chay_tool("https://raw.githubusercontent.com/Nhatp1/Nekoto/main/AutoYTB.py")
    elif choose == '206':
    	chay_tool("https://raw.githubusercontent.com/Nhatp1/Nekoto/main/AutoTheads.py")
    elif choose == '207':
    	chay_tool("https://raw.githubusercontent.com/Nhatp1/Nekoto/main/AutoLinkedin.py")
    elif choose == '209':
    	chay_tool("https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/SPAMSMSV1.py")
    elif choose == '208':
    	chay_tool("https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/DDOS.py")
    elif choose == '210':
    	chay_tool("https://raw.githubusercontent.com/Nhatp1/Nekoto/refs/heads/main/VIEWTIK.py")
    else:
        print(f"{chars} Lựa Chọn Không Hợp Lệ. Vui Lòng Nhập Lại !!")
        time.sleep(2)  
        return True  
        
if __name__ == '__main__':
    install_missing_modules()
    threading.Thread(target=check_connection, daemon=True).start()
    clear()
    banner()
    info_key = key_free_by_ngtuw()
    while True:
        clear()
        banner()
        choose = tool(info_key)
        valid_choice = ngtuw_dep_trai_vcl(choose)
        if valid_choice:  
            continue
        else:
            break  
import random
from atexit import register
from time import sleep
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
os.system("clear")
dau="\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m➩"
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
for h in banner:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.00003)
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
        banner()
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
    key1 = str(ngay * 279775598 + 2499976756)
    ip_numbers = ''.join(filter(str.isdigit, ip_address))
    key = f'PAP{key1}{ip_numbers}'
    keyvip = f'PAP8386'
    expiration_date = datetime.now().replace(hour=23, minute=59, second=59, microsecond=59)
    url = f'https://dichvutaphoa.x10.mx/Api/key-free/keytool.php?key={key}'
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
        token = "67fb49b8ef455711087542b1"  # Thay bằng API Token Của Bạn
        api_url = f"https://link4m.co/api-shorten/v2?api={token}&url={url}"

        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"status": "error", "message": "Không thể kết nối đến dịch vụ rút gọn URL."}
    except Exception as e:
        return {"status": "error", "message": f"Lỗi khi rút gọn URL: {e}"}

def main():
    ip_address = get_ip_address()
    display_ip_address(ip_address)

    if ip_address:
        existing_key = kiem_tra_ip(ip_address)
        if existing_key:
            print(f"\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;32mTool còn hạn,chờ 3s để load...")
            time.sleep(3)
        else:
            if da_qua_gio_moi():
                print("\033[1;32mQuá giờ sử dụng tool !!!")
                return

            url, key, expiration_date = generate_key_and_url(ip_address)

            with ThreadPoolExecutor(max_workers=2) as executor:
                print("\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;36mNhập 1 Để Lấy Key Hoặc Nhập KeyVIP\033[1;35m( Free )")

                while True:
                    try:
                        choice = input("\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;39mNhập lựa chọn: ")
                        print("\033[97m════════════════════════════════════════════════")
                        if choice == "1":
                            yeumoney_future = executor.submit(get_shortened_link_phu, url)
                            yeumoney_data = yeumoney_future.result()
                            if yeumoney_data and yeumoney_data.get('status') == "error":
                                print(yeumoney_data.get('message'))
                                return
                            else:
                                link_key_yeumoney = yeumoney_data.get('shortenedUrl')
                                print('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;32mLink Để Vượt Key Là \033[1;39m:', link_key_yeumoney)

                            while True:
                                keynhap = input('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mKey Đã Vượt Hoặc Đã Mua Là: \033[1;36m')
                                if keynhap == key or keyvip:
                                    print('Key Đúng Mời Bạn Dùng Tool Như Con Chym 😭')
                                    sleep(2)
                                    luu_thong_tin_ip(ip_address, keynhap, expiration_date)
                                    return
                                else:
                                    print('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mKey Sai Vui Lòng Vượt Lại Link \033[1;36m:', link_key_yeumoney)
                    except ValueError:
                        print("Vui lòng nhập số hợp lệ.")
                    except KeyboardInterrupt:
                        print("\n\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mCảm ơn bạn đã dùng Tool !!!")
                        sys.exit()


def logo():
    pass
import random
from collections import Counter
import os
import time
import sys
                                                                # Mã màu ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
AQUA = "\033[96m"
LIME = "\033[92m"
                                                                # Danh sách các phòng với tên viết tắt và tên đầy đủ
phong = {
    "NHÀ KHO": "NK",
    "PHÒNG HỌP": "PH",                                              "PHÒNG GIÁM ĐỐC": "PGD",
    "PHÒNG TRÒ CHUYỆN": "PTC",
    "PHÒNG GIÁM SÁT": "PGS",
    "VĂN PHÒNG": "VP",
    "PHÒNG TÀI VỤ": "PTV",
    "PHÒNG NHÂN SỰ": "PNS"
}

phong_keys = list(phong.values())

def hien_thi_danh_sach_phong():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{BOLD}{AQUA}DANH SÁCH PHÒNG VIẾT TẮT TOOL :{RESET}")
    for ten_phong, ten_viet_tat in phong.items():
        print(f"{BOLD}{BLUE}{ten_phong} ({ten_viet_tat}){RESET}")

def hien_thi_intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    intro_messages = [
        "ADMIN NP-TOOL CHÀO BẠN ĐÃ ĐẾN VỚI TOOL 💥",
        "TOOL HỖ TRỢ DỰ ĐOÁN TỈ SỐ VUA THOÁT HIỂM CHÍNH XÁC LÊN ĐẾN 90% ⚠️",
        "ADMIN  XIN ĐƯỢC PHÉP BẮT ĐẦU TOOL 💢",
        "NHẬP TÊN PHÒNG VIẾT TẮT MÀ SÁT THỦ ĐÃ VÀO TRẬN TRƯỚC ❗"
        "MUA FULL SCR VIP CỰC RẺ LIÊN HỆ ZALO 0394764859 30K DÙNG VĨNH VIỄN🎭 !"
    ]

    for message in intro_messages:
        print(f"{BOLD}{CYAN}{message}{RESET}")
        time.sleep(2)  # Hiển thị mỗi thông điệp trong 2 giây

    print(f"\n{BOLD}{GREEN}ĐANG TẢI VUI LÒNG CHỜ TÍ NHA⏰")

    # Hiệu ứng tải
    for i in range(1, 101):
        sys.stdout.write(f"\r{BOLD}{LIME}ĐANG LOADING: {i}% {'█' * (i // 5)}{RESET}")
        sys.stdout.flush()
        time.sleep(0.03)  # Điều chỉnh thời gian chờ nếu cần

    # Xóa màn hình sau khi tải xong
    os.system('cls' if os.name == 'nt' else 'clear')

hien_thi_intro()
hien_thi_danh_sach_phong()

while True:
    phong_satt_thu_da_vao = input ("Nhập Phòng Sát Thủ Đã Vào Trận Trước : ").strip()

    if phong_satt_thu_da_vao.lower() == 'exit':
        print(f"{BOLD}{AQUA}CẢM ƠN BẠN ĐÃ SỬ DỤNG TOOL!")

        break

    if phong_satt_thu_da_vao not in phong_keys:
        print("PHÒNG KHÔNG HỢP LỆ VUI LÒNG NHẬP LẠI ⚠.")
    else:
        so_lan_mo_phong = 1000000
        ket_qua_chon = [random.choice(phong_keys) for _ in range(so_lan_mo_phong)]
        dem_phong = Counter(ket_qua_chon)
        xac_suat_phong = {phong_key: dem_phong[phong_key] / so_lan_mo_phong for phong_key in phong_keys}

        phong_thap_nhat = min(xac_suat_phong, key=xac_suat_phong.get)
        xac_suat_phong_thap_nhat_pt = xac_suat_phong[phong_thap_nhat] * 100
        phan_tram_con_lai = 100 - xac_suat_phong_thap_nhat_pt

        ten_phong_thap_nhat = [name for name, code in phong.items() if code == phong_thap_nhat][0]

        hien_thi_danh_sach_phong()

        for i in range(1, 101):
            sys.stdout.write(f"\r{BOLD}{LIME}BẮT ĐẦU DỰ ĐOÁN: {i}% {'█' * (i // 5)}{RESET}")
            sys.stdout.flush()
            time.sleep(0.03)

        print(f"\n{BOLD}{AQUA}PHÒNG NÊN CHỌN: {RESET}{BOLD}{BLUE}{ten_phong_thap_nhat} ({phong_thap_nhat}){RESET}")
        print(f"{BOLD}{YELLOW}TỈ LỆ AN TOÀN LÀ: {RESET}{phan_tram_con_lai:.2f}%")

#/c/ea991b37-e128-4c96-bfa6-54b7e9abf68c
import hashlib
import random
import requests
import time
from datetime import datetime
import json
import sys
import urllib3

mo_ngoac_1 = "\033[1m["
mo_ngoac = "\033[1m[\x1b[1;38;2;173;255;47m"  # dấu [ xanh chuối
dong_ngoac = "\033[0m\033[1m]"  # dấu ]
mo_ngoac_do = "\033[0m\033[1m[\033[1;31m"   # dấu [ màu đỏ
mo_ngoac_xl = "\033[0m\033[1m[\033[1;32m"  # dấu [ xanh lá
mo_ngoac_cam = "\033[0m\033[1m[\x1b[1;38;2;255;165;0m"  # dấu [ cam
mo_ngoac_xd = "\033[0m\033[1m[\x1b[1;38;2;135;206;250m"  # dấu [ xanh dương
mo_ngoac_hong = "\033[0m\033[1m[\x1b[1;38;2;255;182;193m"  # dấu [ hồng

# Màu
xanhchuoi = "\x1b[1;38;2;173;255;47m"  # xanh chuối
xanhla = "\033[1;32m"  # xanh lá
do = "\033[1;31m"  # đỏ
trang = "\x1b[1;38;2;233;233;233m"  # trắng đậm
resetmau = "\033[0m\33[1m"  # đặt lại màu
xanhduong = "\x1b[1;38;2;135;206;250m"  # xanh d nhạt
hong = "\x1b[1;38;2;255;182;193m"  # hồng nhạt
cam = "\x1b[1;38;2;255;165;0m"  # cam

# Thanh gạch
que = ''.join(['─'] * 50)
thanh = f"{xanhduong}{que}{resetmau}"
gach = ''.join(['═'] * 20)

# Vô hiệu hóa các cảnh báo InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Cấu hình API và Key
app = {
    'api_key': '882a8490361da98702bf97a021ddc14d',
    'secret': '62f8ce9f74b12f84c123cc23437a4a32',
    'key': ['ChanHungCoder_KeyRegFBVIP_9999', 'DCHVIPKEYREG']
}

email_prefix = [
    'gmail.com',
    'hotmail.com',
    'yahoo.com',
    'live.com',
    'rocket.com',
    'outlook.com',
]

# Hàm tạo tài khoản
def create_account():
    # Tạo ngày sinh ngẫu nhiên
    random_birth_day = datetime.strftime(datetime.fromtimestamp(random.randint(
        int(time.mktime(datetime.strptime('1980-01-01', '%Y-%m-%d').timetuple())),
        int(time.mktime(datetime.strptime('1995-12-30', '%Y-%m-%d').timetuple()))
    )), '%Y-%m-%d')

    # Danh sách tên
    names = {
        'first': ['JAMES', 'JOHN', 'ROBERT', 'MICHAEL', 'WILLIAM', 'DAVID'],
        'last': ['SMITH', 'JOHNSON', 'WILLIAMS', 'BROWN', 'JONES', 'MILLER'],
        'mid': ['Alexander', 'Anthony', 'Charles', 'Dash', 'David', 'Edward']
    }

    # Tạo tên ngẫu nhiên
    random_first_name = random.choice(names['first'])
    random_name = f"{random.choice(names['mid'])} {random.choice(names['last'])}"
    password = f'ChanHungCoder{random.randint(0, 9999999)}?#@'
    full_name = f"{random_first_name} {random_name}"
    md5_time = hashlib.md5(str(time.time()).encode()).hexdigest()

    # Tạo hash và email ngẫu nhiên
    hash_ = f"{md5_time[0:8]}-{md5_time[8:12]}-{md5_time[12:16]}-{md5_time[16:20]}-{md5_time[20:32]}"
    email_rand = f"{full_name.replace(' ', '').lower()}{hashlib.md5((str(time.time()) + datetime.strftime(datetime.now(), '%Y%m%d')).encode()).hexdigest()[0:6]}@{random.choice(email_prefix)}"
    gender = 'M' if random.randint(0, 10) > 5 else 'F'

    # Tạo yêu cầu đăng ký
    req = {
        'api_key': app['api_key'],
        'attempt_login': True,
        'birthday': random_birth_day,
        'client_country_code': 'EN',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': random_first_name,
        'format': 'json',
        'gender': gender,
        'lastname': random_name,
        'email': email_rand,
        'locale': 'en_US',
        'method': 'user.register',
        'password': password,
        'reg_instance': hash_,
        'return_multiple_errors': True
    }

    sig = ''.join([f'{k}={v}' for k, v in sorted(req.items())])
    ensig = hashlib.md5((sig + app['secret']).encode()).hexdigest()
    req['sig'] = ensig

    api = 'https://b-api.facebook.com/method/user.register'

    def _call(url='', params=None, post=True):
        headers = {
            'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'
        }
        if post:
            response = requests.post(url, data=params, headers=headers, verify=False)
        else:
            response = requests.get(url, params=params, headers=headers, verify=False)
        return response.text

    reg = _call(api, req)
    reg_json = json.loads(reg)
    uid = reg_json.get('session_info', {}).get('uid')
    access_token = reg_json.get('session_info', {}).get('access_token')

    # Nếu có lỗi, sẽ có các khóa error_code và error_msg trong JSON
    error_code = reg_json.get('error_code')
    error_msg = reg_json.get('error_msg')

    if uid is not None and access_token is not None:
        data_to_save = f"{random_birth_day}:{full_name}:{email_rand}:{password}:{uid}:{access_token}"
        
        with open(file_name, "a") as file:
            file.write(data_to_save + "\n")
        # In thông tin ra màn hình
        print("Birthday:", random_birth_day)
        print("Fullname:", full_name)
        print("Email:", email_rand)
        print("Password:", password)
        print("UID:", uid)
        print("Token:", access_token)
        print(thanh)
    else:
        # Nếu có lỗi, in mã lỗi và thông báo lỗi
        if error_code and error_msg:
            print(f"Error Code: {error_code}")
            print(f"Error Message: {error_msg}")
        else:
            print(f"{do}Unknown error occurred.{resetmau}")
        print(f"{mo_ngoac_cam}×{dong_ngoac} Không Thể Lưu Thông Tin. Vui Lòng Đợi Reg Lại!")

while True:
    try:
        account_count = int(input(f"{mo_ngoac}*{dong_ngoac} Nhập Số Lượng Acc Muốn Reg: "))
        if account_count > 0:
            break
        else:
            print(f"{mo_ngoac_do}!{dong_ngoac} Số Lượng Acc Phải Lớn Hơn 0. Vui Lòng Nhập lại!")
    except ValueError:
        print(f"{mo_ngoac_do}!{dong_ngoac} Nội Dung Nhập Không Hợp Lệ!")

while True:
    file_name = input(f"{mo_ngoac}*{dong_ngoac} Nhập Tên File Lưu Thông Tin: ")
    if file_name.strip():
        if not file_name.endswith(".txt"):
            file_name += ".txt"
        break
    else:
        print(f"{mo_ngoac_do}!{dong_ngoac} Tên File Không Được Để Trống. Vui Lòng Nhập Lại!")

while True:
    try:
        delay = int(input(f"{mo_ngoac}*{dong_ngoac} Nhập Thời Gian Delay (Trên 180 Giây): "))
        if delay > 10:
            break
        else:
            print(f"{mo_ngoac_do}!{dong_ngoac} Delay Phải Lớn Hơn 179 Giây. Vui Lòng Nhập Lại!")
    except ValueError:
        print(f"{mo_ngoac_do}!{dong_ngoac} Nội Dung Nhập Không Hợp Lệ!")

print(thanh)

for _ in range(account_count):
    create_account()
    
    print(f"Chờ {delay} Giây...", end='')
    for remaining in range(delay, 0, -1):
        print(f"\r{mo_ngoac}*{dong_ngoac} Vui Lòng Đợi: {remaining} Giây", end='', flush=True)
        time.sleep(1)
    print()
    print(thanh)

print(f"{mo_ngoac}✓{dong_ngoac} Tất Cả Thông Tin Đã Được Lưu Vào File: {xanhchuoi}{file_name}{resetmau}")
sys.exit()

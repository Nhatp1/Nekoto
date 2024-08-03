from time import sleep
import re
import requests
import colorama
colorama.init()


def display():
    print("""
\033[1;91m|==============================================================================================|\033[0m
\033[1;91m|                                           \033[1;36m[1] Tool like tây Fb đa cookie                     \033[1;91m|\033[0m
\033[1;91m|  ▒███████▒ ▒█████   ██ ▄█▀ ██▒▒█████      \033[1;36m[2] Admin: NHAT TOOL              \033[1;91m|\033[0m
\033[1;91m|  ▒ ▒ ▒ ▄▀░▒██▒  ██▒ ██▄█▒ ▓██▒▒█   ▀      \033[1;36m[3] \033[32;1m          \033[1;91m|\033[0m
\033[1;91m|  ░ ▒ ▄▀▒░ ▒██░  ██▒▓███▄░ ▒██▒▒███        \033[1;36m[4] \033[32;1m     \033[1;91m|\033[0m
\033[1;91m|    ▄▀▒   ░▒██   ██░▓██ █▄ ░██░▒▓█  ▄      \033[1;36m[5] \033[32;1m        \033[1;91m|\033[0m
\033[1;91m|  ▒███████▒░ ████▓▒░▒██▒ █▄░██░░▒████▒     \033[1;36m[6]         \033[1;91m|\033[0m
\033[1;91m|  ░▒▒ ▓░▒░▒░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▓  ░░ ▒░ ░     \033[1;36m[7]     \033[1;91m|\033[0m
\033[1;91m|  ░░▒ ▒ ░ ▒  ░ ▒ ▒░ ░ ░▒ ▒░ ▒ ░ ░ ░  ░     \033[1;36m[8]    \033[1;91m|\033[0m
\033[1;91m|  ░ ░ ░ ░ ░░ ░ ░ ▒  ░ ░░ ░  ▒ ░   ░        \033[1;36m[9] \033[32;1m  \033[1;91m|\033[0m
\033[1;91m|    ░ ░        ░ ░  ░  ░    ░     ░  ░     \033[1;36m[10] ......................................        \033[1;91m|\033[0m
\033[1;91m|==============================================================================================|\033[0m

""")


def nghigiailao(o):
    while o > 0:
        o -= 1
        print(f"\033[1;37m[DELAY][X    ][{o}]", end='\r')
        sleep(1 / 5)
        print(f"\033[1;37m[DELAY][ X   ][{o}]", end='\r')
        sleep(1 / 5)
        print(f"\033[1;37m[DELAY][  X  ][{o}]", end='\r')
        sleep(1 / 5)
        print(f"\033[1;37m[DELAY][   X ][{o}]", end='\r')
        sleep(1 / 5)
        print(f"\033[1;37m[DELAY][    X][{o}]", end='\r')
        sleep(1 / 5)


class Machine:
    def __init__(self):
        self.session = []
        self.delay = 0
        self.url = None
        self.dict_buff = {'1': 'like', '2': 'love', '3': 'care', '4': 'haha', '5': 'wow', '6': 'sad', '7': 'angry'}
        self.list_select = []
        self.headers_buff = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'vi-VN,vi;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-AU;q=0.6,en;q=0.5,fr-FR;q=0.4,fr;q=0.3,en-US;q=0.2',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A037F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
        }
        self.cookies = open('cookie.txt').read().split("\n")
        self.dem = 0

    def buff(self, session):
        get_token = session.get('https://machineliker.net/auto-reactions').text
        token = get_token.split('name="_token" value="')[1].split('"')[0]
        hash_ = get_token.split('name="hash" value="')[1].split('"')[0]
        data_buff = {
            'url': self.url,
            'limit': '20',
            'reactions[]': self.list_select,
            '_token': token,
            'hash': hash_
        }
        response = session.post('https://machineliker.net/auto-reactions', headers=self.headers_buff,
                                data=data_buff).text
        if '><strong>Error!</strong>' and "You're currently under cooldown periods, please try again after" in response:
            count = re.findall(r'please try again after (\d+) minutes.</p>', response)[0]
            second = int(count) * 60
            print(f"Sorry Vui Lòng Đợi {second}s Nữa")
            self.delay = second
        elif 'Order Submitted' in response:
            self.dem += 1
            print(f"Tăng Thành Công +20 Cảm Xúc [\033[32;1m{self.dem}\033[0m]")
            self.delay = 1200
        else:
            print("Lỗi")

    def main(self):
        for ckfb in self.cookies:
            session = requests.Session()
            if ckfb == '':
                break
            a = session.get('https://machineliker.net/login')
            self.headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'vi-VN,vi;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-AU;q=0.6,en;q=0.5,fr-FR;q=0.4,fr;q=0.3,en-US;q=0.2',
                'content-type': 'application/x-www-form-urlencoded',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A037F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                'x-xsrf-token': session.cookies.get('XSRF-TOKEN').replace('%3D', '='),
            }
            data = {
                'session': ckfb
            }
            response = session.post('https://machineliker.net/login', headers=self.headers, data=data).json()
            if response['success']:
                name = response['user']['name']
                id_ = response['user']['id']
                print(f"Login Thành Công: \033[32;1m{id_}\033[0m | \033[32;1m{name}\033[0m")
                self.session.append(session)
            else:
                print(f"Login That Bai! Kiem Tra Lai Cookie FB \033[1;91m{ckfb.split('c_user=')[1].split(';')[0]}\033[0m")
        self.url = input("Url bài viết cần buff: ")
        print("Chọn loại cảm xúc cần buff (có thể chọn nhiều ví dụ 123")
        print("""\033[32;1m
                1: like
                2: love
                3: care
                4: haha
                5: wow
                6: sad
                7: angry
            \033[0m""")
        select = input("Nhập số: ")
        self.list_select = [self.dict_buff[x] for x in select]
        while True:
            for session in self.session:
                self.buff(session)
            nghigiailao(self.delay)


display()
Machine().main()

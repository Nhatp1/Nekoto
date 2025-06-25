import json
import os,time
import cloudscraper
import webbrowser
import requests
import socket
import urllib.parse
import subprocess
from time import strftime
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import time
from colorama import Fore, init
import sys

cookie_file = "twitter_cookie.txt"

banner = f"""
{Fore.CYAN}██████╗░██╗░░██╗██╗░░░██╗░█████╗░░█████╗░
{Fore.YELLOW}██╔══██╗██║░░██║██║░░░██║██╔══██╗██╔══██╗
{Fore.RED}██████╔╝███████║██║░░░██║██║░░██║██║░░╚═╝
{Fore.MAGENTA}██╔═══╝░██╔══██║██║░░░██║██║░░██║██║░░██╗
{Fore.RED}██║░░░░░██║░░██║╚██████╔╝╚█████╔╝╚█████╔╝
{Fore.GREEN}╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░░╚════╝░░╚════╝░
"""

os.system('cls' if os.name== 'nt' else 'clear')
print(banner)
print("\033[1;39m╔═════════════════════════════════╗")
print("\033[1;39m║     \033[1;36mĐĂNG NHẬP GOLIKE AUTH       \033[1;39m║")
print("\033[1;39m╚═════════════════════════════════╝") 

    # Nhập auth
try:
  Authorization = open("Authorization.txt","x")
  t = open("token.txt","x")
except:
  pass
Authorization = open("Authorization.txt","r")
t = open("token.txt","r")
author = Authorization.read()
token = t.read()
if author == "":
  author = input("\033[1;32m 💸 NHẬP AUTHORIZATION GOLIKE : \033[1;33m")
  token = input("\033[1;32m💸  NHẬP TOKEN (T CỦA GOLIKE): \033[1;33m")
  Authorization = open("Authorization.txt","w")
  t = open("token.txt","w")
  Authorization.write(author)
  t.write(token)
else:
  print(f"\033[1;32mNhập 1 để vào TOOL Golike Twitter 💸🤑")
  print(f"\033[1;96mHOẶC LÀ ")
  select = input(f"\033[1;32mNhập AUTHORIZATION {Fore.CYAN}Ở đây \033[1;32mđể vào acc golike khác : \033[1;33m")
  if select != "1":
    author = select
    token = input("\033[1;32m Nhập T (token golike) : \033[1;33m")
    Authorization = open("Authorization.txt","w")
    t = open("token.txt","w")
    Authorization.write(author)
    t.write(token)
Authorization.close()
t.close()
os.system('cls' if os.name== 'nt' else 'clear')
print(banner)
print("\033[1;39m╔═════════════════════════════════════════╗")
print("\033[1;39m║   \033[1;36m DANH SÁCH ACC TWITTER  ĐÃ CẤU HÌNH   \033[1;39m║")
print("\033[1;39m╚═════════════════════════════════════════╝")  
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/twitter',
}

scraper = cloudscraper.create_scraper()
def chonacc():
    json_data = {}
    response = scraper.get(
        'https://gateway.golike.net/api/twitter-account',
        headers=headers,
        json=json_data
    ).json()
    return response

def nhannv(account_id):
    try:
        params = {
            'account_id': account_id,
            'data': 'null',
        }

        response = scraper.get(
            'https://gateway.golike.net/api/advertising/publishers/twitter/jobs',
            headers=headers,
            params=params,
            json={}
        )
        return response.json()
    except Exception as e:
        print()
        return {}

def parse_cookie_string(cookie_str):
    return {item.split("=")[0]: "=".join(item.split("=")[1:]) for item in cookie_str.split("; ")}

def create_headers(cookie_str, referer_link="https://x.com/"):
    cookies = parse_cookie_string(cookie_str)
    return {
        "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        "x-csrf-token": cookies.get("ct0", ""),
        "x-twitter-auth-type": "OAuth2Session",
        "x-twitter-active-user": "yes",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36",
        "referer": referer_link,
        "content-type": "application/x-www-form-urlencoded",
    }, cookies

def like_tweet(tweet_id, cookie_str):
    url = "https://x.com/i/api/1.1/likes/create.json"
    
    headers, cookies = create_headers(cookie_str, f"https://x.com/i/web/status/{tweet_id}")
    headers.update({
        "content-type": "application/json",
        "referer": f"https://x.com/i/web/status/{tweet_id}",
    })
    
    payload = {"tweet_mode": "extended", "id": tweet_id}

    try:
        response = requests.post(url, headers=headers, cookies=cookies, json=payload)
        if response.status_code == 200 and '"favorited":true' in response.text:
            print(f"\033[1;32m Like job thành công  💸 tweet_id={tweet_id}")
            return True
        else:
            print(f"\033[1;31m Like lỗi do acc, kiểm tra lại cookie!")
    except Exception as e:
        print(f"\033[1;31m Lỗi Like hoặc do job!")
    return False


def follow_twitter(user_id, cookie_str):
    headers, cookies = create_headers(cookie_str, f"https://x.com/i/user/{user_id}")
    url = f"https://api.twitter.com/1.1/friendships/create.json?user_id={user_id}&follow=true"
    try:
        response = requests.post(url, headers=headers, cookies=cookies)
        if response.status_code == 200 and '"following":true' in response.text:
            print(f"\033[1;32m Follow job thành công 💸 user_id={user_id}")
            return True
        else:
            print(f"\033[1;31m Follow lỗi do acc, kiểm tra lại cookie!!")
    except Exception as e:
        print(f"\033[1;31m Lỗi Follow hoặc do job!")
    return False

def hoanthanh(ads_id, account_id):
    try:
        json_data = {
            'ads_id': ads_id,
            'account_id': account_id,
            'async': True,
            'data': None,
        }

        response = scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs',
            headers=headers,
            json=json_data,
            timeout=6
        )
        return response.json()
    except Exception as e:
        print()
        return {}

def baoloi(ads_id, object_id, account_id, loai):
    try:
        json_data1 = {
            'description': 'Tôi đã làm Job này rồi',
            'users_advertising_id': ads_id,
            'type': 'ads',
            'provider': 'twitter',
            'fb_id': account_id,
            'error_type': 6,
        }

        scraper.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1)

        json_data2 = {
            'ads_id': ads_id,
            'object_id': object_id,
            'account_id': account_id,
            'type': loai,
        }

        scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs',
            headers=headers,
            json=json_data2,
        )
    except Exception as e:
        print()

# Gọi chọn tài khoản một lần và xử lý lỗi nếu có
chontkTwitter = chonacc()

def dsacc():
    if chontkTwitter.get("status") != 200:
        print("\033[1;31m Authorization hoặc Token sai !!!")
        quit()

    data = chontkTwitter.get("data", [])
    if not data:
        print("\033[1;33mKhông có tài khoản X nào được tìm thấy.")
        return

    for i, acc in enumerate(data):
        nickname = acc.get("id")
        print(f'\033[1;20m[{i+1}]\033[1;93m {nickname} \033[1;97m|\033[1;31m✅\033[1;32m Online ')
dsacc()
print(f"{Fore.MAGENTA}═══════════════════════════════════")
while True:
  try:
    luachon = int(input("\033[1;32m Chọn tài khoản Twitter: \033[1;33m"))
    while luachon > len((chontkTwitter)["data"]):
      luachon = int(input("\033[1;32m Acc Này Không Có Trong Danh Sách , Nhập Lại : \033[1;33m"))
    account_id = chontkTwitter["data"][luachon - 1]["id"]
    break  
  except:
    print("\033[1;31m Sai Định Dạng ") 
while True:
  try:
    delay = int(input(f"\033[1;32m Delay thực hiện : \033[1;33m"))
    break
  except:
    print("\033[1;31m Sai Định Dạng ")
twitter_cookie = ""
if os.path.exists(cookie_file):
    with open(cookie_file, "r", encoding="utf-8") as f:
        twitter_cookie = f.read().strip()

    if twitter_cookie:
        new_cookie = input(f"\033[1;32m Nhấn enter dùng Cookie cũ {Fore.BLUE}hoặc \033[1;32mnhập cookie mới {Fore.RED}Ở đây!\033[1;32m: \033[1;33m").strip()

        if new_cookie:
            twitter_cookie = new_cookie
            with open(cookie_file, "w", encoding="utf-8") as f:
                f.write(twitter_cookie)
            print("\033[1;36m 💸Đã lưu cookie mới.")
        else:
            print("\033[1;36m 💸Tiếp tục dùng cookie cũ.")
    else:
        twitter_cookie = input("\033[1;32m Nhập COOKIE TWITTER 🤑 : \033[1;33m").strip()
        with open(cookie_file, "w", encoding="utf-8") as f:
            f.write(twitter_cookie)
        print("\033[1;36m💸 Đã lưu cookie lần đầu dùng tool!")
else:
    twitter_cookie = input("\033[1;32m Nhập COOKIE TWITTER lần đầu: \033[1;33m").strip()
    with open(cookie_file, "w", encoding="utf-8") as f:
        f.write(twitter_cookie)
    print("\033[1;36m 💸Đã lưu cookie lần đầu.")
while True:
  try: 
    doiacc = int(input(f"\033[1;32m Thất bại bao nhiêu lần thì dừng tool: \033[1;33m"))
    break
  except:
    print("\033[1;31m Nhập Vào 1 Số ")  
print("\033[1;35m╔═════════════════════════════════════════╗")
print("\033[1;35m║     \033[1;33m CHỌN LOẠI JOB MUỐN KIẾM TIỀN   💸        \033[1;35m║")
print("\033[1;35m╚═════════════════════════════════════════╝")
print("\033[1;36m[1] Job Follow 💸")
print("\033[1;36m[2] Job Like 💸")
print("\033[1;36m[3] Cả hai Job 💸 (Follow và Like)")

while True:
    try:
        loai_nhiem_vu = int(input("\033[1;32mChọn loại JOB muốn chạy : \033[1;33m"))
        if loai_nhiem_vu in [1, 2, 3]:
            break
        else:
            print("\033[1;31mVui lòng chọn số từ 1 đến 3!")
    except:
        print("\033[1;31mSai định dạng! Vui lòng nhập số.")  
# Thêm phần chọn loại nhiệm vụ sau khi chọn tài khoản và trước khi bắt đầu làm nhiệm vụ
ads_id_da_lam = set()
object_id_da_lam = set()
dem = 0
lap_lai_ads = 0
tong = 0
checkdoiacc = 0
dsaccloi = []
accloi = ""
os.system('cls' if os.name== 'nt' else 'clear')

print(banner)
print("\033[1;39m╔═════════════════════════════════════════╗")
print("\033[1;39m║     \033[1;96m Bắt Đầu Bú Job + Kiếm Tiền 😈                 \033[1;39m║")
print("\033[1;39m╚═════════════════════════════════════════╝")

while True:
    if checkdoiacc == doiacc:
        print(f"{Fore.GREEN} Đã lỗi {doiacc} lần, tự động dừng tool 😠{Fore.WHITE}")
        exit()
    max_retries = 3
    retry_count = 0
    nhanjob = None

    while retry_count < max_retries:
        try:
            nhanjob = nhannv(account_id)
            if nhanjob and nhanjob.get("status") == 200 and nhanjob["data"].get("link") and nhanjob["data"].get("object_id"):
                break
            else:
                retry_count += 1
                time.sleep(2)
        except Exception as e:
            retry_count += 1
            time.sleep(1)

    if not nhanjob or retry_count >= max_retries:
        continue

    ads_id = nhanjob["data"]["id"]
    if ads_id in ads_id_da_lam:
       lap_lai_ads += 1
       print(f"\033[1;33m⚠️ Bỏ qua job trùng : ads_id={ads_id} ({lap_lai_ads} lần)")

    # Nếu job trùng lặp quá 5 lần, báo lỗi lên GoLike rồi bỏ qua hoàn toàn
    if lap_lai_ads >= 5:
        baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
        print("\033[1;35m Đã báo lỗi job trùng quá nhiều...")
        lap_lai_ads = 0
        time.sleep(5)  # nghỉ 5 giây tránh spam server

        continue
    else:
        lap_lai_ads = 0  # reset nếu có job mới

    ads_id_da_lam.add(ads_id)

    if len(ads_id_da_lam) > 100:
        ads_id_da_lam = set(list(ads_id_da_lam)[-100:])


    link = nhanjob["data"]["link"]
    object_id = nhanjob["data"]["object_id"]
    if object_id in object_id_da_lam:
      print(f"\033[1;33m 💸 Đã follow/like job object_id={object_id} trước đó. Bỏ qua Job.")
      baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
      time.sleep(2)
      continue

    job_type = nhanjob["data"]["type"]

    # Kiểm tra loại nhiệm vụ
    if (loai_nhiem_vu == 1 and job_type != "follow") or \
       (loai_nhiem_vu == 2 and job_type != "like") or \
       (job_type not in ["follow", "like"]):
        baoloi(ads_id, object_id, account_id, job_type)
        continue

    # Mở link và kiểm tra lỗi
    # Thực hiện job bằng cookie Twitter
    try:
        success = False
        if job_type == "follow":
            success = follow_twitter(object_id, twitter_cookie)
        elif job_type == "like":
            success = like_tweet(object_id, twitter_cookie)
        else:
            baoloi(ads_id, object_id, account_id, job_type)
            continue

        if not success:
            baoloi(ads_id, object_id, account_id, job_type)
            checkdoiacc += 1
            continue

        # Đếm ngược delay
        for remaining_time in range(delay, -1, -1):
            color = "\033[1;36m" if remaining_time % 2 == 0 else "\033[1;33m"
            print(f"\r{color} 💸 PAP |TOOL-V3| {remaining_time}s           ", end="")
            time.sleep(1)

        print("\r                          \r", end="") 
        print("\033[1;36m 💹 Đang Nhận Tiền,Chờ 1 Chút...", end="\r")
    except Exception as e:
        print(f"\033[1;31m Lỗi thực hiện job : {e}")
        baoloi(ads_id, object_id, account_id, job_type)
        checkdoiacc += 1
        continue

    # Hoàn thành job
    max_attempts = 2
    attempts = 0
    nhantien = None
    while attempts < max_attempts:
        try:
            nhantien = hoanthanh(ads_id, account_id)
            if nhantien and nhantien.get("status") == 200:
                break
        except:
            pass  
        attempts += 1

    if nhantien and nhantien.get("status") == 200:
        object_id_da_lam.add(object_id)
    if len(object_id_da_lam) > 200:
        object_id_da_lam = set(list(object_id_da_lam)[-100:])
        dem += 1
        tien = nhantien["data"]["prices"]
        tong += tien
        local_time = time.localtime()
        hour = local_time.tm_hour
        minute = local_time.tm_min
        second = local_time.tm_sec
        h = hour
        m = minute
        s = second
        if hour < 10:
            h = "0" + str(hour)
        if minute < 10:
            m = "0" + str(minute)
        if second < 10:
            s = "0" + str(second)
                                      
        chuoi = (f"\033[1;35m[\033[1;31m{dem}\033[1;35m]"
                f" \033[1;35m[\033[1;32mDc Tiền Rùi\033[1;35m]"
                f" \033[1;35m[\033[38;2;0;180;255m{job_type}\033[1;35m]"
                f" \033[1;35m[\033[1;33m+{tien}\033[1;35m]"
                f" \033[1;35m[\033[1;33mTổng số tiền đã kiếm dc : {tong}\033[1;35m]"
)
        print("                                                    ", end="\r")
        print(chuoi)
        time.sleep(0.7)
        checkdoiacc = 0
    else:
        try:
            baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
            print("                                              ", end="\r")
            print("\033[1;31m Bỏ qua nhiệm vụ do job die link 😭!!!", end="\r")
            sleep(1)
            checkdoiacc += 1
        except:
            pass

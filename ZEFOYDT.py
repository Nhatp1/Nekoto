import requests,re,time,base64,os
from prettytable import PrettyTable
from colorama import init, Fore
from urllib.parse import urlparse, unquote, quote
from string import ascii_letters, digits
os.system("cls" if os.name == "nt" else "clear")

class ApiZefoy:
  def __init__(self) -> None:
    self.zefoy = "https://zefoy.com"
    self.headers = {
      'authority': 'zefoy.com',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
      'cache-control': 'max-age=0',
      'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36'
    }
    self.session = requests.Session()
    self.session.headers.update(self.headers)
    self.captcha = {}
    self.captcha_1 = None
    self.captcha_name = 'captcha_zefoy.png'
    self.services = {}
    self.services_ids = {}
    self.services_status = {}
    self.url = input("Nhập link video: ")
  
  def get_captcha(self):
    main = self.session.get(self.zefoy)
    try:
      self.captcha_1 = main.text.split('type="text" name="')[1].split('"')[0]
      self.session.headers.update({"cookie": f"PHPSESSID={self.session.cookies['PHPSESSID']}"})
      captcha_img = self.session.post(self.zefoy+main.text.split('<img src="')[1].split('"')[0].replace("amp;", "")).content
      open(self.captcha_name, "wb").write(captcha_img)
      print('</> Đang giải capcha...')
      return False
    except Exception as e:
      print(f"</> Không thể giải captcha: {e}")
      time.sleep(2)
      self.get_captcha()
  
  def solve_captcha(self):
    files = {'file': open(self.captcha_name, "rb"),'language': (None, 'eng'),'isOverlayRequired': (None, 'true'),'FileType': (None, '.Auto'),'IsCreateSearchablePDF': (None, 'false'),'isSearchablePdfHideTextLayer': (None, 'true'),'detectOrientation': (None, 'false'),'isTable': (None, 'false'),'scale': (None, 'true'),'OCREngine': (None, '1'),'detectCheckbox': (None, 'false'),'checkboxTemplate': (None, '0')}
    rq = requests.post('https://api8.ocr.space/parse/image', headers={'apikey': 'donotstealthiskey_ip1'}, files=files).json()
    key = rq['ParsedResults'][0]['ParsedText'].replace("\r\n","")
    return key
  
  def giai_captcha(self):
    self.get_captcha()
    giai_captcha = self.solve_captcha()
    self.captcha[self.captcha_1] = giai_captcha
    rq = self.session.post("https://zefoy.com/", data=self.captcha)
    if 'Enter Video URL' in rq.text:
      self.session.cookies.update({"PHPSESSID": self.session.cookies['PHPSESSID']})
      print(f"</> Giải capcha thành công: {giai_captcha}")
      self.video_key = rq.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]
  
  def get_status_services(self):
    rq = self.session.get(self.zefoy, headers=self.headers).text
    for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+\n.+', rq):
      self.services[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = x.split('d-sm-inline-block">')[1].split('</small>')[0].strip()
    for x in re.findall(r'<h5 class="card-title mb-3">.+</h5>\n<form action=".+">', rq):
      self.services_ids[x.split('title mb-3">')[1].split('<')[0].strip()] = x.split('<form action="')[1].split('">')[0].strip()
    for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+<button .+', rq):
      if 'disabled class' in x:
        self.services_status[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = False
      else:
        self.services_status[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = True
    return (self.services, self.services_status)

  def get_table(self):
    i = 1
    table = PrettyTable(field_names=["ID", "DỊCH VỤ", "Status"], title="Status Services", header_style="upper",border=True)
    while True:
      if len(self.get_status_services()[0])>1:
        break
      else:
        print('Không có sever nào hoạt động. Thử lại...')
        self.giai_captcha()
        time.sleep(3)
    for service in self.services:
      table.add_row([f"{Fore.CYAN}{i}{Fore.RESET}", service, f"{Fore.GREEN if 'ago updated' in self.services[service] else Fore.RED}{self.services[service]}{Fore.RESET}"])
      i += 1
    table.title =  f"{Fore.YELLOW}Số Dịch Vụ Hoạt Động: {len([x for x in self.services_status if self.services_status[x]])}{Fore.RESET}"
    os.system("cls" if os.name == "nt" else "clear")
    print(table)
    while True:
      self.service = int(input("Nhập số: "))-1
      if self.service > len(self.services_status)-1 or self.service < 0:
        print("Số dịch vụ này không tồn tại!")
      else:
        ten_chedo = list(self.services.keys())
        self.service = ten_chedo[self.service]
        if self.services_status[self.service]:
          break
        else:
          print("Dịch vụ không hoạt động!")
  
  def find_video(self):
    if self.service is None:
      return False, "You didn't choose the service"
    while True:
      if self.service not in self.services_ids:
        self.get_status_services()
        time.sleep(1)
      request = self.session.post(f'{self.zefoy}/{self.services_ids[self.service]}', headers={'content-type':'multipart/form-data; boundary=----WebKitFormBoundary0nU8PjANC8BhQgjZ', 'user-agent':self.headers['user-agent'], 'origin':'https://zefoy.com'}, data=f'------WebKitFormBoundary0nU8PjANC8BhQgjZ\r\nContent-Disposition: form-data; name="{self.video_key}"\r\n\r\n{self.url}\r\n------WebKitFormBoundary0nU8PjANC8BhQgjZ--\r\n')
      try:
        self.video_info = base64.b64decode(unquote(request.text.encode()[::-1])).decode()
      except:
        time.sleep(3)
        continue
      if 'Session expired. Please re-login' in self.video_info:
        print('</> Phiên hết hạn. Đang đăng nhập lại...')
        self.giai_captcha()
        return
      elif 'service is currently not working' in self.video_info:
        return True,'</> Dịch vụ hiện không hoạt động, hãy thử lại sau. | Bạn có thể thay đổi nó trong cấu hình.'
      elif """onsubmit="showHideElements""" in self.video_info:
        self.video_info = [self.video_info.split('" name="')[1].split('"')[0],self.video_info.split('value="')[1].split('"')[0]]
        return True, request.text
      elif 'Checking Timer...' in self.video_info:
        try:
          t=int(re.findall(r'ltm=(\d*);', self.video_info)[0])+2 
          lamtilo = int(re.findall(r'ltm=(\d*);', self.video_info)[0])
        except:
          return (False,)
        if lamtilo==0:
          self.find_video()
        elif lamtilo >= 1000:
          print('</> Your IP was banned')
        _=time.time()
        while time.time()<_+lamtilo:
          t-=1
          print(f"</> Vui lòng chờ: {t} giây...", end="\r")
          time.sleep(1)
        continue
      elif 'Too many requests. Please slow' in self.video_info:
        time.sleep(3)
      else:
        print(self.video_info)
        
  def use_service(self):
    if self.find_video()[0] is False:
      return False
    self.token = "".join(random.choices(ascii_letters+digits, k=16))
    request = self.session.post(f'{self.zefoy}/{self.services_ids[self.service]}', headers={'content-type':f'multipart/form-data; boundary=----WebKitFormBoundary{self.token}', 'user-agent':self.headers['user-agent'], 'origin':'https://zefoy.com'}, data=f'------WebKitFormBoundary{self.token}\r\nContent-Disposition: form-data; name="{self.video_info[0]}"\r\n\r\n{self.video_info[1]}\r\n------WebKitFormBoundary{self.token}--\r\n')
    try:
      res = base64.b64decode(unquote(request.text.encode()[::-1])).decode()
    except:
      time.sleep(3)
      return ""
    if 'Session expired. Please re-login' in res:
      print('</> Phiên hết hạn. Đang đăng nhập lại...')
      self.giai_captcha()
      return ""
    elif 'Too many requests. Please slow' in res:
      time.sleep(3)
    elif 'service is currently not working' in res:
      return ('</> Dịch vụ hiện không hoạt động, hãy thử lại sau. | Bạn có thể thay đổi nó trong cấu hình.')
    else:
      print(res.split("sans-serif;text-align:center;color:green;'>")[1].split("</")[0])

Z = ApiZefoy()
Z.giai_captcha()
Z.get_table()
while True:
  try:
    if 'Service is currently not working, try again later' in str(Z.use_service()):
      print('\033[1;31m</>Dịch vụ hiện không hoạt động, hãy thử lại sau. | Bạn có thể thay đổi nó trong cấu hình.')
      time.sleep(5)
  except Exception as e:
    print(f'LỖI NGHIÊM TÚC | thử lại sau 10 giây.|| {e}');time.sleep(10)

import os, sys,time 
try:
  from faker import Faker
  from requests import session
  import requests, random, re
  from random import randint
  import concurrent.futures
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  from faker import Faker
  from requests import session
  import requests, random, re
  from random import randint
  import concurrent.futures


def clear():
	if os.name=='nt':os.system('cls')
	else:os.system('clear')
clear()
def fakeEmail():
  faker = Faker()
  print ('')
  print ('             \033[1;34m[ \033[1;37mTool Random Email \033[1;34m]')
  print ('')
  data_kytu = ['', '_', '.']
  so_luong = int(input(" \033[1;31m[\033[1;37m[•_•]\033[1;31m] \033[1;37m=> \033[1;32mNhập Số Lượng : \033[1;37m"))
  Domain = input(" \033[1;31m[\033[1;37m[•_•]\033[1;31m] \033[1;37m=> \033[1;32mNhập Domain(ex: yahoo) : \033[1;37m")
  file_email = input(" \033[1;31m[\033[1;37m[•_•]\033[1;31m] \033[1;37m=> \033[1;32mNhập File Lưu Mails(ex: email.txt) : \033[1;37m")
  n = 0
  for fake in range(so_luong):
    n += 1
    num = randint(10,200)
    first_name = faker.first_name().lower()
    last_name = faker.last_name().lower()
    get_kytu = random.choice(data_kytu)
    fake_email = first_name + last_name + str(num) + '@' + Domain + '.com'
    print (" \033[1;31m[\033[1;33m" + str(n) + "\033[1;31m] \033[1;37m=> \033[1;32m" + fake_email)
    open(file_email,"a").write(fake_email + "\n")
  process_menu()


def checkhotmail():
  print ('')
  print ('             \033[1;34m[ \033[1;37mTool Check Mail hotmail.com\033[1;34m]')
  print ('')
  try:
    print ("\033[1;31m[\033[1;37m[•_•]\033[1;31m] \033[1;37m=> \033[1;32mCÓ THỂ NHẬP ĐỊNH DẠNG MAIL|PASS")
    hotmail = open(input("\033[1;31m[\033[1;37m[•_•]\033[1;31m] \033[1;37m=> \033[1;32mNhập File Chứa Hotmail(ex: hotmail.txt) : \033[1;37m")).readlines()
    hotmail_die = input("\033[1;31m[\033[1;37m[•_•]\033[1;31m] \033[1;37m=> \033[1;32mNhập File Lưu Hotmail Die(hotmaildie.txt) : \033[1;37m")
    hotmail_live = input("\033[1;31m[\033[1;37m[•_•]\033[1;31m] \033[1;37m=> \033[1;32mNhập File Lưu Hotmail Live(hotmaillive.txt) : \033[1;37m")
    print("\033[1;31m────────────────────────────────────────────────────────────")
  except:
    print (" \033[1;31mKHÔNG TÌM THẤY FILE BẠN ĐÃ NHẬP !")
    quit()
  list_hotmail = []
  for line_hotmail in hotmail:
    HotMail = line_hotmail.strip("\n")
    HM = HotMail[0:HotMail.index("@")]
    list_hotmail.append(HM)
  
  def run_check_hotmail(hot_mail):
    s = session()
    response = s.get('https://signup.live.com/signup?username='+hot_mail+'@hotmail.com&lic=1')
    kq = re.search("isAvailable",response.text)
    if kq == None:
      print ("\033[1;31m[\033[1;37m[•_•]\033[1;31m] \033[1;37m=> \033[1;37m| \033[1;32mEmail Live \033[1;37m| \033[1;32m" + hot_mail + "@hotmail.com")
      open(hotmail_live,'a').write(hot_mail + "@hotmail.com" + "\n")
    else:
      print ("\033[1;31m[\033[1;37m[•_•]\033[1;31m] \033[1;37m=> \033[1;37m| \033[1;31mEmail Die \033[1;37m| \033[1;32m" + hot_mail + "@hotmail.com")
      open(hotmail_die,'a').write(hot_mail + "@hotmail.com" + "\n")

  with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(run_check_hotmail, list_hotmail)


def checkyahoo():
  print ("")
  print ("             \033[1;34m[ \033[1;32mTool Check Mail yahoo.com\033[1;34m]")
  print ("")
  try:
    print (" \033[1;31m[\033[1;37m[•_•] \033[1;31m] \033[1;37m=> \033[1;32mCÓ THỂ NHẬP ĐỊNH DẠNG MAIL|PASS")
    n_yahoo = 0
    yahoo = open(input("\033[1;31m[\033[1;37m[•_•] \033[1;31m] \033[1;37m=> \033[1;32mNhập File Chứa Yahoo(ex: yahoo.txt) : \033[1;37m")).readlines()
    yahoo_die = input("\033[1;31m[\033[1;37m[•_•] \033[1;31m] \033[1;37m=> \033[1;32mNhập File Lưu Yahoo Die(ex: yahoodie.txt) : \033[1;37m")
    yahoo_live = input("\033[1;31m[\033[1;37m[•_•] \033[1;31m] \033[1;37m=> \033[1;32mNhập File Lưu Yahoo Live(ex: yahoolive.txt) : \033[1;37m")
    print("\033[1;31m────────────────────────────────────────────────────────────")
  except:
    print (" \033[1;31mKHÔNG TÌM THẤY FILE BẠN ĐÃ NHẬP !")
    quit()
  list_yid = []
  for line_yahoo in yahoo:
    y = line_yahoo[0:line_yahoo.index('@')]
    list_yid.append(y)
  def run_check_yahoo(yid):
    cookies = {
      'OTH': 'v=1&d=eyJraWQiOiIwMTY0MGY5MDNhMjRlMWMxZjA5N2ViZGEyZDA5YjE5NmM5ZGUzZWQ5IiwiYWxnIjoiUlMyNTYifQ.eyJjdSI6eyJndWlkIjoiVFRJNEdXNUxOUkRZVllXWTVGVUVPRzYzQk0iLCJwZXJzaXN0ZW50Ijp0cnVlLCJzaWQiOiJqdmNTMUhCeVVDOUsifX0.X_NnPLwAx-Pp64hpfdG6GXyV7CayYF_NXQY7LQdgMoS7qGyj0wZ5odPbpGOWdCWchMC7bluy2HHt3w5L6tRV1dwaQdcbAlc2sUlMvm7zIRisRXUIxZaOyK8OsF8w8kEvf6n45XeGWQ-SYi6AhxoeRkdr50vXRMCGprQjrprcUt4',
      'F': 'd=c_5NaFI9vIaCRwWLpl9WioTw6E8yo5fiI5LqNvPK',
      'FS': 'v=1&d=zPp3EiXz4rrGqLxfr4O38MFY4XOSOj3jY1s79wLYc57Hp15JiDNNwvcmddDP6yWR4StUAeqPBkLEhhNMfq0Y2kMh5NBDYfUuRsboI7cnEq2fKRp4M0D5gO.xJTBzrn6p~A',
      'PH': 'l=vi-VN',
      'APID': 'UPd9d7f802-4365-11ec-980b-06a45724a3b4',
      'B': 'd01kp4pg0bdrb&b=4&d=neURBE1tYFn4hXkrqMNv&s=8i&i=U7i5kvbkgF5nUCmrGPQI',
      'GUCS': 'ARji73Kp',
      'A1': 'd=AQABBGu3BWACENKrPJCgerWnEppDDyaZBtAFEgEBBgHj2mGkYtTYb2UB_eMBAAcIa7cFYCaZBtAID1O4uZL25IBeZ1Apqxj0CAkBBwoBuw&S=AQAAAshltxt1fD4hRa8uk3FPZpk',
      'A3': 'd=AQABBGu3BWACENKrPJCgerWnEppDDyaZBtAFEgEBBgHj2mGkYtTYb2UB_eMBAAcIa7cFYCaZBtAID1O4uZL25IBeZ1Apqxj0CAkBBwoBuw&S=AQAAAshltxt1fD4hRa8uk3FPZpk',
      'A1S': 'd=AQABBGu3BWACENKrPJCgerWnEppDDyaZBtAFEgEBBgHj2mGkYtTYb2UB_eMBAAcIa7cFYCaZBtAID1O4uZL25IBeZ1Apqxj0CAkBBwoBuw&S=AQAAAshltxt1fD4hRa8uk3FPZpk&j=WORLD',
      'GUC': 'AQEBBgFh2uNipEIdngR2',
      'cmp': 't=1641651144&j=0',
      'APIDTS': '1641651233',
      'AS': 'v=1&s=b6DuthP3&d=A61daedc3|2z0NIVL.2SrrTLqPq7mRmcr2Pp3bwnyiVy78CcP8Tl6nkEoQV8CC_PpLqGpsSe7T9Er0EK.2JgWWtxpoBYPwusO7dAaSqvqqilmJfjBGhP4JW7jq2_P53GPCtGCvMIeuxYCDcySagRrJHHEMOq43Kory92Mtr_ITwFrFmUcHS0rIU0l_8sIwA5svxzGccw_LP86SunVG7E3X7GtU0f9QM.oTXpzj3Y.0SnCYjQu.UpxX2KdLg8NqwvImE7B0xG8xlQASeCyIiLWi.KDvzGE4Ry1LDkxGkUuh_ElrMBdaGkcbf0a9Esw0tzAQDcWZcFj_5VbaKb3VSwLHMg6mvYxh3Mokej_iAmwusksfN.kQqwc.s8I6_luixdBGgpne27TPMmvb29ftqTinm6EtRyNZryRte3NtTelQngHwBiCdIJxSWHv8MjdeHsey_sxfQpvna8SQL6lGqYfDgAONCBnv5oVK4KNbvQfgIp6PCmfaY0ochwIlgz.zXka_cecmhXWAFplb5tKrHdHCvDDE7T9W_YObq0u0rh96QC__fCqef2e0Bh4cuUHSQu77po8RXxodEFXj0Dge6NcnGC8StP0cDt1Tdyd8x1ZAUz7uGzZ8muGhajW1fZ2Bt86LdN4XttaN19u.q7uWWwJblWhlYjO3uvU.nRNQ85F7Bs20t0oPn7idgtbYNmWgikcOAV91L1PJFntHmGSVdQQ8GEKPGl2frvBgTrgdiFf_yoMSDFwDx0GixVyBspIbE6.4ryWyQVh1Ga2hkH8cwPiZfS.OapzEXKgl7j3ccbgRsFe7V4w9hhexU2oWVyOG~A|B61daef3c|MpxzwDz.2TqUt9hufPtA2u76Ekf4eGjUU9EJaL00QO2_CSCYKS4WOivoUjm2xw5Psr4hdpS0cyODOKMQc0HA2ntrdNmVpF_jDJvIefEIXIKUnDKYlinTSVps8aPE2YLPY9KcytF1a9uj57CTjGSOKeRKCxJSCYSJNcpoOOAqiQh0lZVHLCI2nu7Kz5IWaXbpcPeHH.UhrQh_nEH2gZg.jw9z6FvqTkMgt1_A_VGmAAoFYYqqs082nu5YsshO7PX2y_vKZ2WECMsTWFWEFlzcvP3joQblBO1E9h9WqxZXYa55sqeoh9ZfrKZNtUxRKa6LKSxz6uuZQBMKJfS5xyyoyawCyII8Sz9Ian8m6K_IhBYGzdJPyeoxUcIKlnvd2qi5QbW6j.mqB8lcCuB7M8YBbT6yORcjd0lt38tR_NchoW7H8enyCTgQJCRNYptVjjNai1_44QE82iACvnBIQrL6MaOTnWT2GZat_m.7cAX5Fzs55xfCo0oSuygMTO5UXeZYzQKifuq6YAKuhM7Mv648I3v2YOtfXaRPaExvTny0GcmHhxLYePsZXJM.vjShJ5jdSuyPLp2S4dImRvQUo.qv75yesAG0qVniU_xfIY41COe91NuNDPN6XgENPUYMZFw4bq3ZoJveWgfmSHnJo6_S6OC4_TYtsjjMUwDlFKCFI1XzkJaZpwQV3CVJCIUqcyUuyzBA8zPOSVL18SKjOrLoNmOkHFd8mX.1oAPx8XkF5aNBonvCYS89MPUJTFYQnxTl0BBVif2dr5K.5oz7VNGTpQZihdAIuTFSdyZenI35d0Q8b4hBM86FmR8cSU49VXnD9secAADk1tEvcfN_fUvMCLQhwY2Mzb1vJUeSx3juC.2g.EStGr6PNBUihHqfwi0-~A',
  }
    headers = {
      'Connection': 'keep-alive',
      'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
      'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'X-Requested-With': 'XMLHttpRequest',
      'sec-ch-ua-mobile': '?0',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
      'sec-ch-ua-platform': '"Windows"',
      'Accept': '*/*',
      'Origin': 'https://login.yahoo.com',
      'Sec-Fetch-Site': 'same-origin',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Dest': 'empty',
      'Referer': 'https://login.yahoo.com/account/create?.lang=vi-VN&src=homepage&specId=yidreg&activity=ybar-signin&pspid=965620046&.done=https%3A%2F%2Fvn.yahoo.com%2F%3Fp%3Dus%26guccounter%3D1&done=https%3A%2F%2Fvn.yahoo.com%2F%3Fp%3Dus%26guccounter%3D1&intl=vn&context=reg',
      'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  }
    data = {
     'browser-fp-data':'%7B%22language%22%3A%22vi-VN%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A2%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A-420%2C%22timezone%22%3A%22Asia%2FBangkok%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22openDatabase%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win36%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%20Direct3D9Ex%20vs_3_0%20ps_3_0%2C%20igdumdx36.dll-8.15.10.2555)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A46%2C%22hash%22%3A%22064d0690c46a020baabba41f6efb55e7%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221360%22%2C%22h%22%3A%22768%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22728%22%2C%22h%22%3A%221360%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1641651644921%2C%22render%22%3A1641651639853%7D%7D',
    'specId':'yidreg',
    'cacheStored':'',
    'crumb':'lIkCayBDeLe',
    'acrumb':'b6DuthP3',
    'done':'https%3A%2F%2Fvn.yahoo.com%2F%3Fp%3Dus%26guccounter%3D1',
    'googleIdToken':'',
    'authCode':'',
    'attrSetIndex':'0',
    'specData':'xFpFqogl1490c2062fZQaeVhyJ4qtfBUXfJokQC7gkbGXpyb6GW2EbppxSabFeZduQFIEnZ9fn15F0ii0bbB72a103C4zul%2BpYQZHrVD6otCEzQYGKbN7WePXE7R4pwX0ir7gIyV4nj8qEtEvSnejy3lUVXzB7qf7ruOPkL9j4T9NcZmdoXLQwWxaS9M347k7Jaf9XFMnyV5rKz6v9wBm%2BLkQfuwLp%2FzrDKM1VF%2FFZe4DB8fLxpXAHktCjj%2B9xsc7MyCjhCHhl05ecBcAER%2FVpOF%2BJG1Nr3D%2Bm0rXWNcDBTN7U20ewqZwyrqnvoogk4yag1X4nsfW0cCiSpGr2HedtuKqgr70Ic0bY8HCMDxrAtTxU9CcIMpnJsTxu7f50KTmFY57mEBGtp4DQ%2FhvXlk%2FwPBbSi%2FDMPIbx4QlPfSuPAY23s2l5hpkz35DQr8Pux%2F93%2FjoXTax0y8B7i0nslLO%2FaqBtwv8%2FfFXF2VvfGm%2F5HldUdluxEtdDC%2F9IXB9KidWi%2FNAfnS0s%2FNfx%2BMLZx6tjNE6oFKYisE7kraFUbmQn2gATrbuqQ5mTQ6Ziwc6vSxtzgbnTZ827sZh2H9%2F%2BxFhWqSYWq%2F5rehfJoY6B2Sja7ZwpFQ60nUcQdTjfhCt1QEdXCI1OxyKJB1r%2FRTBcoT%2F24Nf4rJ0NfWG5QlO3jYemh7Z0euyJoFNssQHCizXWnb7Hdc77B8XjyzTKa2dGGHogRPHNqbo9zTU6FWR6cmmo%2BeFHarPsl4WV8%2BAsHweRnLfHQ%2FJrcaoUz6VRh88eZlMtC6veLLkcFAHDn94yjGcuTakeVmYDtNyVJuuV8knjJ9PMnTKFmQSNbZ68Kx6mKOekCif5HvqPzXOmgLlohwCAkbVl9pgflD4eEhP10Bd7MS%2BJMbq0MwOiNE%2BKx3t%2Bb8a%2FHWSs9HE85NPj%2F%2BnG8Z27QRdiddeXclihd8CNDMQhuuDq7rFzUym1NDDxw9zWtQzMrcVBkaJN80iEnWXhZgUOZYJnstROBF2svyEUYoIGDn9qHgdSJBcoO%2B2KaWmZ6SIkvWTVJf0pPyq%2BAEfcbtmlJ51gHdG50K4yDkvOKB8i%2BXYuO0j640iSRYTBVgrqo52f%2BGPBJvhfAi0AF0jzamGXxeV7lglZ2CJFMf%2FHL%2BaoENuzHT9wx1PZEVGJKq0r%2BwDeObAGUrSoPRDSMjU0udyuwZ2jDa1ARbzXkTAYTTGoJAt7haJc8e9xuYGu8dVa%2BqjlEM7b72znirawAQfM7M%2FjGoa6QFy%2FVoL%2BdSSeAl6YuciDPk34VgIBGA10nBoPO6qPhWgeRDlvqqdEZgWgBuM%2BBDZr6Sr7zds2bkbhc9iQV7zaPdBrPSDABYKx6JDykzLGVGApeqRtgsJZS6ZHgeRaqJn7j5aqayznA%2Fjy8VuabJIeub8h%2BLh%2FF3fnOqH9OtKzmDvmUkAmjFc9RJds75cvkYUFlZ6WGer%2BSU5iKoDjY5acbJsaGff4PtwdQVoBumzEAdpq1C5YNQBv3ghRvVCe3ahlMwT3IVIxQ7adO%2F2DvxNQ3vnC6M0R7nLfdYgxjHhD5vdn9%2BMlJxxk5i7lNoMshept2mItAnWh8%2F4VrBxIZreE%2BWsdONeqP%2FS%2FJXl6XuNzYQclyd2g0pHp0Y%2FFT88K34ERfUARz3cy%2B%2FcTwN80t2DLRLUkYhgHpftNKgDrI6b8Du0URWD488swoc2btq52d4FPFiiCVtZFwBEvYbJdjg6drWqEv7HN8IPHNTaSl%2F1k364FPvGgpaZ4icOVdhbmeTISnfzhtZK7vTp38HGmU8K9dL1vgntdNIfnEuQ5a5IfopD8xm2sr81zavSIZP2prURA3h5WomhRfc%2BNw9nrYF05d6EVtFm0mX3Ok8Y5F58ktUXhA%2FNeZD3mqXjLUmnBD3fTu%2BvvFlDTIhXSIyhPivEjKLEYtLRoq7G3lbYmHL3PHBcDAh8fSka9U%2FOZexs0dyxcAS3tNk%2FgrrQCFfuhCJAx1Zp46GLLK0KQ1pICkttOpMeQQKnFe9tVONzrmK2ui4%2FjnyjaZIioOOM5XqaMcdEcuFCfzVMtAHxMujd3zcsswbDWnKLvl1rgPGPZpMueR9I%2FCKMBBINjm%2FwRFz3ZYYZ9N%2F209q4pBZ2vcFGxS00FYQyADyNMdbkwu%2FFpJXQ3EKEczsaT7lFIXoXAvSkoG67STgY7aGWe9AM1SU5YuYO9pr6VQ824rS3n5EuTyHcSt8bwKekPwVv2LFqTZVQMcjdaaC09BdxB1eZbHAvbkoS2CEh1TuOOAxTqPJRHSLjixPY1PXcLluDe0M94xU%2FttfjI%2F6vDpj6Chw9yQpq0wX2zKNfPVLi1pQ9YkyHS%2BI36FpPpaW588byniK5Bimw3U6bsCEV6fNJR2Kp85w%2BjE3lTcgZy6kaMwno1q%2FGghFeo1VTAAcexFii0ax%2F8%2BhuUP4QnEIkcZnEWmc8SU2XNgmNmzspndGYCN1EI4bJ6MLHVDIYdbteXaRm19%2Bqs%2BpewwaFXORsvi7zna5cItWnuIDXJTRanas3LcrgguFuVIy6dsub28hvvlJzUporstwHw9hLxqW0Dcqw11FIk73tj5Fm7J5mQNr1FJW8Cxafpyf8XUMC%2BIXz8RElrjspHGA9AMYe0qIjaAgadbC8cac8ZzlJpW2LxfrqoHairi1jcb5CZifK5J8JncAKtDtR4OpO5SM0EjSNTWLkCeq875hOjD%2BsLytntaVhCDgbpnDPgt1r2IcQJZETpq13zFM87Ls7aKZMISC%2BhZmSBhVLXXsbqJlLnHzOZmpVwKub3yWxfcSjTSVEQ8jq8BcEU13v3gV%2FEoAaSAVUj3P%2B8G4SMYR3K8biG9h72UX%2FyYiQuPVX708%2Fk8UkJacTLw24DRT5ScE%2FAvPJO04Xh3dPRdHPR7YmE2a%2BU0h2xbcvITn5nL98Y8%2FppU4ChBfvs6lOltkneZ9Z29xo%2F7sOBgKi3z3P1jMmXtfqPBe%2BYMDr7GcHUOWTXg0vZi5S0IULWCp75xZ8P%2Bn%2BNhBQchT%2FFjZOGeLMVyD8rwrKHRieN3KySVP1M1xyrDCEpCFmcTdq%2BMgFUKtJ2pbjVwSdJ9wY6RCdrKsV5%2BoCmpaOjD%2B3SX%2B64Dx1gZ3%2FTEZhIbutNiNe75Sj%2BZzK6rr44q3OfluJ4ztJkQbNq%2BTlA7NJIIs%2B3T%2FRemBtCLXIfPpZQHaub6LdzRKGedxNwbuXIP8mJ%2F4jKtUDjprEPG%2FREee2Gg%2F%2F0ukqg5LFqqUbM495%2BKMT1rtcST%2FRZDQrlLsysZ2R67Oc4Tj9cxgts6v4MLUPNg8nT91NIh%2FMCiPIkabvH%2FBlvRw39mAPthqs47oEHOHZTcpMXqAYlIImAbvLhO7xHg7GaC3PgzNSGHHWlYjX4wzOjbGsc3GRsnDnpgrrnJ%2FD3d7RIj%2By0FbKmgemSQMatLVxjg3dg11OoF9Hsa2KII0fpTKjJYRyS%2Bz1HbH8aba566Se%2B7hf1wm3kaivc37sHVnIylo7oYl7TdCbOIRbxiS92r2jcdbpt1sn%2BSEj%2FNebZOI7oNYfz3s9l0%2BEf4JK0W9E1C58cRxYlywceLMrkj%2FwVYazlzCjFggEzEyHwgAQ7cXgohJpf0OrB3W3XpndGCOBkIIl75lG9qFTigJxzQAeHe5lLKkyKpxTJhrm4uwSbqMlPbFJvfQnpNPNefyBPxo15QGhxMbYmw4Asu9Kcrx%2FUIgn57yO7OjEJP9n4t6dO6mERKckL8LFJz%2BYZn2J910ZkB%2BGfE3cjqFBW%2BMdfHf42twildemggmvqSa7IWiBkmcBKaNo87Ngj9Itfwm1hcowO0hI80mm4ap5YWlCJNmOM4BDACvtAJIAlVdI5uC8yCjnp2LBpDt%2FmRfYCeXF9GYfWhCsvM0TXmn1EmO4fCgT3jiV7VfezXtD9GCUWpNJRJrsUK%2Ftb%2BHc14ikKIlOxdh8yJ8ij%2B%2Fmga39pEREejYL8v4F1NC%2FDui2txuSlM5O5%2FEDTRZU8lZVPtDZ1z5vweNQ88oPAeX8lzBzzcIrdZy9CXcwGCZt1u%2B7MZJX2%2BNaQVIcgzqD2kL658%2Ft4i8C3Di3r5qRxW8CVtyRfZV%2FQrsd587nNbVSM4kJ6LOn3zk7rUkWebNRRdEa0MfCb7NFNISlpJigltrXIsmaFX5SEmcf54u%2FiSPIsReE7nXL15JVANzAYKMgsTUjjolx%2B8b8S8R2qe9lxqCW3DpGPzEPiwpyjdcqpKyWVJUiI6HruqOw1JtXGHQrp503J6L3qxbch5rptUwqOEvVCYQkKoIZ4wl9hu9FRXSIYT84nIBUkDsOu9Z%2Fug1%2FXq6r2L7fdFsXNgya0TLnZbj9CAtPIF%2BypWe%2B6yQeTT7lj4p35RvZzxgdSlA7HhQnR9ixczqmHHNfPIUfrYdVhw8KOoD9bO1AuDrqJCb1b6hbiWplWaXaZdgjcc5HIcuzoKXaC6NMsP11H91lzHPqCSo2%2FiLFTVyZ9BweJQal2eYP4nlXllYAU9I5s2K7Ya15DKPCyXc3HePqUcsKF0Ee3PObAfuoblVktoRRJZzzubcKtsbKINyxuRor%2F5LIm2FlgAw4K0JBnAX7hH4BUKeAvUfjqigxAzvAXDjbd6gJmqfjcHsJKK9Tw4AWhjSY%2BMCb7e90fV7%2FxJ%2BI7jtE7VLn0okoNelpSFIboA8%2BbuvOmkJ4VCK%2BIvTUZsUCTEN13CRypL%2Fc3Mu8cRnCu4ijFRqONYR4gzwab4B7v%2BfBQnuA68IPCJMEX6R7r8M5iND3JYMcGKDdQbrkqiufduDeI46SSmr2SwfXdFZhP8wolHvobxsjWsF5sIB%2FxImgDbssP0XsrHSGNWwc0scQjZmWrvpCZX7Ue2cX0H9VPXtataZXonlTmKl0TgB3VAX52gMpoOlb9dGfmBE%2FA4gmCM947qmQT%2BPE9oveEJRongoYzJNEd8XxzEYpa3RGlaZTphJl1h590kyIQPt4W6%2FpalCfwxehao%2FhOhyc2b4z7%2BoWYBNrYcDJIBLpOr9JEldJVMHGhszocf7OqS%2BR6beP4%2BbJrbfaMMozPuQhTzKX35eKWFr3E3Hxc%2Ft4PaIz9lLKGgyRhU0%2FmgHgDKKoplV%2BSYYJ8%2Fhy%2FOX%2B5hASYz1LC6IHCNLdHTdGmARuS2aGuPGo34MOiICwLse9o90ORR1hg7ntKZbRBkGKd1Q0Uj33rMe8%2F0LSohvJhUS7xP0sAkhrnUe0EhHhd8fK2azb3lKrjBRiIKr33whf513VjfKpL3ut7ZSPSqXSiyd0QTDLsf4gcsrgXc0IqkcH3dExfyjKfXXlWeafvqSXKoCno67U4j4YaiT1I7MXekbqDCChk6wd%2B41Fvn5VILwr9z2WRvBbg%2FnJkvGluz%2Fr825qJSY5FonfbZtoNGtNVT4qEqpeKirxCuUeVog6Bw9rXYVLyxO4D0E29sZuUmtt39h3mOKxmRJixcPSzHtKvwZ6OSuqwF6xEST7EUz%2Bbx9OfCcaEXvIjuGwRZCT8HV7KuT5okNoT2dZOLgpUPK%2FqkSISp4tYqi6k2Ca8SG56Bi7frZtPw6MEMoUYP5HO4QNvGv6CPnyDOAczVreUDaX6PXCjaxKiJZ5q7qtSti671e1yfUETIQQleaY5e%2FfBm3hVIqaQhwuHwKkizFS6Joy4OzXzzScYc5RnSGUG%2BwwowuMjhF2K%2BrxwYLYuoNQuKq8v5TIvj158pFLMQ5ZFsVlyAjRhPesx4p2b6AzaT6%2FBm%2F3yE4%2BD8Si%2FGa6mKA%2Fz385ycsVRJcSmjnHMXrka7YGe5VYR64yUV1tk9DSALzRAD2FawqCc2xbSO4yEh8Ojn0dMsa%2F1fobWl6r1VdkRf%2FY8xBhfa7yCPgd9xaf6OGrOxqG5XvabH7EI5KSKfT10Hs03XANfxvMtd0YimCH9oTf8GrN%2FZVIWeQa378X6qyDhcE1ozFUxxVxxAwtY%2FN8FOvvX2GYfexbLbHoIeChD36DiEjBmwBbFQCPOx9Txs1LgFy9M9TuzIca6F4sPZrdkk1pSr14%2FMiuf6PYG4aeJue%2B2RRGFUwGWMUBth%2BwMdBjj7kfEN3dtjMCqpF6SjImjwLVwrQvSRE2na0gk6xoJZ2p%2Bb83y5iNQJhETuQZyp%2BaoCb5Zc5bcrTKjMGf2htNA2Q26Z1EyJOwoZ0S%2BxstVYF%2BWDq6WQte3AP%2FSlVrMrZX%2FAtUYhP4%2BRYQBFUEl7Q29m%2FvyQ3L3C%2BAf5PdOJ%2F6Tteqw790v5hEfAW%2FeW0IoX0oUupJt7r2mJh8%2BmqbDc5DcT0ewq3b24%2BPCymQbYnrHGXV8RCj9E28O7cN7l5ImQN3yHRksBVn5e3HX0XjRwKw1ZIg7L%2FPUlwbVhXPfotpLFJMO4aLQZEXfIiJ0cHpU9zZyZlxYe34Srk%2Bl2nGEXF%2BqRogXG0ge2ypqYvrEXyThkkS6JiSBjrB%2Bb5FNFztrfH%2BAy3HmFUeMg3ICiPu%2FjwDqrZhNOdUW%2BKuHT75EyYvCRfxXhN%2F22huvNZqX2MzFGwEdb5a31TLzbcFWTHkVbwN0SEdoAWJIynbHsI9StF1fWHxeo0NCsvfimK1wTqX77ESiVuBYUg1O1bcgjtVl7HbV5oTYwCJsb5haevBpMrerOHZwnPJquAZePpAoCzWUjx5f%2Bmi6MamSbyC8xn7zX1p7LZiIYAX3vHzbtoxGoHC8DmldiFs6srfWVrI4qPOd5g6LZpwJsvrCiWYm%2FKrqfEB11G2muDyvsUasq3dDdP1vKrjev5Dzl%2BIDTqlA1i28%2Bm7948qH%2FirFMImssD5Y1uur%2BSTYVT22ZFc%2BBGz7PooBWgLOLfWZeVfAfmspEqVtZ47EohUgiD%2BJXu0Yp6Y2ILje6dj6nNGgmp%2B9ec99Nffxx0zgthT5WJZAfsQB%2BRixuL%2B5pzMlJ4XT0EdnSazBEBmj7ylvOQBUDP%2BD6AA8VI4gwwRVVAFIP8m%2FBgTdEACqDea9Egx%2BtQ9L%2FbG8pzu6IToRR0u6w6ooL6owO4jc4NTykjaH%2BiMANIbB5fZtZHqxfzWFhlviuY5vqZ8M8nXVzRG3HLPbmOb4ojTUZLiKhO9fo4NrUaEDyHFg3mNKyBueXTYIUmr2do%2FLXNAOsDShnVZBQaWSj5RxblCNunoIq372ZJTEMA8aKu%2B7ZpAD4Sw63EYUe2Dm3xWoAEe%2B%2BdZimszFl%2B7xmObtqa7WVCNtm%2FfbHnpFGWuS%2FY4bYYqd8H3yWgRNNYzbskPjUZPy6e5%2FUd%2FZlRSvbFOaeTu7uTBmjTYBfHCdffs26apnPM2MQ%2BKjaQ%2B2luYl%2Bb8bFvt%2BL6InwD4SZqEz26xGukVOyYuJ%2BbHAXCQkvIhDpw%2FB1A1f%2Bv%2BrO1V%2BK%2FSmdIiNZhO5o97rP8oZgbGVPIR6TjnyGkPn8F%2B4XhxZBOuIKJ%2Fgth5h2gOjEFXa60yN5ph752fyemmhWWagi1kbjof9TDbLgdN%2BjbFLU47Y0AY48ShuShJMU1K7BqLiDuYuTmE2HEDOFAAAqPJT1%2BdDkU5bkM9hivXS%2F4LqAdQx0Za6IAFLSOaUALz3TPbtZpBMZZU%2FdqRWkeKgPJQiaI4bg3ZpdRt8SMjCpqjCK8hWuNIj0Kh2VFqghyFW6qUk5tLia1hGjvS3mnDgAEPdjNBEoqFVwTdaD93IiHljs4yKZY921AZBP7m6QtD1Ii3gl%2BsGKP5uXuC%2Fj2brtnuifBAglKpoXmFCuhSzzgo79vg7B6w4diWHek3lzkaXFwNwnlu5ewefhgVn1xiYIHJ%2B9xW7J8umKW5ayw0klmrRM%2BPtx8cadCUNm8rVOlTKaMuw9Mt2HJwGe16%2Fb0siXZuZ8waSEqxtUowkgug40Js4F1hMuDqjitjWWx4cXo%2FkkTN2f0JQl6X5bNwksyT1Px6hQlKViVmYrjie%2FHpaHVRkYl6xbu59uxTNE9%2BMG%2Bwu4f6NOTbLDYICkoW18qDkAbUYbr4Brw6NGUo9KveyOt9IRNUOVMalmUY2AkOp6%2FcGMDkdqRZny8Hkc4AWm7akGsgP2tbALwHDw%2FSKc%2Bz28%2BkNKn1FTd2PIp37ZMfpmkVUWEpVEenMQIhI3Rv5oayNdB2uy7XvtICWQXNXyX8zn7M7ySomZkJtRXDzQxQCIB%2BHtPr0CDQZ%2BhoNa3zewAc%2BLtQcDuoGr0IxkX8GFE7O6IbSIe3mwh6OWI%2BpKizvodHJvvaUJJIs5lRxqe5h1qAj%2BMJXr8crbBk7o%2BWe%2BNOhrblchEhMhX03P3jRTbez%2BZvPfxJ%2B1hG2vz9x1Jr2vc0zK9w%2FRNYvNHM1Jr0ckcSArrSqKRZ5%2BwC2RSTuvA29HiJFcyXWoLqoxs%2FtTMZ4FVD%2BQSJZL4QLPdSVghHpfTh6LXcSmbUKrNGhw6K6EgneA%2FnBIL95XP8%2B058ACbwqm4%2BbA1wGM7vr8X7Y9nnXDD08sEG7FqHIB%2F7pCUDR%2BDzSbnY2EQHvZEHujItTCTThiQ7DaIWGfyJjwnQYJepsXjAydU7fSEeJtGsQgUPPM2ahMxrwLhGq%2FlfwM8azdz5ylsKxo31QkxUXUqNG%2BsGo13dFzaahahigEwCaHXKigU5MWxFAEeYiWsSUcuIeBx2KJSpQWdrg2Ob43k6E%2FnNdAaZd3d0JyvjAu3DzXLR4ePnijDcHHcXJKsM70%2BPanyUTLLBJzBIsTSs5sA7rJqzJoU2vIObtRyKodi3%2F%2F%2FpLgv3KW81Xpm63XhHqcLNVLjLYF7zeUfJXaOUY4TuQok1s1uOpj%2BhhHyaJRuIR10UzTp7vSVBklbXa%2FATO6jWwpsDXESRfQmzWF9L1l2h%2BrxsgaOwcPzzRkmDWHB0oKn6xphXwXvm2%2FTS%2FEuWopEW1sly67H5lGt2vLdaC5drnIIHF77nOLN41Zcgd9vVAGccrr3ywpS3m4P%2B7BQ4ORdTeErIoIhb7R%2FpklrxlDTXGbp5dYsDt0%2ByQYKPVDe%2BP5t31DGEX35Nit7HADYyXiftlRPZ9VfT1fSBKVxMTitAcLfE03K4f8Q%2Bx0EviEpZ75VRuMb4jlyv%2FWP15J4FV62FKMKUC2%2Ftlz7g8Gv6NCTAgYCNMmepNI3uKeGikdySiC0GFqt0epqMZ%2F%2FjISy8ww1eumJrsx4t8GC6uKlHCK3Htb%2B9noD9hh0N8wgOm15Q%2FbRHW%2FXF0mgd1ikGQxUxU5Fvnd%2FKSownRMlbZsv63IKN5HputR4aX7ZKT48zdKl2D1QTW9al3%2FJhyGy5DCKdFSMqrgNgFbY5TCRTmg3yK0hkOakGYHI4SzxAmG6o2o2aqXCDdwLyPF%2Fou3qpzx%2FKQQ2aClDmChcbPMWyKhwI0AKzlz%2Ffvm08izBelJB98W%2BRtDY5gLRAgjQkOQ6kSUN9ydogX456pMUwaexyrMkwAxZLHDsg5ruB6uyH%2Fjs0c4hV%2Fzoj6coSCVyt2Os8VZ0oxDXM0xNjolUHEkGe5Yetlz%2BaFKv%2FNCgL4h50mElcliKqftTLZtXHsrTp2LtN6L0CQSE5JtFCSOu2ohjmzK2ecHPNTmwcZ7uyjbqWlxTmKHw4KcWGvWVNDpb%2Bd0kYQTvQwhEqThZVkCySBkoQriOpUfXTm7EjGB%2BZnX%2B9j1MKWmdYhtGUp54VXQ7oejIo1HKfifI%2FEaA5TQTipXGHH0KfF4GQJkB3suY5CVgJVAiZDkd%2Ftt8N3J0SnPgRhS950HdWIyRW5RiOlIgVf54hiYA2K7mrNieyGvH%2FXxjT5SdzCV2AYS%2BlcZnWFXVwz%2B0FGsm24%2FQVrN7RL0psXFc5LnJwoua%2BmAfchs1iULhg2Ol9uxzhFRG%2F62oAuwMxyU7PpNDtzeoGnDJH5%2B%2Fn3lzNyML2m0xWsrVNxYrhiZvKU3mMSFdo361Vs4zZL3%2FN%2FM8D8CebZCNciFZNP%2BZjHP2SFk3hYH7d9cQiQ%2B0uQd%2Fr%2B%2BTwx3jh%2BZPrJAn3lT9x9l4l0FVDVF%2BCLmDIK%2BhvtNzrgRgemrY%2BcRA4IHQEvpbJyjQM%2B%2BoiW3h%2BUWAF9oI5I%2BEWWWhIelzNdujTFN0wp1m8sLMKn59T3hgx2AQd%2BAtX%2BGbGuv%2FA52s6FKFgHKBRg2cuHYPrmGwnOxx5RLWJ2Qy47VkxNCXijH8cWs7UsQUBudm3qulMC1oIdX7eNyzE%2BlG9mLAokaufVm8eynx1DAOuohXQSlolEjL4gFD2kZUbW6lWuJRxIN4bn3C7kKbUDY5sbGlG4EaGEP7gMco5BIs8MTcSzLRMVA0VFotJm%2FXsxCgvob53RGqIQkw9P11S7bIDVttLdafwn4a%2FDEEncJecDfNiq60ymKUsuf1o1BSfgo3PjuWe3Wfof6XllybdtE1mAYvpeo865DTqv02BUvaNvQPiMIDE2V6luCAlcifJIdP%2FYbAA7qjlMHSR2R2HL%2BahCLWnDDBlAIiywrVI7pZddpUaxm4Pa1jwatb8k01mZgdTpyyzNukJqHe7e1XcreUm5I6YGZ%2B9%2BPEY9N31owHdKVGao89P159%2BomOMi3Gv5B4pSdL4gyLJ90EYGWZFAUI1WDTfCYgnKIuYTxvBNYvdosXpIFCVC5JDRRf3qlGc%2Bf%2Bq8ns%2Fv8%2BEnvIfPQTRcO%2BqMmMRchUlJe3zUE9XXBFcN6P51HSpSG5qR0yt8W6YbXWxzzSxcViZlQtJdFtknTeDV7WbrZJxXvbsP7JuzwE0rPDwjnj2IPUSekt2mJd0A4xa9k85gm1OO6B41Yo3BK6VOVD3fUns2u6LvI5C224zsJDPq%2BxxnGkd2n4w8wkT8xAdVblk18%2FZngiV9U9uV1jQMQ8nzmWMkCldKamctZw911D1cWcrbkfyuPcjUd35KykQJb2KDfMkBb%2BQr5olaMN1eatgVAP12opH8aEGh%2BfmykbOKixIeMV2Gr5SB8sonuFYuJWCGdeV8nNoH36SCP7unTpdL8dp2ywmn2q%2BCr6pOP8J7F3qLSRrWJ3VPzomxsLwYYBB5oJuOQdlzDjxD0q%2BntjPIxwdGNwRu3uE3YbHz93UBw%2FScJFvaxU7A7gCQqScNC1MNLoyM%2Fio4yPE3SIIQr7mW51A2eD3sgXWCoBvL6LmrAaPnO%2FN8L0C5HkX9aEUo5deiL6949wP9dnOUCpVDdMv5Gi8ruIfgVM2ms8Csa3VDhkMPgTGGoxPw7PN5c80tAA8YWP4NoVBbW4qmr6E71jFJVSVASqGBgEtSLRLzwHcum4fBvtj0WZYqfoEuCk2JAkcO%2BulRONSjoYBCWcSuujEVHPyjRjDNoTR7vfR2Xov130Bq3egHndGqxLc4zx%2BaoisRzYgAtb20Z7VmmmIPrcAQGnk%2F3UpAXJs%2BEkxKUcA3%2FRlGLkQccVJDbFoOKA9dDQ%2BSswSJ5I%2FLvlRRIKQgpEHFEzfxZHDbGWbtJLsowiZ0ijGT%2Bmmcrt%2BsmhM0asvWyNOtlKlHs1gAGlGZubv%2BzOXhN0s17n6txvm5pwA5HjEvGA6xYllJluGiyEAN4GzTjDll0OJMDlblTByzP7lZJ5bwIZN%2FQFnMj9igIF2Sv1EE5ol0I2DbPHZGjMlrTDWg1Qd4QFZ98wnrWwmSDpqu7DH0e6yrGjCStToiNaC9xyc2GFOoM%2Fpq2vAzJ7kqsHLEhLyQf%2F5LtiRjXSRNYHr9Fd%2FQgHBf6QyQdTQeHzk0BrZirOgLPFdGFUuU%2FEDbCkcRIaOcN4IZUyhUdl6c9BQLl9gOTjFlWsSqjF3gyj1i%2B95xHt2kUcT1%2Fzowt1rEOLy7vfFH22xafF8%2F42styY9TTcVIiOTy0be6uZMGgnQLmkc28TT3B0PLii0ISpvx0NFxvoGeP0fmW8i9FtYHNHlHtD5Ywx5PE5JghrDeVSJm7E68rTnuLOHnKVRs8Cdi1ANrg7EYMZoWCVRAH5Pw6RQW79%2F1DtduxXnpkHgFWFRFs25SfMSRsproM%2BimJD7G9IYCMefh4IYFlDhMl7NOUW51OBJgMipr2%2Bvk9FG%2Flijvtu5zn7FVPs8gcXuIOwB3gDeU9ld61RrkYCkRAaZGPNfjmwMA2lxZKu3PQtajlGogKmjz0xMX6UGRhL7f724DKU4b3Br0L673ee2QiVX6%2FBfgnqse%2FDGe3wu5x8%2BLvZFogJJCKEMYHuMoa7TcXsUVBBrKMeTl4xj%2BgC4TBDnHjbYd5M9ZziSqX5%2BTWtvX7LSc4BUt7ojmpzxUCao2S27iGHGFxYyQQNBmz2ztG5I1DsLHLkQmQ3IE7hWMBYH6Dm%2BtXylBE%2B%2FP98t6H4RuttEnkQYoC8hu2dGRjuSXXmJgBh%2FXBUwBBbE8B1kcaFaP3Euv7ORit3pA8dlbLXWpLPOXUTLccPoJu0b8KOtTHUwtdRTge13QNdw6mf%2BV%2BvcNa9DPkaRrrbxAhMBU8me6TC%2Bl85rZz%2F55MuS%2BG2UvlR9mjRlR8nf7tuqrJFyUhy1WJwbcCYASiDbm0J0E1v4Oi4N2umo%2F99D4Gz9Y68VSqELa0Jz4onXER0VDFh2Ko1xOn%2FRJh9Ev%2B0B05DZIFsd6tKdVv3zbzI58%2F95N2VLg%2F7WqEYihUhhOX9%2BzMG7LjeIwO8rJ0naaEDMyPj5vIemImcv9FmbFigPjpQNJpFgYAdrmyp6sCUGOZw4CKxQlkjKt6dj9xaQn0VwcM%2Bs6RQw3BGbg0hfX775GUPhxYCeYJXenPCIHymGdCUOj9VuROh7jrEeYM2mP4dnL1%2BjO8UPt4txLV1ho2bkFoNoDA6qGpKCpPCK2ft6TmhT8DQ3x8mbyaBOkvT3uDpQwtzZ3yCMDQ7gK8pcv6zMyDii87oO4G0DKd9eb8lb3qKkaz80gm6midIrpnKIhe4DURGPdoO54Gy9PCIKEaqEhSVQ4l8DKNFtaFTuaqFlKI99irIbw2nDS2fEITdjHJc87gi1KlgbUWPa8Swb9zAo4HA82zHwoqxLw7DTXfp%2FROlco4t59%2FLrv7hwDZTGMbiidSrp38EDylvWsktR4DMnaJrY%2BLY12QqnvyI4YGQ2I6qpv%2FKHmsHbSbTU%2Bb93vSJVAXuXbPZepyRICOMj5ovQ7J%2FEVjKistpaorbK44U%2BhJLLsJq21GsLAs3yrC8asVjhPLvjO1uT6FsK1nocorKdJwMGnKEM2s7%2FaXGYwA%2B5NFtyfI8n4zduBekjxhz4quHtegW6hNYRrktW7e9SzdEcKSAvUmA2X2dY4Xj6z2BE9WJASD4bN%2F0x9H%2BhOvr15aSX1mn4vp6ud3kya3P1%2Fe6ykwz3yP%2BLMZzguFWMJv8dR1TF%2BMGSc%2BNF6hrxZaUzm7wPj%2Bh%2FMxfick6rDlJhV58vC0CcJa5iqeyMdq8DzgaGyREtaPUwA6OLtT333Gvp8XwYLSdxgWQ7qTyBmU1p7hkzaSjvOly3TUuimYfU0p3g11UjgxlxnNKnYAC6dlmHlBCUZfc0HqdGe%2FNqme12Xn05vhvhLlQ%2FEquJ1hZ3dYxc3OtV19ob3wsMm2jhX7aIJrgp8iIwjPkf3asRiBYZW6%2BhUJe8hOI7hJOibrR5poDbSUW20PkV8fbFbDMfAlrnDWkTZIBAuH1MiGbqdM0%2F2hNW8y93%2BMBaSWvw5A0i2j%2Fk9W4KEYCZSn0ME5MdK5iicK73pFLPT1LxDMSTuDY4dV%2FpWG6k696b%2Ft3G1BGsc5rIXSvjz3IB6gQi1JtqGdou0zD8fsVt8ZklYfDe4k0Yc%2ByXJP%2BUcXgjZVsoGvv5H6HmpqhegdaRvVt23aUQPU04b0E%2FkkZ4jK0oY25dwzARJijbCObd41w7r1DcJ0HBLXsDTukx5HlVZXf3Pft5yi3a17XSAfs2ptmo9OPM1Ttjj68Zlb8Lzso2%2BRIlBWVJqPM2v5vUxvabI6SRd11HLyV1C3Rr18wNxDU5xv89DydddCh8dNec38D%2Btq8hnDdW9xlTgw4oWA0XxhmDW6KBp4EgcPV8QIJbhyF1fc7K%2FQdpZCejRwBzlaFOSuYDaa5EeB5uxr0bVWTQfQ4qemyd2J5Uz36in41TzBmWR1zsOHMkIBgq8yT4IHkJhQu3CEHZkMAs84r%2BkKL9hX%2FW0PlalmVc3dR5QOu0k2%2BcJlPi%2F8ndgzrcq3%2Fheug5bMCb67KBN2l5yfPa0PFRPVLOdnum41AZG1HvI1NEbZKIu9%2FBdovhrMog%2BGLWGSoKovTdDMTmerkKIa9F%2BsmFd5WPl5VIymHxYrxRtmslA8xNvn2kYBw%2FCFLhc90MVl2T8ofr6yg%2BAarfiWjNNqWnhtlmOVrjuJBx43oSBD8m%2FxKVDO3TYJ4iNupGryQaNcdqRmi3qW4CGqevf3nnS%2BN6MqScXhesqWml3MGb34qviLpoTodaNZgA8wdO8oP4w0%2BzFs%2BJJyq2Wd3AsFJ0ADc6wAkCnIbN5IZsxmb94XXx4oeQbKpU6beA6Bpljly4A%2FlvtIWZiUrUyacb9CCCflVpCnkr4yahm3RpHz79fzJftgtDV5e%2BXSm9mffZcKy8KBhfsy2ebq3zKslFV9T9vsT7qV5QnPfGd5kA3uAfQJfffeVIMui%2F%2FQ%2B33JRtxKibP2nNh36MiYuKQLG%2FBE3TMF%2BpGNLfRGyMA77QAI1UtLhntEqb%2F7wLxU3NKbhPA2IdZMT1KDUl%2BAn1F%2FOWBxDsusz4%2BIFwFVq2kQpd%2FjlzI8XSntk015oqjKE%2F4hNewC2K3KIDIFrcBORNyI%2BM5jTBC%2FYjkdtT1ttTInKOXS7V7WZDd5DgOifvbvbpt4FYqWhnof%2BBUhqejJVe5syVlDcWHWrxewp1rlmNdw%2FaGB%2BguzVjU1JI9Nl%2B53pQzF%2F%2BAM%2BZJ4yoXalFDNc61cS5vhgZU2cH96Vrqfe7rZhHScFaYqoA9urc0rtfirscwSL8F02oaU2eSmeyzLA05WbVAudlRso3GoJHRethqsOZAuMqMR4N%2Bkm7WV3y8vKY3kk%2FyBKJGVYlIi2uBdMBqVwyE9NBlqbrf88H0%2BBS9X92FMFyH6g%2BPZgGbzHP6GCvxp9E%2BCt73VMJR7UnGQ1UZtcZN9lXWTvl8q5VRDpHQK5ZvuNs62GNzjBJ9xwxqto%2B7dowcZSQJCg2NlaPON0ypi7uQZAeX317D7skJAtqkkw%2FxDZ%2F6qH2zHvn1wMBJd%2BuvALggOuh3nAYBOsk%2FFDlZkFwB4e5xRbVPlSW99z8LRxEAzmdIsIv4FAVHOlOaWuuiTSVYa1DgnpPP7hGVjHuDgDPcA7UiBCV0d%2F4OPKPFZu2xhV0TAgGNlyurGlIq%2FYyq%2FzKmDvXGCcxe%2BALQXKCw1sW8fNg0Y3m0ZggBTFQqP%2B%2FIgV0yWEj5TB5KRItodHL0XE60AnFLtsJVGopYmPW%2BCXpOFvtfx20XPey2Q3AE1ZWRsGO212UVOW%2BG4pRebph%2BUZXNMgZvR2esRg3Dg3%2FmurXCUycpW%2FTnAuWgXsSiXuWxTCIyr%2Bt%2FjBUN9cIHKhEM0CLLI0RW2YVgK4JgZySi48sexnmvxeGnV4MFd5qZ2pxLW5UTk%3D%7CSYMrVR6bUQZUCRE3soYIOA%3D%3D%7CZOX9V0IbW7BBDd8wPl8OQw%3D%3D',
    'tos0':'oath_freereg%7Cvn%7Cvi-VN',
    'firstName':'asddds',
    'lastName':'aaafcs',
    'yid':(yid),
    'password':'xxxx',
    'shortCountryCode':'VN',
    'phone':'0',
    'mm':'24',
    'dd':'05',
    'yyyy':'2022',
    'freeformGender':'',
    'signup':'',
  }
    check_yahoo = requests.post('https://login.yahoo.com/account/module/create?validateField=yid', headers=headers, cookies=cookies, data=data)
    KQ = re.search('error',str(check_yahoo.json()['errors']))
    if KQ == None:
      print ("\033[1;31m[\033[1;37m[•_•]\033[1;31m] \033[1;37m=> \033[1;37m| \033[1;31mEmail Die \033[1;37m| \033[1;32m" + yid + "@yahoo.com")
      open(yahoo_die,"a").write(yid + "@yahoo.com" + "\n")
    else:
      print ("\033[1;31m[\033[1;37m[•_•]\033[1;31m] \033[1;37m=> \033[1;37m| \033[1;32mEmail Live \033[1;37m| \033[1;32m" + yid + "@yahoo.com")
      open(yahoo_live,"a").write(yid + "@yahoo.com" + "\n")
  with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(run_check_yahoo,list_yid)

def logo():
  logo = """
                    
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
  for pr in logo:sys.stdout.write(pr);sys.stdout.flush();time.sleep(0.001)


def process_menu():
  menu = """
┌───────────────────┐
║     Mail.         ║
└───────────────────┘
\033[1;31m[\033[1;33m1\033[1;31m] \033[1m\033[38;5;51m Tool Đào Mail 
\033[1;31m[\033[1;33m2\033[1;31m] \033[1m\033[38;5;51m Tool Check Live/die Hotmail.com
\033[1;31m[\033[1;33m3\033[1;31m] \033[1m\033[38;5;51m Tool Check Live/die Yahoo.com 
\033[1;31m[\033[1;33m4\033[1;31m] \033[1m\033[38;5;51m Out Tool Gộp 😭 

"""
  for letter in menu:
  	sys.stdout.write(letter)
  	sys.stdout.flush()
  	time.sleep(0.001)
  choice_user = input("\033[1;31m[\033[1;37m•_•\033[1;31m] \033[1;37m => \033[1;32mNhập Lựa Chọn : \033[1;37m")
  if choice_user == '1':
    clear()
    fakeEmail()
  if choice_user == '2':
    clear()
    checkhotmail()
  if choice_user == '3':
    clear()
    checkyahoo()
  if choice_user == '4':
    clear()
    print(" Cảm Ơn Bạn Đã Dùng Tool 😆 .")
    quit()
  if choice_user != '1' or '2' or '3' or '4' or '5':
    process_menu()
  if choice_user == '':
    process_menu()
logo() 
process_menu()



CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
BLUE = '\033[94m'
RED = '\033[91m'
RESET = '\033[0m'

import threading
import time
import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from colorama import Fore, Style
# print độc lập
print_lock = threading.Lock()
os.system("")
frames = ['|', '/', '-', '\\']  

# Hàm delay chung với tham số cho hành động và thời gian
def delay_action(second, action_text, is_error=False):
    for i in range(second * 10, 0, -1):
        icon = frames[i % len(frames)]  # Chọn icon theo bước
        color = RED if is_error else CYAN if i % 2 == 0 else BLUE
        bracket_color = YELLOW if i % 2 == 0 else MAGENTA
        print(f"{color}{icon} {action_text} {bracket_color}[{i//10}.{i%10}s]{RESET}", end="\r")
        time.sleep(0.1)
    print(" " * 60, end="\r")  
def delay(second):
    delay_action(second, "Đang chạy job...")
def delay_laplai(second):
    delay_action(second, "Đang lấy job...")
def delay_die(second):
    delay_action(second, "Job lỗi hoặc die => Đang bỏ qua", is_error=True)
def delay_anti(second):
    delay_action(second, "Đang chạy antiband...")
# Tạo profile
def tao_profile_moi():
    index = 1
    while True:
        new_profile_path = os.path.join(base_path, f"chrome_profile_{index}")
        if not os.path.exists(new_profile_path):
            break
        index += 1

    print(f"{CYAN}➡️ Đang tạo profile chrome_profile_{index}, vui lòng đăng nhập GoLike{RESET}")
    driver = create_driver(new_profile_path, headless=False)
    driver.set_window_size(500, 700)
    driver.get("https://app.golike.net/login")
    input("👉 Sau khi đăng nhập xong GoLike, nhấn Enter để tiếp tục...")
    driver.quit()
    print(f"{GREEN}✅ Đã tạo và lưu chrome_profile_{index}{RESET}")
    return new_profile_path 
base_path = os.path.dirname(os.path.abspath(__file__))
profiles = []        
def load_profiles_from_file():
    profiles = []
    if os.path.exists('profiles.txt'):
        with open('profiles.txt', 'r') as file:     
            profiles = [line.strip().split("\\")[-1] for line in file.readlines()]
    return profiles
profiles = load_profiles_from_file()
def save_profiles_to_file(profiles):
    with open('profiles.txt', 'w') as file:
        for profile in profiles:
            file.write(f"{profile}\n")
def kiem_tra_dang_nhap(driver, profile_path, index):
    driver.get("https://app.golike.net/home")
    time.sleep(2)
    while True:
        if driver.current_url == "https://app.golike.net/home":
            print(f"{Fore.GREEN}[Luồng {index}] ✅ Đã đăng nhập GoLike ({profile_path}){Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.YELLOW}[Luồng {index}] ⏳ Đang chờ đăng nhập GoLike ({profile_path}){Style.RESET_ALL}")
            input(f"[Luồng {index}] 🔐 Vui lòng đăng nhập rồi nhấn Enter...")
            driver.get("https://app.golike.net/home")
            time.sleep(2)
def kiem_tra_chon_profile(profiles):
    # Hiển thị danh sách các profile để người dùng chọn
    print(f"{CYAN}===== Danh sách các tài khoản ====={RESET}")
    for idx, profile in enumerate(profiles, start=1):
        print(f"[{idx}] {profile}")
    lua_chon = input(f"[W] Nhập số tài khoản muốn kiểm tra (hoặc nhập 'x' để thoát): ").strip()
    if lua_chon.lower() == 'x':
        return  
    try:
        lua_chon = int(lua_chon)
        if 1 <= lua_chon <= len(profiles):
            profile_path = profiles[lua_chon - 1]
            print(f"{CYAN}➡️ Đang kiểm tra tài khoản: {profile_path}{RESET}")
            driver = create_driver(profile_path, headless=False)
            kiem_tra_dang_nhap(driver, profile_path, lua_chon - 1)
            driver.quit()  # Đóng driver sau khi kiểm tra
        else:
            print(f"{RED}⚠️ Số tài khoản không hợp lệ!{RESET}")
    except ValueError:
        print(f"{RED}⚠️ Vui lòng nhập số hợp lệ!{RESET}")
# Hàm tạo driver với profile
def create_driver(profile_path, headless=False):
    
    options = uc.ChromeOptions()
    #options.add_argument(f'--user-data-dir="{os.path.abspath(profile_path)}"')
    options.add_argument(f"--user-data-dir={os.path.abspath(profile_path)}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--force-device-scale-factor=0.3")
    options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    mobile_ua = "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"
    options.add_argument(f"--user-agent={mobile_ua}")
    #mobile_emulation = { "deviceName": "Pixel 2" }
    #options.add_experimental_option("mobileEmulation", mobile_emulation)
    if headless:
        options.headless = True
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--log-level=3')  # Chỉ hiện lỗi nghiêm trọng
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-software-rasterizer')

    driver = uc.Chrome(options=options, use_subprocess=True)
    return driver

def lam_nhiem_vu_snapchat(driver , index = 0):
    global tongxu, biendem
    try:
        driver.get("https://app.golike.net/jobs/snapchat")
        delay(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/h5/button/i').click()
        delay(1)
        driver.find_element(By.XPATH, '//*[contains(@src, "/assets/images/icons/gold.svg")]').click()
        delay(1)
        driver.find_element(By.XPATH, '//*[contains(@src, "/assets/images/icons/snapchat.svg")]').click()
        delay(1)
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        all_windows = driver.window_handles
        driver.switch_to.window(all_windows[-1])
        driver.close()
        driver.switch_to.window(all_windows[0])
        delay(1)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div').click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.swal2-confirm.swal2-styled'))
        ).click()
        delay(1)
        print(f"{GREEN}Hoàn thành job!{RESET}", end = "\r")
        time.sleep(1)
        print(""*30, end="\r")  
        print(f" [Luồng {index}] {CYAN}|   SNAPCHAT |{GREEN} Hoàn Thành {RESET}| {BLUE}Time: {datetime.now().strftime('%H:%M:%S')}{RESET} |")
        #tongxu += 50
        #biendem += 1
        #print(f" [Luồng: {index}] {CYAN}| {biendem} |  SNAPCHAT  |{GREEN} Hoàn Thành {RESET}| {YELLOW}+50 đ{RESET} | {MAGENTA}Tổng xu: {tongxu}{RESET} | {BLUE}Time: {datetime.now().strftime('%H:%M:%S')}{RESET} |")
    except:
        delay_die(1)
        print(f"{GREEN}[Luồng {index}] Lỗi Job! => bỏ qua thành công....{RESET}", end="\r")
        print(""*30, end="\r")

def lam_nhiem_vu_thread(driver, index = 0):
    global tongxu, biendem
    try:
        driver.get("https://app.golike.net/jobs/thread")
        delay(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/h5/button/i').click()
        delay(2)
        kt_job = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/span/span')
        #job_text = kt_job.text 
        kt_job.click()
        delay(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div/a/div[3]/i').click()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        all_windows = driver.window_handles
        driver.switch_to.window(all_windows[-1])
        driver.close()
        driver.switch_to.window(all_windows[0])
        delay(2)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div/div[3]/i').click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.swal2-confirm.swal2-styled'))
        ).click()
        delay(2)
        print(f"{GREEN}Hoàn thành job!{RESET}", end = "\r")
        time.sleep(1)
        print(""*30, end="\r")
        #xu_number = int(job_text.split()[0])
        print(f" [Luồng {index}] {CYAN}|   THREADS  |{GREEN} Hoàn Thành {RESET}| {BLUE}Time: {datetime.now().strftime('%H:%M:%S')}{RESET} |")
        #tongxu += xu_number
        #biendem += 1
        #print(f" [Luồng: {index}] {CYAN}| {biendem} |   THREAD   |{GREEN} Hoàn Thành {RESET}| {YELLOW}+{job_text}{RESET} | {MAGENTA}Tổng xu: {tongxu}{RESET} | {BLUE}Time: {datetime.now().strftime('%H:%M:%S')}{RESET} |")
    except :
        delay_die(2)
        print(f"{GREEN}[Luồng {index}] Lỗi Job! => bỏ qua thành công....{RESET}", end="\r")
        print(""*30, end="\r")
def lam_nhiem_vu_linkedin(driver, index = 0):
    global tongxu, biendem
    try:
        # ko dc pc
        driver.get("https://app.golike.net/jobs/linkedin")
        delay(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div[2]/h5/button/i').click()
        delay(2)
        kt_job = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/span/span')
        #job_text = kt_job.text 
        kt_job.click()
        delay(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div/a/div[3]/i').click()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        all_windows = driver.window_handles
        driver.switch_to.window(all_windows[-1])
        driver.close()
        driver.switch_to.window(all_windows[0])
        delay(1)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div/div[3]/i').click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.swal2-confirm.swal2-styled'))
        ).click()
        delay(1)
        print(f"{GREEN}Hoàn thành job!{RESET}", end = "\r")
        time.sleep(1)
        print(""*30, end="\r")
        #xu_number = int(job_text.split()[0])
        #tongxu += xu_number
        #biendem += 1
        print(f" [Luồng {index}] {CYAN}|  LINKEDIN  |{GREEN} Hoàn Thành {RESET}| {BLUE}Time: {datetime.now().strftime('%H:%M:%S')}{RESET} |")
        #print(f" [Luồng: {index}] {CYAN}| {biendem} |  LINKEDIN  |{GREEN} Hoàn Thành {RESET}| {YELLOW}+{job_text}{RESET} | {MAGENTA}Tổng xu: {tongxu}{RESET} | {BLUE}Time: {datetime.now().strftime('%H:%M:%S')}{RESET} |")
    except:
        delay_die(1)
        print(f"{GREEN}[Luồng {index}] Lỗi Job! => bỏ qua thành công....{RESET}", end="\r")
        print(""*30, end="\r")
def lam_nhiem_vu_IG(driver, index = 0):
    global tongxu, biendem
    try:
        driver.get("https://app.golike.net/jobs/instagram")
        delay(5)
        kt = driver.find_element(By.XPATH, '//i[@style = "vertical-align: sub; font-size: 17px;"]')
        kt.click()
        delay(10)
        elements = driver.find_elements(By.XPATH, '//img[@style = "vertical-align: sub; width: 18px;"]')
        delay(10)
        if len(elements) >= 2:
            elements[1].click()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        all_windows = driver.window_handles
        driver.switch_to.window(all_windows[1])
        driver.close()
        driver.switch_to.window(all_windows[0])
        delay(40) 
        nut = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, '//img[@style = "width: 19px;"]'))
        )
        nut.click()
        delay(40)
        WebDriverWait(driver, 100).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.swal2-confirm.swal2-styled'))
        ).click()

        #tongxu += 42
        #biendem += 1
        print(f" [Luồng {index}] {CYAN}|  INSTAGRAM |{GREEN} Hoàn Thành {RESET}| {BLUE}Time: {datetime.now().strftime('%H:%M:%S')}{RESET} |")
        #print(f" [Luồng {index}] {CYAN}| {biendem} |  INSTAGRAM |{GREEN} Hoàn Thành {RESET}| {YELLOW}+42 đ{RESET} | {MAGENTA}Tổng xu: {tongxu}{RESET} | {BLUE}Time: {datetime.now().strftime('%H:%M:%S')}{RESET} |")
    except:
        delay_die(1)
        print(f"{GREEN}[Luồng {index}] Lỗi Job! => bỏ qua thành công....{RESET}", end="\r")
        print(""*30, end="\r")

# Hàm làm nhiệm vụ Facebook Like cho mỗi profile
def lam_job(profile_path, index=0):
    driver = create_driver(profile_path, headless=False)
    driver.set_window_size(500, 700)
    driver.set_window_position(x=550 * index, y=0 )  
    # Nhiệm vụ
    os.system('cls')
    while True:
        delay_anti(2)
        lam_nhiem_vu_snapchat(driver, index)
        delay_anti(2)
        lam_nhiem_vu_thread(driver, index)
        delay_anti(2)
        lam_nhiem_vu_linkedin(driver, index)
        delay_anti(2)
        lam_nhiem_vu_IG(driver, index)
# Hàm chạy đa luồng với delay giữa các luồng
def chay_da_luong(profile_paths, delay=5):
    threads = []
    for index, profile_path in enumerate(profile_paths):
        time.sleep(delay * index)
        t = threading.Thread(target=lam_job, args=(profile_path, index))
        t.daemon = True 
        print(f"Đang mở: {profile_path} [Luồng thứ {index}] ")
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
def tat_chrome_hieu_ung():
    os.system("")
    frames = ['|', '/', '-', '\\']  
    try:
        print("\033[1;33mĐang tắt trình duyệt Chrome", end="", flush=True)  
        for i in range(20): 
            print(f"\r\033[1;33mĐang tắt trình duyệt Chrome {frames[i % len(frames)]}", end="", flush=True)
            time.sleep(0.2)
        os.system('taskkill /f /im chrome.exe >nul 2>&1')
        time.sleep(0.5)
        print("\n\0033[1;32mĐã tắt Chrome thành công.") 
    except Exception as e:
        print("\n\033[1;31m❌ Lỗi khi tắt Chrome:", e)  
 #Menu UI
def ui():
    while True:
        os.system('cls')
        print(f"""
{CYAN}===== MENU ====={RESET}
[1]  Thêm tài khoản Golike
[2]  Kiểm tra đăng nhập Golike
[3]  Làm nhiệm vụ Golike (đa luồng 🤑)
[X]  Out tool
        """)
        lua_chon = input("[W] Nhập lựa chọn: ").strip()
        profiles = load_profiles_from_file()  # Đọc lại danh sách profile từ file

        if lua_chon == "1":
            profile_path = tao_profile_moi()
            if profile_path not in profiles:
                profiles.append(profile_path)
                save_profiles_to_file(profiles)  # Lưu lại danh sách profile vào file
        elif lua_chon == "2":
            kiem_tra_chon_profile(profiles)

        elif lua_chon == "3":
            try:
                tat_chrome_hieu_ung()
                chay_da_luong(profiles)
            except Exception as e:
                print(e)
                break
        elif lua_chon.lower() == "x":
            break
# Thực thi chương trình với 3 profile
if __name__ == "__main__":
    ui()

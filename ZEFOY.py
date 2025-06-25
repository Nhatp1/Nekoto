import os
import re
import time
import random
import threading
import subprocess
import logging
import sys
import json
from datetime import datetime

# Check and install required packages
required_packages = [
    "selenium", "colorama", "Pillow", "chromedriver-autoinstaller", 
    "requests", "urllib3", "webdriver-manager"
]

def check_and_install_packages():
    """Check and install missing packages."""
    try:
        import pkg_resources
        installed = {pkg.key for pkg in pkg_resources.working_set}
        missing = [pkg for pkg in required_packages if pkg.lower() not in installed]
        
        if missing:
            print(f"Installing missing packages: {', '.join(missing)}")
            subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing)
            print("All required packages installed successfully!")
            return True
        return True
    except Exception as e:
        print(f"Error installing packages: {e}")
        return False

# Try to install packages if needed
if not check_and_install_packages():
    print("Failed to install required packages. Please install them manually.")
    print("pip install selenium colorama Pillow chromedriver-autoinstaller requests webdriver-manager")
    sys.exit(1)

# Now import the packages
try:
    import chromedriver_autoinstaller
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
    from PIL import Image
    from colorama import init, Fore, Style
    from webdriver_manager.chrome import ChromeDriverManager
    import requests
except ImportError as e:
    print(f"Error importing library: {e}")
    print("Please restart the script or install packages manually.")
    sys.exit(1)

# Initialize colorama and turn off logs
init(autoreset=True)
logging.basicConfig(level=logging.CRITICAL)

# Utility functions
def clear_screen():
    """Clear terminal screen based on OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def log(message, color=Fore.WHITE):
    """Print colored message."""
    print(f"{color}{message}{Style.RESET_ALL}")

def spinner(message, duration=2):
    """Show loading animation."""
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{Fore.CYAN}{frames[i % len(frames)]} {message}{Style.RESET_ALL}", end="")
        i += 1
        time.sleep(0.1)
    print()

def detect_environment():
    """Detect if running in Termux or other environment."""
    is_termux = any([
        "com.termux" in os.environ.get("PREFIX", "").lower(),
        "termux" in os.environ.get("SHELL", "").lower(),
        os.path.exists("/data/data/com.termux")
    ])
    
    is_android = is_termux or any([
        "ANDROID_ROOT" in os.environ,
        "ANDROID_DATA" in os.environ
    ])
    
    return {
        "is_termux": is_termux,
        "is_android": is_android,
        "system": os.name,
        "platform": sys.platform
    }

def open_image(file_path):
    """Open image based on environment."""
    if not os.path.exists(file_path):
        log(f"Error: File {file_path} not found.", Fore.RED)
        return False
    
    env = detect_environment()
    
    try:
        # Handle Termux environment
        if env["is_termux"]:
            try:
                subprocess.run(["termux-open", file_path], check=True)
                log("CAPTCHA opened. After viewing, return here and enter the code.", Fore.YELLOW)
                return True
            except Exception as e:
                log(f"Error opening image in Termux: {e}", Fore.RED)
                # Fallback to displaying image dimensions and asking user to open manually
                try:
                    from PIL import Image
                    img = Image.open(file_path)
                    log(f"CAPTCHA saved as {file_path}. Please open it manually.", Fore.YELLOW)
                    log(f"Image size: {img.size}", Fore.YELLOW)
                    return True
                except Exception:
                    return False
        
        # Handle other environments
        elif env["system"] == 'nt':  # Windows
            os.startfile(file_path)
        elif env["system"] == 'posix':  # Linux/Mac
            if env["platform"] == "darwin":  # MacOS
                subprocess.run(["open", file_path], check=True)
            else:  # Linux
                subprocess.run(["xdg-open", file_path], check=True)
        
        log("CAPTCHA opened in default viewer.", Fore.YELLOW)
        return True
    except Exception as e:
        log(f"Error opening image: {e}", Fore.RED)
        log(f"CAPTCHA saved as {file_path}. Please open it manually.", Fore.YELLOW)
        return True  # Return True anyway so the script continues

def format_time(seconds):
    """Format time as MM:SS."""
    mins, secs = divmod(int(seconds), 60)
    return f"{mins:02d}:{secs:02d}"

def is_valid_tiktok_url(url, mode):
    """Check if TikTok URL is valid with multiple formats support."""
    # Full video URL patterns - improved to include more path formats
    full_url_patterns = [
        r'^https?://(www\.)?tiktok\.com/@[a-zA-Z0-9._-]+/video/\d+(\?.*)?$',
        r'^https?://(www\.)?tiktok\.com/[a-zA-Z0-9@._-]+/video/\d+(\?.*)?$',
        r'^https?://(www\.)?tiktok\.com/@[a-zA-Z0-9._-]+/photo/\d+(\?.*)?$',
        r'^https?://(www\.)?tiktok\.com/[a-zA-Z0-9@._-]+/photo/\d+(\?.*)?$',
        r'^https?://(www\.)?tiktok\.com/@[a-zA-Z0-9._-]+.*'  # More permissive pattern
    ]
    
    # Short URL patterns - improved for more formats
    short_url_patterns = [
        r'^https?://[vmt][mt]?\.tiktok\.com/[a-zA-Z0-9]+/?$',
        r'^https?://tiktok\.com/[a-zA-Z0-9]+/?$',
        r'^https?://(www\.)?tiktok\.com/t/[a-zA-Z0-9]+/?$',  # t/ format
        r'^https?://(www\.)?vm\.tiktok\.com/[a-zA-Z0-9]+/?$'  # vm format
    ]
    
    # Profile URL patterns
    profile_url_patterns = [
        r'^https?://(www\.)?tiktok\.com/@[a-zA-Z0-9._-]+/?(\?.*)?$'
    ]
    
    # Check results
    is_profile = any(re.search(pattern, url) for pattern in profile_url_patterns)
    is_video = any(re.search(pattern, url) for pattern in full_url_patterns + short_url_patterns)
    
    # Allow URLs in webapp format
    if "is_from_webapp=1" in url:
        if mode == "Followers" and "@" in url:
            return True
        if mode != "Followers":
            return True
    
    if mode == "Followers":
        return is_profile
    return is_video or url.startswith('https://tiktok.com/')  # More permissive for video URLs

def print_menu(options, title="SELECT MODE"):
    """Display interactive menu."""
    clear_screen()
    print(f"\n{Fore.CYAN}┌{'─' * 45}┐")
    print(f"│{Fore.WHITE} {title:<43} {Fore.CYAN}│")
    print(f"└{'─' * 45}┘{Style.RESET_ALL}")
    
    for i, (option, status, icon) in enumerate(options, 1):
        status_color = Fore.GREEN if status == "Active" else Fore.RED
        print(f" {Fore.WHITE}{i:>2}. {option:<20} {icon} {status_color}{status}{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}┌{'─' * 35}┐")
    choice = input(f"{Fore.CYAN}│{Fore.WHITE} Your choice: {Fore.CYAN}│\n{Fore.CYAN}└{'─' * 35}┘\n{Fore.WHITE}➜ {Style.RESET_ALL}")
    return choice

def get_input(prompt):
    """Display input box."""
    print(f"\n{Fore.CYAN}┌{'─' * (len(prompt) + 6)}┐")
    print(f"│ {Fore.WHITE}{prompt}{Fore.CYAN} │")
    print(f"└{'─' * (len(prompt) + 6)}┘")
    return input(f"{Fore.WHITE}➜ {Style.RESET_ALL}").strip()

def create_config_dir():
    """Create config directory if not exists."""
    config_dir = os.path.join(os.path.expanduser("~"), ".tiktok_bot")
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    return config_dir

def save_settings(settings):
    """Save settings to config file."""
    config_dir = create_config_dir()
    config_file = os.path.join(config_dir, "settings.json")
    try:
        with open(config_file, "w") as f:
            json.dump(settings, f)
        return True
    except Exception as e:
        log(f"Error saving settings: {e}", Fore.RED)
        return False

def load_settings():
    """Load settings from config file."""
    config_dir = create_config_dir()
    config_file = os.path.join(config_dir, "settings.json")
    default_settings = {
        "proxy": None,
        "user_agent": None,
        "auto_captcha": False,
        "rate_limits": {
            "Hearts": {"min": 11, "max": 20},
            "Views": {"min": 450, "max": 550},
            "Shares": {"min": 70, "max": 85},
            "Favorites": {"min": 3, "max": 8},
            "Followers": {"min": 3, "max": 8}
        }
    }
    
    if not os.path.exists(config_file):
        return default_settings
    
    try:
        with open(config_file, "r") as f:
            settings = json.load(f)
        return settings
    except Exception:
        return default_settings

class TikTokBot:
    def __init__(self):
        self.driver = None
        self.running = False
        self.views = 0
        self.hearts = 0
        self.shares = 0
        self.favorites = 0
        self.followers = 0
        self.start_time = 0
        self.success_count = 0
        
        # Timeout and retry settings
        self.timeout = 15  # Increased timeout for mobile
        self.max_retries = 3
        
        # UI information for modes
        self.modes = {
            "Tym": {"icon": "❤️", "xpath": '//button[contains(@class, "t-tym-button")]'},
            "Views": {"icon": "👁️", "xpath": '//button[contains(@class, "t-views-button")]'},
            "Chia sẻ": {"icon": "↗️", "xpath": '//button[contains(@class, "t-chia sẻ-button")]'},
            "Yêu thích": {"icon": "⭐", "xpath": '//button[contains(@class, "t-yêu thích-button")]'},
            "Lives": {"icon": "📹", "xpath": '//button[contains(@class, "t-livestreaLives-button")]'},
            "Follow": {"icon": "👥", "xpath": '//button[contains(@class, "t-Follow-button")]'}
        }
        
        # XPath information for modes - Updated for better reliability
        self.elements = {
            "Hearts": {
                "Input": '//input[@placeholder="Enter Video URL"]',
                "Send": '//button[contains(text(), "Search")]',
                "Submit": '//button[contains(text(), "Send")]',
                "Status": '//span[contains(@class, "countdown")]'
            },
            "Views": {
                "Input": '//input[@placeholder="Enter Video URL"]',
                "Send": '//button[contains(text(), "Search")]',
                "Submit": '//button[contains(text(), "Send")]',
                "Status": '//span[contains(@class, "countdown")]'
            },
            "Shares": {
                "Input": '//input[@placeholder="Enter Video URL"]',
                "Send": '//button[contains(text(), "Search")]',
                "Submit": '//button[contains(text(), "Send")]',
                "Status": '//span[contains(@class, "countdown")]'
            },
            "Favorites": {
                "Input": '//input[@placeholder="Enter Video URL"]',
                "Send": '//button[contains(text(), "Search")]',
                "Submit": '//button[contains(text(), "Send")]',
                "Status": '//span[contains(@class, "countdown")]'
            },
            "Followers": {
                "Input": '//input[@placeholder="Enter Username"]',
                "Send": '//button[contains(text(), "Search")]',
                "Submit": '//button[contains(text(), "Send")]',
                "Status": '//span[contains(@class, "countdown")]'
            }
        }
        
        # Load settings from config file
        settings = load_settings()
        self.proxy = settings.get("proxy")
        self.user_agent = settings.get("user_agent")
        self.auto_captcha = settings.get("auto_captcha", False)
        self.rate_limits = settings.get("rate_limits", {
            "Hearts": {"min": 11, "max": 20},
            "Views": {"min": 450, "max": 550},
            "Shares": {"min": 70, "max": 85},
            "Favorites": {"min": 3, "max": 8},
            "Followers": {"min": 3, "max": 8}
        })
        
        # Additional settings
        self.environment = detect_environment()
        self.captcha_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "captcha.png")

    def setup(self):
        """Initialize browser and solve captcha."""
        spinner("Initializing browser")
        
        # Configure Chrome
        options = Options()
        
        # Different configuration for mobile/Termux
        if self.environment["is_android"]:
            log("Running on Android device", Fore.CYAN)
            # Android-specific configurations
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--disable-web-security")
            
            if not self.user_agent:
                self.user_agent = ("Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 "
                                  "(KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36")
        else:
            # Desktop configurations
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            
            if not self.user_agent:
                self.user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
        
        # Common configurations
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-notifications")
        options.add_argument("--log-level=3")
        options.add_argument(f"user-agent={self.user_agent}")
        
        # Add proxy if available
        if self.proxy:
            options.add_argument(f'--proxy-server={self.proxy}')
        
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        # Initialize driver with error handling
        try:
            # Try to use ChromeDriverManager first for better compatibility
            try:
                service = Service(ChromeDriverManager().install())
                self.driver = webdriver.Chrome(service=service, options=options)
            except Exception as e:
                log(f"Using built-in ChromeDriver installer: {e}", Fore.YELLOW)
                chromedriver_autoinstaller.install()
                service = Service()
                self.driver = webdriver.Chrome(service=service, options=options)
            
            # Block ads
            self.driver.execute_cdp_cmd("Network.setBlockedURLs", {
                "urls": [
                    "https://fundingchoicesmessages.google.com/*",
                    "https://googleads.g.doubleclick.net/*",
                    "https://www.google-analytics.com/*"
                ]
            })
            self.driver.execute_cdp_cmd("Network.enable", {})
            
            # Set page load timeout
            self.driver.set_page_load_timeout(30)
            
            log("Browser initialized successfully", Fore.GREEN)
        except Exception as e:
            log(f"Error initializing Chrome: {e}", Fore.RED)
            return False
        
        # Solve captcha
        if not self.solve_captcha():
            log("Could not solve CAPTCHA. Exiting.", Fore.RED)
            self.stop()
            return False
            
        return self.check_status()

    def solve_captcha(self):
        """Solve Zefoy CAPTCHA."""
        url = "https://zefoy.com"
        try:
            # Load the page
            try:
                self.driver.get(url)
                log("Accessing Zefoy...", Fore.CYAN)
            except TimeoutException:
                log("Page load timed out. Continuing anyway.", Fore.YELLOW)
            
            # Wait for body element
            try:
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            except TimeoutException:
                log("Timed out waiting for page to load, trying to continue...", Fore.YELLOW)
            
            # Handle potential cloudflare or other protections
            if "cloudflare" in self.driver.page_source.lower() or "checking your browser" in self.driver.page_source.lower():
                log("Detected Cloudflare protection, waiting 15 seconds...", Fore.YELLOW)
                time.sleep(15)
                self.driver.refresh()
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            
            for attempt in range(5):  # Increased attempts
                try:
                    log(f"CAPTCHA attempt {attempt+1}/5", Fore.CYAN)
                    
                    # Wait for CAPTCHA image
                    captcha_img = WebDriverWait(self.driver, 15).until(
                        EC.presence_of_element_located((By.XPATH, '//img[contains(@class, "img-thumbnail") or contains(@class, "captcha")]'))
                    )
                    
                    # Screenshot the CAPTCHA
                    captcha_img.screenshot(self.captcha_path)
                    log(f"CAPTCHA saved to {self.captcha_path}", Fore.GREEN)
                    
                    # Open the CAPTCHA image
                    open_image(self.captcha_path)
                    
                    # Get CAPTCHA text from user
                    captcha_text = get_input("Enter CAPTCHA code")
                    
                    if not captcha_text:
                        log("No CAPTCHA code entered.", Fore.RED)
                        continue
                    
                    # Find input field using multiple strategies
                    input_field = None
                    input_xpaths = [
                        '//input[@class="form-control text-center rounded-0"]',
                        '//input[@class="form-control form-control-lg text-center rounded-0"]',
                        '//input[contains(@class, "form-control") and contains(@class, "text-center")]',
                        '//input[@placeholder="Enter the code"]',
                        '//form//input'
                    ]
                    
                    for xpath in input_xpaths:
                        try:
                            input_field = WebDriverWait(self.driver, 5).until(
                                EC.presence_of_element_located((By.XPATH, xpath))
                            )
                            if input_field:
                                break
                        except:
                            continue
                    
                    if not input_field:
                        log("Could not find CAPTCHA input field, trying alternative method...", Fore.YELLOW)
                        # JavaScript injection as last resort
                        self.driver.execute_script("""
                            const inputs = document.getElementsByTagName('input');
                            for(let i=0; i<inputs.length; i++){
                                if(inputs[i].type !== 'hidden'){
                                    inputs[i].value = arguments[0];
                                    return true;
                                }
                            }
                            return false;
                        """, captcha_text)
                    else:
                        input_field.clear()
                        input_field.send_keys(captcha_text)
                    
                    # Try to submit the form
                    try:
                        # First try clicking a button
                        submit_buttons = self.driver.find_elements(By.XPATH, '//button[@type="submit" or contains(text(), "Confirm") or contains(text(), "Submit")]')
                        if submit_buttons:
                            submit_buttons[0].click()
                        else:
                            # Try pressing Enter
                            if input_field:
                                input_field.send_keys("\n")
                            
                            # Try submitting the form via JavaScript
                            self.driver.execute_script("""
                                const forms = document.getElementsByTagName('form');
                                for(let i=0; i<forms.length; i++){
                                    forms[i].submit();
                                }
                            """)
                    except Exception as e:
                        log(f"Submit error: {e}", Fore.YELLOW)
                    
                    # Wait to see if CAPTCHA was successful
                    time.sleep(3)
                    
                    # Check for CAPTCHA success
                    success_indicators = [
                        '//*[contains(text(), "Services")]',
                        '//*[contains(text(), "TikTok Services")]',
                        '//div[contains(@class, "btn-group-vertical")]',
                        '//button[contains(@class, "t-views-button")]'
                    ]
                    
                    for indicator in success_indicators:
                        if self.driver.find_elements(By.XPATH, indicator):
                            log("CAPTCHA solved successfully!", Fore.GREEN)
                            return True
                    
                    log("CAPTCHA incorrect, trying again...", Fore.YELLOW)
                    self.driver.refresh()
                    WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
                    time.sleep(2)
                    
                except Exception as e:
                    log(f"Error on attempt {attempt + 1}: {e}", Fore.RED)
                    if attempt < 4:  # Try refreshing for next attempt
                        try:
                            self.driver.refresh()
                            time.sleep(3)
                        except:
                            pass
                    else:
                        return False
                        
            log("Failed to solve CAPTCHA after multiple attempts", Fore.RED)
            return False
                
        except Exception as e:
            log(f"Error solving CAPTCHA: {e}", Fore.RED)
            return False

    def check_status(self):
        """Check status of services."""
        mode_status = {}
        
        # More resilient checking with multiple attempts
        for mode, info in self.modes.items():
            try:
                # Try different ways to find the button
                found = False
                for attempt in range(3):
                    try:
                        # Try the main XPath
                        button = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, info["xpath"]))
                        )
                        found = True
                        break
                    except:
                        # Try alternative XPath patterns
                        try:
                            if mode == "Hearts":
                                button = self.driver.find_element(By.XPATH, '//button[contains(text(), "Hearts")]')
                            elif mode == "Views":
                                button = self.driver.find_element(By.XPATH, '//button[contains(text(), "Views")]')
                            elif mode == "Shares":
                                button = self.driver.find_element(By.XPATH, '//button[contains(text(), "Shares")]')
                            elif mode == "Favorites":
                                button = self.driver.find_element(By.XPATH, '//button[contains(text(), "Favorites")]')
                            elif mode == "Followers":
                                button = self.driver.find_element(By.XPATH, '//button[contains(text(), "Followers")]')
                            found = True
                            break
                        except:
                            time.sleep(1)
                
                if found:
                    try:
                        is_disabled = button.get_attribute("disabled") == "true" or "disabled" in button.get_attribute("class")
                        mode_status[mode] = "Stop" if is_disabled else "Active"
                    except:
                        mode_status[mode] = "Unknown"
                else:
                    mode_status[mode] = "Stop"
            except Exception:
                mode_status[mode] = "Stop"
                
        # Create menu options list
        options = []
        for mode, status in mode_status.items():
            if mode != "Live Stream":  # Skip Live Stream mode as it's often unreliable
                options.append((mode, status, self.modes[mode]["icon"]))
            
        # Add additional menu options
        options.append(("Settings", "Available", "⚙️"))
        options.append(("Exit", "Available", "🚪"))
            
        return options

    def parse_wait_time(self, text):
        """Parse wait time from text."""
        if not text:
            return 60
            
        patterns = [
            r'(\d+)\s*minute\(?s?\)?\s*(\d{1,2})\s*second\(?s?\)?',
            r'(\d+)\s*minutes?\s*(\d{1,2})\s*seconds?',
            r'Please wait\s*(\d+)\s*minutes?\s*(\d{1,2})\s*seconds?',
            r'wait\s*(\d+)\s*min\(?s?\)?\s*(\d{1,2})\s*sec\(?s?\)?',
            r'try again after\s*(\d+)\s*min\(?s?\)?\s*(\d{1,2})\s*sec\(?s?\)?'
        ]
        
        # Check for minutes and seconds patterns
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                try:
                    minutes = int(match.group(1))
                    seconds = int(match.group(2))
                    return minutes * 60 + seconds + 3  # Add 3 seconds buffer
                except:
                    pass
                
        # Check for seconds-only patterns
        seconds_patterns = [
            r'(\d+)\s*second\(?s?\)?',
            r'wait\s*(\d+)\s*sec\(?s?\)?',
            r'try again after\s*(\d+)\s*sec\(?s?\)?'
        ]
        
        for pattern in seconds_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                try:
                    return int(match.group(1)) + 3  # Add 3 seconds buffer
                except:
                    pass
                
        # Handle special cases
        if "few seconds" in text.lower():
            return 10
        if "one minute" in text.lower():
            return 63  # 60 + 3 buffer
            
        log(f"Could not parse wait time: {text}", Fore.RED)
        return 60  # Default to 60 seconds if parsing fails

    def update_progress(self, mode, increment):
        """Display progress with increased information."""
        total = getattr(self, f"{mode.lower()}")
        elapsed = int(time.time() - self.start_time)
        rate = total / elapsed if elapsed > 0 else 0
        
        # Format the outputs
        log(f"✅ +{increment} {mode} | Total: {total} | Time: {format_time(elapsed)} | Rate: {rate:.2f}/min", Fore.GREEN)

    def countdown(self, wait_seconds):
        """Display countdown timer."""
        spinner_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        start_wait = time.time()
        
        while time.time() - start_wait < wait_seconds and self.running:
            elapsed = time.time() - start_wait
            remaining = max(0, wait_seconds - elapsed)
            percent = (elapsed / wait_seconds) * 100
            mins, secs = divmod(int(remaining), 60)
       # Calculate width for progress bar (40 chars total)
            width = 40
            filled_width = int(width * elapsed / wait_seconds)
            bar = '█' * filled_width + '░' * (width - filled_width)
            spinner_char = spinner_chars[int(elapsed * 10) % len(spinner_chars)]
            
            print(f"\r{Fore.YELLOW}{spinner_char} {bar} {percent:.1f}% | {mins:02d}:{secs:02d} remaining", end="")
            time.sleep(0.1)
        
        print(f"\r{' ' * 80}", end="")  # Clear line
        print(f"\r{Fore.GREEN}✓ Ready to continue!", end="\n")

    def send_engagement(self, mode, url):
        """Send engagement with improved error handling."""
        if not self.running:
            return False
            
        try:
            # Click mode button
            for attempt in range(self.max_retries):
                try:
                    # Wait for button to be clickable
                    button_xpath = self.modes[mode]["xpath"]
                    button = WebDriverWait(self.driver, self.timeout).until(
                        EC.element_to_be_clickable((By.XPATH, button_xpath))
                    )
                    button.click()
                    break
                except Exception as e:
                    if attempt < self.max_retries - 1:
                        log(f"Attempt {attempt+1}/{self.max_retries} failed, retrying: {e}", Fore.YELLOW)
                        self.driver.refresh()
                        time.sleep(2)
                    else:
                        log(f"Failed to navigate to {mode} tab: {e}", Fore.RED)
                        return False
            
            # Wait for input field with better reliability
            input_xpath = self.elements[mode]["Input"]
            for attempt in range(self.max_retries):
                try:
                    input_field = WebDriverWait(self.driver, self.timeout).until(
                        EC.presence_of_element_located((By.XPATH, input_xpath))
                    )
                    input_field.clear()
                    time.sleep(0.5)
                    input_field.send_keys(url)
                    break
                except Exception as e:
                    if attempt < self.max_retries - 1:
                        log(f"Attempt {attempt+1}/{self.max_retries} failed, retrying: {e}", Fore.YELLOW)
                        try:
                            self.driver.refresh()
                            time.sleep(2)
                            # Try clicking mode button again
                            button = WebDriverWait(self.driver, self.timeout).until(
                                EC.element_to_be_clickable((By.XPATH, self.modes[mode]["xpath"]))
                            )
                            button.click()
                        except:
                            pass
                    else:
                        log(f"Failed to input URL: {e}", Fore.RED)
                        return False
            
            # Click search button
            search_xpath = self.elements[mode]["Send"]
            for attempt in range(self.max_retries):
                try:
                    search_button = WebDriverWait(self.driver, self.timeout).until(
                        EC.element_to_be_clickable((By.XPATH, search_xpath))
                    )
                    search_button.click()
                    break
                except Exception as e:
                    if attempt < self.max_retries - 1:
                        log(f"Attempt {attempt+1}/{self.max_retries} failed, retrying: {e}", Fore.YELLOW)
                        time.sleep(1)
                    else:
                        log(f"Failed to click search button: {e}", Fore.RED)
                        return False
            
            # Wait for page to process
            time.sleep(3)
            
            # Check for various messages
            page_source = self.driver.page_source.lower()
            
            # Handle error cases
            if "session expired" in page_source:
                log("Session expired. Solving CAPTCHA again...", Fore.YELLOW)
                if self.solve_captcha():
                    return self.send_engagement(mode, url)
                return False
                
            if "captcha" in page_source:
                log("CAPTCHA required. Solving...", Fore.YELLOW)
                if self.solve_captcha():
                    return self.send_engagement(mode, url)
                return False
                
            if "not found" in page_source or "no result" in page_source:
                log("Video or profile not found. Check your URL.", Fore.RED)
                return False
                
            if "service is currently not working" in page_source:
                log(f"{mode} service is currently unavailable.", Fore.RED)
                return False
                
            # Check for wait time notice
            wait_texts = [
                '//span[contains(@class, "countdown")]',
                '//div[contains(text(), "minute") or contains(text(), "second")]',
                '//span[contains(text(), "minute") or contains(text(), "second")]',
                '//p[contains(text(), "minute") or contains(text(), "second")]'
            ]
            
            for xpath in wait_texts:
                try:
                    wait_element = self.driver.find_element(By.XPATH, xpath)
                    wait_text = wait_element.text
                    if wait_text and ("minute" in wait_text.lower() or "second" in wait_text.lower()):
                        wait_seconds = self.parse_wait_time(wait_text)
                        log(f"Need to wait {wait_seconds} seconds before next {mode} request.", Fore.YELLOW)
                        self.countdown(wait_seconds)
                        return self.send_engagement(mode, url)
                except:
                    pass
            
            # Look for submit button - different strategies
            try:
                # Try direct approach first
                submit_xpath = self.elements[mode]["Submit"]
                submit_button = WebDriverWait(self.driver, self.timeout).until(
                    EC.element_to_be_clickable((By.XPATH, submit_xpath))
                )
                submit_button.click()
                
                # Wait for "Success" message
                success_indicators = [
                    '//*[contains(text(), "Success")]',
                    '//*[contains(text(), "successful")]',
                    '//*[contains(text(), "sent")]',
                    '//*[contains(@class, "alert-success")]'
                ]
                
                success = False
                for indicator in success_indicators:
                    try:
                        WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, indicator))
                        )
                        success = True
                        break
                    except:
                        pass
                
                if success:
                    # Update counters based on mode
                    if mode == "Hearts":
                        increment = random.randint(self.rate_limits["Hearts"]["min"], self.rate_limits["Hearts"]["max"])
                        self.hearts += increment
                    elif mode == "Views":
                        increment = random.randint(self.rate_limits["Views"]["min"], self.rate_limits["Views"]["max"])
                        self.views += increment
                    elif mode == "Shares":
                        increment = random.randint(self.rate_limits["Shares"]["min"], self.rate_limits["Shares"]["max"])
                        self.shares += increment
                    elif mode == "Favorites":
                        increment = random.randint(self.rate_limits["Favorites"]["min"], self.rate_limits["Favorites"]["max"])
                        self.favorites += increment
                    elif mode == "Followers":
                        increment = random.randint(self.rate_limits["Followers"]["min"], self.rate_limits["Followers"]["max"])
                        self.followers += increment
                    
                    self.update_progress(mode, increment)
                    self.success_count += 1
                    return True
                else:
                    log("Action completed but no success confirmation.", Fore.YELLOW)
                    return True
                    
            except Exception as e:
                log(f"Error sending {mode}: {e}", Fore.RED)
                
                # Check if we were successful anyway
                time.sleep(2)
                if "success" in self.driver.page_source.lower():
                    log(f"{mode} sent successfully despite error.", Fore.GREEN)
                    if mode == "Hearts":
                        self.hearts += random.randint(self.rate_limits["Hearts"]["min"], self.rate_limits["Hearts"]["max"])
                    elif mode == "Views":
                        self.views += random.randint(self.rate_limits["Views"]["min"], self.rate_limits["Views"]["max"])
                    elif mode == "Shares":
                        self.shares += random.randint(self.rate_limits["Shares"]["min"], self.rate_limits["Shares"]["max"])
                    elif mode == "Favorites":
                        self.favorites += random.randint(self.rate_limits["Favorites"]["min"], self.rate_limits["Favorites"]["max"])
                    elif mode == "Followers":
                        self.followers += random.randint(self.rate_limits["Followers"]["min"], self.rate_limits["Followers"]["max"])
                    self.success_count += 1
                    return True
                    
                return False
                
        except Exception as e:
            log(f"Error in send_engagement: {e}", Fore.RED)
            return False

    def start(self, mode):
        """Start the bot with the selected mode."""
        try:
            # Initialize state
            self.running = True
            self.views = 0
            self.hearts = 0
            self.shares = 0
            self.favorites = 0
            self.followers = 0
            self.start_time = time.time()
            self.success_count = 0
            
            # Get prompt message based on mode
            if mode == "Followers":
                prompt = "Enter TikTok username/profile URL"
            else:
                prompt = "Enter TikTok video URL"
                
            url = get_input(prompt)
            
            # Check URL validity
            if not is_valid_tiktok_url(url, mode):
                log("Invalid TikTok URL. Please try again.", Fore.RED)
                return
                
            # Clear screen and display banner
            clear_screen()
            print(f"\n{Fore.CYAN}┌{'─' * 50}┐")
            print(f"│{Fore.WHITE} TikTok {mode} Bot - Running {Fore.CYAN}│")
            print(f"└{'─' * 50}┘{Style.RESET_ALL}")
            print(f"{Fore.WHITE}URL: {url}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}Mode: {self.modes[mode]['icon']} {mode}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'─' * 52}{Style.RESET_ALL}")
            
            log("Starting bot...", Fore.GREEN)
            log("Press Ctrl+C to stop the bot at any time", Fore.YELLOW)
            
            # Main loop
            cycle_count = 0
            while self.running:
                cycle_count += 1
                log(f"Cycle #{cycle_count}", Fore.CYAN)
                
                result = self.send_engagement(mode, url)
                
                if not result:
                    log("Error occurred. Waiting 5 seconds before retry...", Fore.RED)
                    time.sleep(5)
                    
                    # Check if we need to re-solve CAPTCHA
                    if "captcha" in self.driver.page_source.lower() or "session expired" in self.driver.page_source.lower():
                        log("Session expired or CAPTCHA required. Reauthorizing...", Fore.YELLOW)
                        if not self.solve_captcha():
                            log("Failed to solve CAPTCHA. Stopping bot.", Fore.RED)
                            break
                
                # Random wait between cycles
                wait_time = random.randint(10, 20)
                log(f"Waiting {wait_time} seconds before next request...", Fore.YELLOW)
                self.countdown(wait_time)
                
        except KeyboardInterrupt:
            log("Bot stopped by user", Fore.YELLOW)
        except Exception as e:
            log(f"Error in bot process: {e}", Fore.RED)
        finally:
            self.running = False

    def settings_menu(self):
        """Display and manage settings."""
        while True:
            clear_screen()
            print(f"\n{Fore.CYAN}┌{'─' * 45}┐")
            print(f"│{Fore.WHITE} SETTINGS MENU {Fore.CYAN}│")
            print(f"└{'─' * 45}┘{Style.RESET_ALL}")
            
            print(f" {Fore.WHITE}1. Proxy: {Fore.YELLOW}{self.proxy if self.proxy else 'None'}")
            print(f" {Fore.WHITE}2. User Agent: {Fore.YELLOW}{self.user_agent[:30]}..." if self.user_agent and len(self.user_agent) > 30 else f" {Fore.WHITE}2. User Agent: {Fore.YELLOW}{self.user_agent if self.user_agent else 'Default'}")
            print(f" {Fore.WHITE}3. Rate Limits")
            print(f" {Fore.WHITE}4. Reset to Default")
            print(f" {Fore.WHITE}5. Back to Main Menu")
            
            choice = get_input("Choose an option")
            
            if choice == "1":
                # Proxy settings
                new_proxy = get_input("Enter proxy (format: ip:port or username:password@ip:port) or 'none' to clear")
                if new_proxy.lower() == 'none':
                    self.proxy = None
                    log("Proxy cleared", Fore.GREEN)
                else:
                    self.proxy = new_proxy
                    log(f"Proxy set to: {new_proxy}", Fore.GREEN)
                    
            elif choice == "2":
                # User agent settings
                print(f"\n{Fore.CYAN}┌{'─' * 45}┐")
                print(f"│{Fore.WHITE} USER AGENT OPTIONS {Fore.CYAN}│")
                print(f"└{'─' * 45}┘{Style.RESET_ALL}")
                print(f" {Fore.WHITE}1. Default Desktop Chrome")
                print(f" {Fore.WHITE}2. Default Mobile Chrome")
                print(f" {Fore.WHITE}3. Custom User Agent")
                
                ua_choice = get_input("Choose an option")
                
                if ua_choice == "1":
                    self.user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
                    log("Set to default desktop Chrome user agent", Fore.GREEN)
                elif ua_choice == "2":
                    self.user_agent = ("Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 "
                                      "(KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36")
                    log("Set to default mobile Chrome user agent", Fore.GREEN)
                elif ua_choice == "3":
                    custom_ua = get_input("Enter custom user agent")
                    if custom_ua:
                        self.user_agent = custom_ua
                        log("Custom user agent set", Fore.GREEN)
                
            elif choice == "3":
                # Rate limit settings
                clear_screen()
                print(f"\n{Fore.CYAN}┌{'─' * 45}┐")
                print(f"│{Fore.WHITE} RATE LIMITS SETTINGS {Fore.CYAN}│")
                print(f"└{'─' * 45}┘{Style.RESET_ALL}")
                
                for i, (mode, limits) in enumerate(self.rate_limits.items(), 1):
                    print(f" {Fore.WHITE}{i}. {mode}: {Fore.YELLOW}Min: {limits['min']}, Max: {limits['max']}")
                
                print(f" {Fore.WHITE}6. Back to Settings")
                
                rate_choice = get_input("Choose a mode to modify")
                
                if rate_choice in ["1", "2", "3", "4", "5"]:
                    modes = list(self.rate_limits.keys())
                    selected_mode = modes[int(rate_choice) - 1]
                    
                    min_val = get_input(f"Enter minimum {selected_mode} per request")
                    max_val = get_input(f"Enter maximum {selected_mode} per request")
                    
                    try:
                        min_val = int(min_val)
                        max_val = int(max_val)
                        
                        if min_val > max_val:
                            min_val, max_val = max_val, min_val
                            
                        self.rate_limits[selected_mode]["min"] = min_val
                        self.rate_limits[selected_mode]["max"] = max_val
                        log(f"{selected_mode} rate limits updated", Fore.GREEN)
                    except ValueError:
                        log("Invalid input. Please enter numbers only.", Fore.RED)
                        time.sleep(2)
                        
            elif choice == "4":
                # Reset settings
                confirm = get_input("Reset all settings to default? (y/n)")
                if confirm.lower() == 'y':
                    default_settings = {
                        "proxy": None,
                        "user_agent": None,
                        "auto_captcha": False,
                        "rate_limits": {
                            "Hearts": {"min": 11, "max": 20},
                            "Views": {"min": 450, "max": 550},
                            "Shares": {"min": 70, "max": 85},
                            "Favorites": {"min": 3, "max": 8},
                            "Followers": {"min": 3, "max": 8}
                        }
                    }
                    
                    self.proxy = default_settings["proxy"]
                    self.user_agent = default_settings["user_agent"]
                    self.auto_captcha = default_settings["auto_captcha"]
                    self.rate_limits = default_settings["rate_limits"]
                    log("Settings reset to default", Fore.GREEN)
                    time.sleep(2)
                    
            elif choice == "5":
                # Save settings before exiting
                settings = {
                    "proxy": self.proxy,
                    "user_agent": self.user_agent,
                    "auto_captcha": self.auto_captcha,
                    "rate_limits": self.rate_limits
                }
                save_settings(settings)
                return
                
            # Save settings after each change
            settings = {
                "proxy": self.proxy,
                "user_agent": self.user_agent,
                "auto_captcha": self.auto_captcha,
                "rate_limits": self.rate_limits
            }
            save_settings(settings)

    def stop(self):
        """Clean up and stop the bot."""
        self.running = False
        if self.driver:
            try:
                self.driver.quit()
            except:
                pass


def main():
    """Main application function."""
    # Initialize colorama
    init(autoreset=True)
    
    clear_screen()
    
    # ASCII art banner
    banner = f"""{Fore.CYAN}
  _______ _ _  _____ _       _    ______       _   
 |__   __(_) |/ ____| |     | |  |  ____|     | |  
    | |   _| | |    | |_ ___| | _| |__   _ __ | |_ 
    | |  | | | |    | __/ _ \ |/ /  __| | '_ \| __|
    | |  | | | |____| ||  __/   <| |____| | | | |_ 
    |_|  |_|_|\_____|\__\___|_|\_\______|_| |_|\__|
    {Style.RESET_ALL}"""
    
    print(banner)
    print(f"{Fore.CYAN}{'─' * 52}")
    print(f"{Fore.WHITE}      TikTok Zefoy Bot {Fore.YELLOW}v5.0")
    print(f"{Fore.CYAN}{'─' * 52}{Style.RESET_ALL}")
    
    # Initialize bot
    bot = TikTokBot()
    
    # Main application loop
    while True:
        # Setup browser if not initialized
        if not bot.driver:
            if not bot.setup():
                log("Failed to initialize. Please check your internet connection and try again.", Fore.RED)
                input(f"{Fore.WHITE}Press Enter to exit...{Style.RESET_ALL}")
                sys.exit(1)
        
        # Get service status and show menu
        options = bot.check_status()
        choice = print_menu(options)
        
        try:
            # Handle numeric choices
            if choice.isdigit():
                choice_num = int(choice)
                
                if 1 <= choice_num <= len(options) - 2:  # Service options
                    mode = options[choice_num - 1][0]
                    status = options[choice_num - 1][1]
                    
                    if status == "Active":
                        bot.start(mode)
                    else:
                        log(f"{mode} service is currently unavailable.", Fore.RED)
                        time.sleep(2)
                        
                elif choice_num == len(options) - 1:  # Settings
                    bot.settings_menu()
                    
                elif choice_num == len(options):  # Exit
                    log("Exiting...", Fore.YELLOW)
                    bot.stop()
                    sys.exit(0)
            
            # Handle text choices
            elif choice.lower() in ["exit", "quit", "q"]:
                log("Exiting...", Fore.YELLOW)
                bot.stop()
                sys.exit(0)
                
        except Exception as e:
            log(f"Error: {e}", Fore.RED)
            time.sleep(2)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Program interrupted by user. Exiting...{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}Unexpected error: {e}{Style.RESET_ALL}")
        input("Press Enter to exit...")     

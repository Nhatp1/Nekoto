import subprocess
import sys
import os

os.system("cls" if os.name == "nt" else "clear")


def a1():
    return True

def b2():
    return "áº¨n!"

def c3(pkg):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

p1 = ['hashlib']
for p in p1:
    try:
        __import__(p)
    except ImportError:
        c3(p)

def d4(s):
    x = int(s, 16)
    y = x % 100
    z = 100 - y
    return y, z

def e5(md5_input):
    if len(md5_input) != 32:
        return False
    return all(c in '0123456789abcdef' for c in md5_input.lower())

def f6():
    while True:
        inp = input("@NP-TOOL vui lòng nhập mã MD5 : ")
        if inp.lower() == "thoat":
            print("ChÆ°Æ¡ng trÃ¬nh káº¿t thÃºc.")
            break
        if not e5(inp):
            print("Ä‘Ã©o pháº£i mÃ£ MD5 !!!")
            continue
        t, x = d4(inp)
        output = f" káº¿t quáº£ TÃ€IðŸ”´ðŸŽ²ðŸŽ² : {t:.2f}%\n káº¿t quáº£ Xá»ˆUðŸŸ¢ðŸŽ²ðŸŽ²: {x:.2f}%"
        print(output)
        print("-" * 30)

def g7():
    a1()
    b2()
    f6()

if __name__ == "__main__":
    g7()

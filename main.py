from requests import get as rget
from lxml import etree
from random import uniform as rand_s
from time import sleep
from os import mkdir
import re

HEADERS   = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Firefox/94.0"}
PROXY     = {"http": "http://127.0.0.1:1080", "https": "http://127.0.0.1:1080"}
MATCH_URL = ["/html/body/div/div/div/a/@href", "/html/body/div/div/a/img/@src"]
IMG_URL   = r"^\w+://[a-z]{7}.[a-z]{12}.hath.[\w\:\d]{7,13}\/\w\/[a-z0-9]+\-\d+\-\d+\-\d+\-[a-z]{3,5}/\w{8}\=\d+\-[a-z0-9]+\;\w{9}\=\d+\;\w{4}\=[a-z0-9A-Z]+\/[a-z0-9A-Z\-\_]+([a-z0-9A-Z.]+)"

BLUE = "\x1b[96m"
RED  = "\x1b[91m"
RSET = "\x1b[0m"
YOLW = "\x1b[93m"

def get(url, total, R18G :bool = None):
    if R18G:
        global HEADERS
        HEADERS['Cookie'] = 'nw=1'
    
    try:
        dirname = etree.HTML(rget(url, headers=HEADERS, proxies=PROXY).text).xpath("/html/head/title/text()")[0]
        mkdir(dirname)
        print(f"{RED}[!]{RSET} 文件夹不存在，正在创建...")
        print(f"{YOLW}[!]{RSET} 创建成功.")
    except FileExistsError:
        print(f"{RED}[-]{RSET} 文件夹已存在，将在此已存在的文件夹中写入数据.")
    
    index = 1
    for x in range(total):
        res = rget(url + f"?p={x}", headers = HEADERS, proxies=PROXY).text
        res = etree.HTML(res).xpath(MATCH_URL[0])
        print(f"{BLUE}[+]{RSET} 获取第{x+1}页图片总数成功...")
        for y in range(len(res)):
            img = rget(res[y], headers = HEADERS, proxies=PROXY).text
            print(f"{BLUE}[+]{RSET} 获取第{x+1}页第{y+1}图片成功...")
            img_url = etree.HTML(img).xpath(MATCH_URL[1])[0]
            imgData = rget(img_url, headers = HEADERS, proxies = PROXY).content
            print(f"{BLUE}[+]{RSET} {img_url[:20]}..{img_url[-20:]}, 数据已获取.")
            suffixName = re.findall(IMG_URL, img_url, re.S)[0]
            fileName = "0"*(8 - len(str(index))) + str(index) + suffixName
            print(f"{BLUE}[+]{RSET} 正在保存第{x+1}页第{y+1}图片...")
            with open(dirname + "/" + fileName, "wb") as f:
                f.write(imgData)
                print(f"{YOLW}[+]{RSET} 第{x+1}页第{y+1}图片保存成功. 文件名: '{fileName}'.\n")
            index += 1
            sleep(rand_s(0.1, 0.3))
    return "Done."

def main():
    url = "https://e-hentai.org/g/2182217/c8c5a5acb7/"
    get(url, 4, True)

if __name__ == "__main__":
    main()









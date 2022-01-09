from requests import get as rget
from os import mkdir, getcwd, rmdir
from os.path import exists
from binascii import a2b_hex as a2b
from time import sleep
from lxml import etree
from random import uniform as rand_s
import sys
import re

from requests.exceptions import ProxyError, SSLError
from urllib3.exceptions import MaxRetryError
from ssl import SSLEOFError

class dw_img:
    def __init__(self, url: str, folderNAME: str = None, total_page: int = None):
        self.url = url
        self.folderNAME = folderNAME
        self.total_page = total_page
        # 预设一些变量
        self.HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537 (KHTML, like Gecko) Firefox/94.0"}
        self.PROXY = {"http": "http://127.0.0.1:1080", "https": "http://127.0.0.1:1080"}
        self.MATCH_URL = ["/html/body/div/div/div/a/@href", "/html/body/div/div/a/img/@src"]
        self.IMGURLCHECK = r"^\w+://[a-z]{7}.[a-z]{12}.hath.[\w\:\d]{7,13}\/\w\/[a-z0-9]+\-\d+\-\d+\-\d+\-[a-z]{3,5}/\w{8}\=\d+\-[a-z0-9]+\;\w{9}\=\d+\;\w{4}\=[a-z0-9A-Z]+\/([a-z0-9A-Z\-\_\.]+)"

    @property
    def download(self):
        dirname = self.folderNAME+"/"
        try:
            mkdir(dirname)
        except FileExistsError:
            print("文件夹已存在，将在此已存在的文件夹中写入数据.")
        
        USERURL=self.url
        # 新建一个列表，以储存接下来要保存的内容
        url_list = []
        number = 1
        try:
            if self.total_page == None:
                # 进行代码清洗，将需要的内容筛选出来。
                res = etree.HTML(rget(USERURL, headers=self.HEADERS, proxies=self.PROXY).text).xpath(self.MATCH_URL[0])
                res_len = len(res)

                for x in range(res_len):
                    url_list.append(etree.HTML(rget(res[x], headers=self.HEADERS, proxies=self.PROXY).text).xpath(self.MATCH_URL[1])[0])
                    
                    # 图片链接有效性检查
                    re.findall(self.IMGURLCHECK, url_list[x], re.S)[0]
                    print("已提取第{0}张图片的链接: {1}".format(number, url_list[number-1]))
                    
                    # 将图片的数据保存至用户指定的目录内
                    imgdata = rget(url_list[number-1], headers=self.HEADERS, proxies=self.PROXY).content
                    resFileNAME = "".join(re.findall(self.IMGURLCHECK, url_list[number-1], re.S)[0])
                    with open(dirname+resFileNAME, "wb") as f:
                        f.write(imgdata)
                        print("已写入这张图片，文件名为: {1}\n".format(number, resFileNAME))
                        
                    sleep(rand_s(0.1, 0.6))
                    number += 1
            elif type(self.total_page) == int:
                for page in range(self.total_page):
                    # 进行代码清洗，将需要的内容筛选出来。
                    res = etree.HTML(rget(USERURL+"?p={}".format(page), headers=self.HEADERS, proxies=self.PROXY).text).xpath(self.MATCH_URL[0])
                    res_len = len(res)

                    for x in range(res_len):
                        url_list.append(etree.HTML(rget(res[x], headers=self.HEADERS, proxies=self.PROXY).text).xpath(self.MATCH_URL[1])[0])
                        
                        # 图片链接有效性检查
                        re.findall(self.IMGURLCHECK, url_list[x], re.S)[0]
                        print("已提取第{0}张图片的链接: {1}".format(number, url_list[number-1]))
                        
                        # 将图片的数据保存至用户指定的目录内
                        imgdata = rget(url_list[number-1], headers=self.HEADERS, proxies=self.PROXY).content
                        resFileNAME = "".join(re.findall(self.IMGURLCHECK, url_list[number-1], re.S)[0])
                        with open(dirname+resFileNAME, "wb") as f:
                            f.write(imgdata)
                            print("已写入这张图片，文件名为: {1}\n".format(number, resFileNAME))
                        
                        sleep(rand_s(0.1, 0.6))
                        number += 1
            else:
                exit("请添加正确的总页数值，当前总页数的变量类型为{}\n如已指定页码，请勿添加total_page!!!".format(self.total_page))
        except (IndexError, ProxyError, MaxRetryError, ConnectionResetError, SSLEOFError, SSLError):
            print(url_list[x])
            sys.exit("出现了意外的错误，请检查以下的情况，排除之后如果还存在错误，请与我联络。\n1. 网络是否连接正常。\n2. IP状态是否正常\n3. 下载配额是否正常\n4. URL是否正常")
        return "Done."
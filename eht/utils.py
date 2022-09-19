from requests import get as rget
from os.path  import exists
from os       import mkdir
from lxml     import etree
import re

ProxyIPAddress = 'http://127.0.0.1:1080'
UserAgent = 'Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'
ProxyInfo = {"http": ProxyIPAddress, "https": ProxyIPAddress}

match_xpath_title   = '/html/head/title/text()'            # 匹配网页标题
match_xpath_show    = '/html/body/div/div/div/a/@href'     # 匹配单页所有图片的查看链接
match_xpath_picture = '/html/body/div/div/a/img/@src'      # 通过查看链接获取页面中的图片
match_xpath_page    = '/html/body/div/table/tr/td/a/@href' # 匹配总页数

def xpath(data :str, xpath_text :str):
    HTML = etree.HTML(data)
    HTML = HTML.xpath(xpath_text)
    return HTML

def fwrite(fn :str, fd :bytes):
    with open(fn, 'wb') as f: f.write(fd)

def checkDirectory(DirectoryName :str):
    if not exists(DirectoryName):
        mkdir(DirectoryName)

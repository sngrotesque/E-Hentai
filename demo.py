'''
使用方法:
    snt.dw_img(url: str, folderNAME: str = None, total_page: int = None).download

    url (字符串类型变量):                   作品的链接地址
    folderNAME (字符串类型变量):            用于存放图片的目录名
    total_page (整型变量):                 作品的总页数

如果你已经在url内指定页码，那么请勿添加total_page变量的值
url指定页码如: 
    https://e-hentai.org/g/1111111111/11111111/?p=0
    https://e-hentai.org/g/1111111111/11111111?p=0
    
    指定页码为作品第一页的所有图片(也就是不添加p值)
    https://e-hentai.org/g/1111111111/11111111

如果你要让程序下载所有页面的图片，请添加total_page的值，值为真实页码数(不用-1)

目前类方法里有一个，是:
    download           将作品页面内的所有图片的超链接清洗出来，将已清洗出来的图片超链接全部下载至用户指定的目录内
'''
import snt

url="https://e-hentai.org/g/1111111111/11111111"
foldername="TEST"

res = snt.dw_img(url, folderNAME=foldername, total_page=1).download

print(res)

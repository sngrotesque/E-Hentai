from .utils import *

class ehentai:
    def __init__(self, url :str, directoryName :str, r18g :bool = False, proxyinfo :dict = None):
        self.DEFINED_URL           = url
        self.DEFINED_directoryName = directoryName
        self.DEFINED_Proxy         = proxyinfo
        self.DEFINED_Headers       = {'User-Agent': UserAgent}
        if r18g: self.DEFINED_Headers['Cookie'] = 'nw=1'
        
        self.RESULTS_PageCount   = 0
        self.RESULTS_artworkList = []

    @property
    def getTotalPages(self):
        HtmlData = rget(self.DEFINED_URL,
        headers = self.DEFINED_Headers, proxies = self.DEFINED_Proxy).text
        PageNumber = set(xpath(HtmlData, match_xpath_page))
        self.RESULTS_PageCount = len(PageNumber)
        print(f'>>>> 总页数: {self.RESULTS_PageCount}')

    @property
    def getTotalArtworkList(self):
        self.getTotalPages
        serialNumber = 1
        for page in range(self.RESULTS_PageCount):
            HtmlData = rget(f'{self.DEFINED_URL}?p={page}',
                headers = self.DEFINED_Headers, proxies = self.DEFINED_Proxy).text
            tempArtworksList = xpath(HtmlData, match_xpath_show)
            for artworkUrl in tempArtworksList:
                print(f'\r>>>> 已获取第{serialNumber:0>5}张图片的页面链接.', end='')
                self.RESULTS_artworkList.append(artworkUrl)
                serialNumber += 1
        print('\n', end='')

    @property
    def download(self):
        self.getTotalArtworkList
        checkDirectory(self.DEFINED_directoryName)
        serialNumber = 1
        for artworkUrl in self.RESULTS_artworkList:
            saveFilePath = f'{self.DEFINED_directoryName}/{serialNumber:0>8}.jpg'
            if exists(saveFilePath):
                print(f'\r>>>> {serialNumber:>8}已存在，跳过...', end='')
            HtmlData = rget(artworkUrl, headers = self.DEFINED_Headers, proxies = self.DEFINED_Proxy).text
            PictureLink = xpath(HtmlData, match_xpath_picture)[0]
            PictureData = rget(PictureLink, headers = self.DEFINED_Headers, proxies = self.DEFINED_Proxy).content
            print(f'\r>>>> 已下载第{serialNumber:>8}张图片.', end='')
            fwrite(saveFilePath, PictureData)
            serialNumber += 1
        print('\n', end='')



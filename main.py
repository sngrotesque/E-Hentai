from eht.utils import ProxyInfo
import eht

url = 'https://e-hentai.org/g/123456abc/123456abc/'
directoryName = '123'
r18g = 1

e = eht.ehentai(url, directoryName, r18g = r18g, proxyinfo = ProxyInfo)
e.download

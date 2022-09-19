from eht.utils import ProxyInfo
import eht

url = 'https://e-hentai.org/g/123456abc/123456abc/'
r18g = 1

e = eht.ehentai(url, r18g = r18g, proxyinfo = ProxyInfo)
e.download

from eht.utils import ProxyInfo
import json
import eht

with open('000_ArtworkList.json', 'r', encoding='utf-8') as f:
    Artworks = json.loads(f.read())

for x in Artworks:
    url = Artworks[x]['artworkUrl']
    dn  = Artworks[x]['artworkName']
    print(url, dn)

# url = 'https://e-hentai.org/g/123456abc/123456abc/'
# directoryName = '123'
# r18g = 1

# e = eht.ehentai(url, directoryName, r18g = r18g, proxyinfo = ProxyInfo)
# e.download

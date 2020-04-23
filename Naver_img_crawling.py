from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('Please write a Keyword : ')
url = baseUrl + quote_plus(plusUrl)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.findAll(class_='_img')


n = 1
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        # you must create folder as a 'img'
        with open('./img/' + plusUrl + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    print(imgUrl)

print('Download Complete')


# orign video
# https://www.youtube.com/watch?v=_wRTyQYjHcg&t=327s

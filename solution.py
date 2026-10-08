import urllib.request
from bs4 import BeautifulSoup
url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
total = 0
count = 0
for tag in tags:
    total = total + int(tag.contents[0])
    count = count + 1
    pass

print('Count', count)
print('Sum', total)


lol
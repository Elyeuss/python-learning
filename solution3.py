import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print('Retrieving', url)
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
counts = tree.findall('.//count')
print('Count:', len(counts))

total = 0
for item in counts:
    total = total + int(item.text)

print('Sum:', total)
import urllib.request
import json

url = input('Enter location: ')
print('Retrieving', url)

data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
comments = info['comments']
print('Count:', len(comments))

total = 0
for item in comments:
    total += item['count']

print('Sum:', total)
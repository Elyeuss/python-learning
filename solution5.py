import urllib.request, urllib.parse
import json

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'
address = input('Enter Location: ')
params = {'q': address, 'key': 42}
url = serviceurl + urllib.parse.urlencode(params)

print('Retrieving', url)
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)

plus_code = info['features'][0]['properties']['plus_code']
print('Plus code', plus_code)
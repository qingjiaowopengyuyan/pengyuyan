import urllib.request
import urllib.parse
data = bytes(urllib.parse.urlencode({'pw':'lq1425715080','acc':'1425715080'}),enconding='utf8')
url = 'http://httpbin.org/post'
response = urllib.request.urlopen(url,data=data)
result = response.read().decode('utf8')
print(result)
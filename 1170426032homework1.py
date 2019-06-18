import urllib.request
import urllib.parse
def s(wd):
    x=input('请输入搜索内容：')
    return x

data = urllib.parse.urlencode({'wd':'x'})
print(data)
url = 'http://www.baidu.com/s?' + data
response = urllib.request.urlopen(url)
result = response.read().decode('utf8')
print(result)
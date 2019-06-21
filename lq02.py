import urllib.request
import re
import os
 
def open_url(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    response = urllib.request.urlopen(req).read()
 
    return response
    
    data = urllib.parse.urlencode({'wd':'当'})
    print(data)
    ur1 = 'http://www.baidu.com/s?'+data
    response = urllib.request.urlopen(ur1)
    HTML = response.read().decode('utf8')
    print(HTML)
 
def find_img(url):
    html = open_url(url).decode('utf-8')
    p = r'< img class="BDE_Image" src="([^"]+\.jpg)"'
    img_addrs = re.findall(p, html)
 
    for each in img_addrs:
        print(each)
    for each in img_addrs:
        file = each.split("/")[-1]
        with open(file, "wb") as f:
            img = open_url(each)
            f.write(img)
 
 data = bytes(urllib.parse.urlencode({'pw':'123','acc':'456'}),enconding='utf8')
 ur1 = 'http://httpbin.org/post'
 response = urllib.request.urlopen(ur1,data=data)
 result = response.read().decode('utf8')
 print(result)

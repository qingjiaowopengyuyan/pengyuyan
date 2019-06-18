import requests
# 请求百度，需要注意：一定要带上http或https
response = requests.get('http://www.baidu.com')
print(response)
# 看它拿到了什么东西
print(response.headers)
# 模拟伪造一个浏览器
headers = {User-agent}
response = requests.get('http://www.baidu.com',headrs=headers)
print(response.text)
print(reponse.headers)

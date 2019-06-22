import requests
def TuPian(path):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
    response = requests.get(url)
    res = response.text 
    chai = res.split('\n')
    for url in chai:
        try:
            tupian = requests.get(url=url,headers=headers)
        except Exception as e:
            print(e)
        else:
            tupian = requests.get(url=url,headers=headers)
            name = chai.split('/')[-1]
            with open(path+name,'wb') as f:
                f.write(tupian.content)


if __name__ == "__main__":
    path = 'C:/Users/Administrator'
    TuPian(path=path)
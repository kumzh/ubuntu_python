import urllib.request
import urllib.error
import requests

if __name__ == "__main__":

    '''爬虫浏览器伪装'''
    heard = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'}
    try:
        url = 'https://www.bilibili.com/video/av22571713/?p=19'
        # req = requests.get(url,headers=heard)
        req = urllib.request.Request(url,headers=heard)
        print('爬取完成！')
        print(req)
    except urllib.error.HTTPError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)

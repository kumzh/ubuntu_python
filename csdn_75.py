import requests
import re
from sys import argv
import urllib.request
from urllib.error import URLError,HTTPError


def open_web(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    response = requests.request('get',url,headers=header)
    code = response.status_code
    print('statu:',code)
    if code == 200:
        print(response.json)
        return response
    else:
        print(response.raise_for_status())
        exit(1)

def urllib_open_web(url):
    try:
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        response = urllib.request.Request(url,headers=header)    #构造请求
        data = urllib.request.urlopen(response).read().decode('utf-8')
        return data
    except HTTPError as e:
        if hasattr(e,'code'):
            print('code',e)
        if hasattr(e,'reason'):
            print('reason',e)
    
def regex_info(data):
    # regex = '<a href="(https://blog.csdn.net/(.*?)/article/details/[0-9]*)" (.*?)>(.*?)</a>'
    regex = 'href="(https://blog.csdn.net/.*?/article/details/[0-9]*)"'
    string = re.compile(regex).findall(data)
    new_string = []
    for i in string:
        if i not in new_string:
            new_string.append(i)
    return new_string

def download_web(url_list):
    num = 0
    for url in url_list:
        file_name = str(num)+'.html'
        urllib.request.urlretrieve(url,filename=file_name)
        print('=====爬取%s次====='%str(num+1))
        num += 1





if __name__ == "__main__":
    if len(argv) == 1:
        print("请输入参数！")
        exit(1)
    else:
        url = argv[1]
        # open_web(url)
        data = urllib_open_web(url)
        url_list = regex_info(data)
        download_web(url_list)




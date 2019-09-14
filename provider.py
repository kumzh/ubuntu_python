#获取豆瓣网站出版社名称
import urllib.request
import re
from sys import argv
def get_data(url='https://read.douban.com/provider/all'):
    data = urllib.request.urlopen(url).read()
    string = str(data.decode('utf-8'))
    return string

def regex1(string,pat='<div class="name">(.*?)</div>'):
    result = re.compile(pat).findall(string)
    return result

if __name__ == "__main__":
    print('××默认获取豆瓣网址出版社名称××\n也可以追加参数，网址和正则表达式')
    if len(argv) == 1:
        string = get_data()
        result = regex1(string)
    else:
        string = get_data(argv[1])
        result = regex1(string,argv[2])
    for i in result:
        print(i)
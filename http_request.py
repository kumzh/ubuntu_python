import urllib.request
import urllib.parse

def request_get():
    wd = input('搜索内容：')
    # wd1 = urllib.request.quote(wb)   中文编码
    url = 'http://www.baidu.com/s?wd='+wd
    # req = urllib.request.Request(url)
    data = urllib.request.urlopen(url).read()
    da = data.decode('utf-8')
    print(da)
    return da

def request_post():
    #提交的地址
    url = 'file:///home/kun/ubuntu_python/login.html'
    #提交的数据
    data = urllib.parse.urlencode({
        'username':'zzzzz',
        'passwd':'qwqwq',    #设置表单中填写的信息
    }).encode('utf-8')
    #模拟http请求
    req = urllib.request.Request(url,data)
    #读取请求后的网页
    da = urllib.request.urlopen(req).read().decode('utf-8')
    # req.add_header 伪装浏览器
    return da
if __name__ == "__main__":
    req = request_post()
    print(req)
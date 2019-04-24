import urllib.parse
import http.cookiejar
import gzip
import socket

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
           # "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
value = {"log": "liangsoso",
         "pwd": "liangsoso",
         "wp-submit": "登陆",
         "redirect_to": "http://liangsoso.com/wp-admin/",
         "testcookie": "1"}
url="http://liangsoso.com/wp-login.php"
timeout = 2
socket.setdefaulttimeout(timeout)

try:
    data = urllib.parse.urlencode(query=value).encode("utf8")
    request = urllib.request.Request(url=url, data=data, headers=headers)
    cookiejar = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookiejar=cookiejar)
    opener = urllib.request.build_opener(handler)
    # 获取cookie
    opener.open(fullurl=url, data=data)
    response = opener.open(request).read().decode("utf-8")
    # headers中带有"Accept-Encoding": "gzip, deflate"时，需要先对响应解压处理
    # response = gzip.decompress(response).decode("utf-8")
    print(response)
except urllib.error.HTTPError as e:
    if hasattr(e, "reason"):
        print("HTTPError reason:" + str(e.reason))
    if hasattr(e, "code"):
        print("HTTPError code:" + str(e.code))
except urllib.error.URLError as e:
    if hasattr(e, "reason"):
        print("URLError reason:" + str(e.reason))
    if hasattr(e, "code"):
        print("URLError code:" + str(e.code))
except socket.timeout:
    print("socket time out!")
else:
    print()


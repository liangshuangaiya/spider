import urllib.request
import urllib.error
import urllib.parse
import http.cookiejar
import gzip


headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
           "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
value = {"log": "liangsoso",
         "pwd": "liangsoso",
         "wp-submit": "登陆",
         "redirect_to": "http://liangsoso.com/wp-admin/",
         "testcookie": "1"}
url="http://liangsoso.com/wp-login.php"

try:
    data = urllib.parse.urlencode(query=value).encode("utf8")
    request = urllib.request.Request(url=url, data=data, headers=headers)
    response = urllib.request.urlopen(request)
    response = response.read()
    ret = gzip.decompress(response)
    result = ret.decode("utf-8")
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
else:
    print()

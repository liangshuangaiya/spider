import urllib.request
import urllib.error

url = "http://liangsoso.com"
response = urllib.request.urlopen(url)
result = response.read().decode("utf-8")
url = response.geturl()
info = response.info()
code = response.getcode()

headers = {"User_Agent": ""}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
code = response.getcode()

try:
    response = urllib.request.urlopen("http://google.com")
    result = response.read().decode("utf-8")
except urllib.error.HTTPError as e:
    if hasattr(e, "reason"):
        print("HTTPError:" + str(e.reason))
except urllib.error.URLError as e:
    if hasattr(e, "reason"):
        print("URLError:" + str(e.reason))
    else:
        print(e)
else:
    print("请求成功！")
print(code)

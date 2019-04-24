# -*- coding: utf-8 -*-
import urllib.request
import urllib.error
import urllib.parse
import http.cookiejar

import sys
from imp import reload

reload(sys)

cookies = "ngaPassportUid=guest05cb343a4f4008; taihe=e75b019a0a164ce02fa7f322c67a5b9c; Hm_lvt_5adc78329e14807f050ce131992ae69b=1555168413,1555252054; Hm_lpvt_5adc78329e14807f050ce131992ae69b=1555255481; lastvisit=1555256175; guestJs=1555256175; UM_distinctid=16a1c403d2e501-0fae4e11315564-784a5935-158100-16a1c403d2f1a9; CNZZDATA30043604=cnzz_eid%3D1179685297-1555249284-%26ntime%3D1555254684; CNZZDATA30039253=cnzz_eid%3D209741003-1555248811-%26ntime%3D1555255574; bbsmisccookies=%7B%22uisetting%22%3A%7B0%3A%22a%22%2C1%3A1555255780%7D%2C%22insad_refreshid%22%3A%7B0%3A%22/WsVWjNWf5dgI1WS2rFTus2g9CqDDOmotPZmB72as%22%2C1%3A1555856936%7D%2C%22pv_count_for_insad%22%3A%7B0%3A-44%2C1%3A1555261312%7D%2C%22insad_views%22%3A%7B0%3A1%2C1%3A1555261312%7D%7D; CNZZDATA1256638820=1760039222-1555251335-http%253A%252F%252Fbbs.nga.cn%252F%7C1555251335"

headers = {"Accept": "text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8",
           "Host": "bbs.nga.cn",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
           "Referer": "http: // bbs.nga.cn / thread.php?fid = -7 & page = 2 & rand = 677",
           "Upgrade": "Insecure - Requests: 1",
           "Cookie": cookies}

url = "http://bbs.nga.cn/thread.php?fid=-7&page=2&rand=533"


try:
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    response = response.read().decode("GBK")
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
else:
    print("爬取结束！")

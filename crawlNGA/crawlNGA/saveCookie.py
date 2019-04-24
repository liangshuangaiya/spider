from urllib import request
from http import cookiejar

# 从请求头中的Cookie字段获取
cookies = "UM_distinctid=166bf140cea486-0c4685494fe79d-594c2a16-306000-166bf140cebb23; taihe=bb95bf834fe8b9cb417a4f76e57d71ed; ngacn0comUserInfo=%25CF%25CF%25BA%25C5%25CA%25AE%25C1%25F9%09%25E8%2588%25B7%25E5%258F%25B7%25E5%258D%2581%25E5%2585%25AD%0942%0942%09%09-30%0927300%094%090%090%0953_-600%2C61_143; CNZZDATA1256638924=1352051463-1549029003-https%253A%252F%252Fbbs.nga.cn%252F%7C1549029003; CNZZDATA1256638919=1329572441-1540816093-http%253A%252F%252Fbbs.nga.cn%252F%7C1552819746; CNZZDATA1256638828=1805424189-1542356914-http%253A%252F%252Fbbs.nga.cn%252F%7C1553177984; ngaPassportUid=35345195; ngaPassportUrlencodedUname=%25CF%25CF%25BA%25C5%25CA%25AE%25C1%25F9; ngaPassportCid=Z8lud5kqrun2ep630ll258m50io2m3f6qupt307r; CNZZDATA1256638851=887532552-1540798715-http%253A%252F%252Fbbs.nga.cn%252F%7C1554551353; ngacn0comUserInfoCheck=5a2859abaa8b7e6e1930e9fcceb45d77; ngacn0comInfoCheckTime=1555250151; bbsmisccookies=%7B%22uisetting%22%3A%7B0%3A2097152%2C1%3A1563017091%7D%2C%22insad_refreshid%22%3A%7B0%3A%22/WsVWjNWf5dgI1WS2rFTus2g9CqDDOmotPZmB72as%22%2C1%3A1555804933%7D%7D; CNZZDATA30043604=cnzz_eid%3D103186534-1540800948-http%253A%252F%252Fbbs.nga.cn%252F%26ntime%3D1555335684; CNZZDATA30039253=cnzz_eid%3D1180855752-1540798994-http%253A%252F%252Fbbs.nga.cn%252F%26ntime%3D1555336574; Hm_lvt_5adc78329e14807f050ce131992ae69b=1555168578,1555241087,1555250152,1555338235; taihe_session=38d7b7769cf0f427eacc90c39d7a2640; CNZZDATA1256638820=2027800863-1540799010-http%253A%252F%252Fbbs.nga.cn%252F%7C1555334549; lastvisit=1555339388; lastpath=/read.php?tid=16962421&_ff=-7&page=2; Hm_lpvt_5adc78329e14807f050ce131992ae69b=1555339395"

headers2 = [("Accept", "text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8"),
           ("Host", "bbs.nga.cn"),
           ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763"),
           ("Referer", "http://bbs.nga.cn/thread.php?fid=-7&page=2&rand=136"),
           ("Upgrade", "Insecure - Requests: 1"),
           ("Cookie", cookies)]

filename = 'cookie.txt'
cookie = cookiejar.MozillaCookieJar(filename)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
opener.addheaders = headers2
response = opener.open("http://bbs.nga.cn/thread.php?fid=-7&page=2&rand=136")
cookie.save(ignore_discard=True, ignore_expires=True)
print(cookiejar)
for item in cookie:
    print("Name:%s" % item.name)
    print("Value:%s" % item.value)
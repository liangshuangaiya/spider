import http.cookiejar
import urllib.request
from urllib.error import HTTPError

url = "http://bbs.nga.cn/thread.php?fid=-7"

headers = [("Accept", "text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8"),
           ("Host", "bbs.nga.cn"),
           ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763"),
           ("Referer", "http://bbs.nga.cn/"),
           ("Upgrade", "Insecure - Requests: 1")]

# cookies = "UM_distinctid=166bf140cea486-0c4685494fe79d-594c2a16-306000-166bf140cebb23; taihe=bb95bf834fe8b9cb417a4f76e57d71ed; ngacn0comUserInfo=%25CF%25CF%25BA%25C5%25CA%25AE%25C1%25F9%09%25E8%2588%25B7%25E5%258F%25B7%25E5%258D%2581%25E5%2585%25AD%0942%0942%09%09-30%0927300%094%090%090%0953_-600%2C61_143; CNZZDATA1256638924=1352051463-1549029003-https%253A%252F%252Fbbs.nga.cn%252F%7C1549029003; CNZZDATA1256638919=1329572441-1540816093-http%253A%252F%252Fbbs.nga.cn%252F%7C1552819746; CNZZDATA1256638828=1805424189-1542356914-http%253A%252F%252Fbbs.nga.cn%252F%7C1553177984; ngaPassportUid=35345195; ngaPassportUrlencodedUname=%25CF%25CF%25BA%25C5%25CA%25AE%25C1%25F9; ngaPassportCid=Z8lud5kqrun2ep630ll258m50io2m3f6qupt307r; CNZZDATA1256638851=887532552-1540798715-http%253A%252F%252Fbbs.nga.cn%252F%7C1554551353; bbsmisccookies=%7B%22uisetting%22%3A%7B0%3A2097152%2C1%3A1563017091%7D%2C%22insad_refreshid%22%3A%7B0%3A%22/WsVWjNWf5dgI1WS2rFTus2g9CqDDOmotPZmB72as%22%2C1%3A1555804933%7D%7D; CNZZDATA1256638820=2027800863-1540799010-http%253A%252F%252Fbbs.nga.cn%252F%7C1555334549; lastvisit=1555344187; lastpath=/; ngacn0comUserInfoCheck=47d76c8094fff1bf752fe9fa9223eb0e; ngacn0comInfoCheckTime=1555344187; taihe_session=ac9f75740b83364d722311d260610b79; CNZZDATA30039253=cnzz_eid%3D1180855752-1540798994-http%253A%252F%252Fbbs.nga.cn%252F%26ntime%3D1555340612; CNZZDATA30043604=cnzz_eid%3D103186534-1540800948-http%253A%252F%252Fbbs.nga.cn%252F%26ntime%3D1555341084; Hm_lvt_5adc78329e14807f050ce131992ae69b=1555241087,1555250152,1555338235,1555344190; Hm_lpvt_5adc78329e14807f050ce131992ae69b=1555344190"
# headers = [("Accept", "text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8"),
#            ("Host", "bbs.nga.cn"),
#            ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763"),
#            ("Referer", "http://bbs.nga.cn/thread.php?fid=-7"),
#            ("Upgrade", "Insecure - Requests: 1"),
#            ("Cookie", cookies)]


filename = str('cookie2.txt')
request = urllib.request.Request(url=url)
mozillaCookieJar = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookiejar=mozillaCookieJar)
opener = urllib.request.build_opener(handler)
opener.addheaders = headers
try:
    response = opener.open(request).read().decode("GBK")
    print(response)
except HTTPError as e:
    print(e.reason)

mozillaCookieJar.save(filename=filename, ignore_discard=True, ignore_expires=True)
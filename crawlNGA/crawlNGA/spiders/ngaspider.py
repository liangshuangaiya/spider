import scrapy

cookies = {"ngaPassportUid=guest05cb343a4f4008",
           "taihe=e75b019a0a164ce02fa7f322c67a5b9c",
           "taihe_session=034fa703f13e81f38b9b187c02adb4fe",
           "Hm_lvt_5adc78329e14807f050ce131992ae69b=1555168413,1555252054",
           "Hm_lpvt_5adc78329e14807f050ce131992ae69b=1555252137",
           "lastvisit=1555252149",
           "guestJs=1555252132",
           "UM_distinctid=16a1c403d2e501-0fae4e11315564-784a5935-158100-16a1c403d2f1a9",
           "CNZZDATA30043604=cnzz_eid%3D1179685297-1555249284-%26ntime%3D1555249284",
           "CNZZDATA30039253=cnzz_eid%3D209741003-1555248811-%26ntime%3D1555248811",
           "lastpath=/thread.php?fid=-7",
           "bbsmisccookies=%7B%22uisetting%22%3A%7B0%3A%22b%22%2C1%3A1555252449%7D%2C%22insad_refreshid%22%3A%7B0%3A%22/WsVWjNWf5dgI1WS2rFTus2g9CqDDOmotPZmB72as%22%2C1%3A1555856936%7D%2C%22pv_count_for_insad%22%3A%7B0%3A-48%2C1%3A1555261312%7D%2C%22insad_views%22%3A%7B0%3A1%2C1%3A1555261312%7D%7D",
           "CNZZDATA1256638820=1760039222-1555251335-http%253A%252F%252Fbbs.nga.cn%252F%7C1555251335"}

headers = {"Accept": "text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8",
           "Host": "bbs.nga.cn",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}


class ngaSpider(scrapy.Spider):

    name = "ngaspider"

    def start_requests(self):
        urls = ["http://bbs.nga.cn/thread.php?fid=-7&page=2",
                "http://bbs.nga.cn/thread.php?fid=-7&page=3"]
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, cookies=cookies, callback=self.parse)

    def parse(self, response):
        page = response.url.split("=")[-1]
        filename = "nga-%s.html" % page
        with open(file=filename, mode="wb", encoding="utf-8") as f:
            f.write(response.body)
        self.log("保存文件：%s" % filename)


if __name__ == "__main__":
    cookie_str = '%s=%s' % (cookies['name'], cookies['value'])
    print(1)
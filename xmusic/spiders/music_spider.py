#-*-coding:utf-8-*-


from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors  import LinkExtractor
from xmusic.items import XmusicItem
from scrapy.http import FormRequest

import requests
import re
import json
import os
import base64
from Crypto.Cipher import AES


class MusicSpider(CrawlSpider):
    name = 'xmusic'
    allowed_domains=["xiami.com"]
    start_urls=[
        "http://www.xiami.com/artist/3110",
        "http://www.xiami.com/artist/135",
        "http://www.xiami.com/artist/23517",
        "http://www.xiami.com/artist/1198",
        "http://www.xiami.com/artist/573",
        "http://www.xiami.com/artist/1469021812",
        "http://www.xiami.com/artist/648",
        "http://www.xiami.com/artist/1166",
        "http://www.xiami.com/artist/7244",
        "http://www.xiami.com/artist/799",
        "http://www.xiami.com/artist/1258",
        "http://www.xiami.com/artist/1195",
        "http://www.xiami.com/artist/1046",
        "http://www.xiami.com/artist/7319",
        "http://www.xiami.com/artist/859",
        "http://www.xiami.com/artist/849",
        "http://www.xiami.com/artist/1175",
        "http://www.xiami.com/artist/1260",
        "http://www.xiami.com/artist/524",
        "http://www.xiami.com/artist/390",
        "http://www.xiami.com/artist/783"]
    rules = [Rule(LinkExtractor(allow=(r'/artist/top-.+'))),
             Rule(LinkExtractor(allow=(r'/song/.+')),callback="parse_song")]



    def parse_song(self,response):
        sel=Selector(response)
        item=XmusicItem()
        item['music_id']=sel.xpath('//link[@rel="canonical"]/@href').extract()
        item['music_name']=sel.xpath('//h1/text()').extract()
        item['lyric']=sel.xpath('//div[@class="lrc_main"]/text()').extract()
        infos=sel.xpath('//table[@id="albums_info"]/tr').extract()
        item['albums_info']=""
        for info in infos:
            s=re.sub('\s*<[^>]+>','',info)
            t=s.strip()
            item['albums_info']+=(t+";")

        return item






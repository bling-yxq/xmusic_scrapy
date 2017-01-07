# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field

class XmusicItem(Item):
    music_id=Field()
    music_name=Field()
    albums_info=Field()
    lyric=Field()

import scrapy

class QuotesSpiderItem(scrapy.Item):
    h1_tag = scrapy.Field()
    tags = scrapy.Field()

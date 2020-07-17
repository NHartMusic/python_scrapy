class QuotesSpiderPipeline(object):
    def process_item(self, item, spider):
        if item['h1_tag']: 
            item['h1_tag'] = item['h1_tag'][0].upper()
        return item

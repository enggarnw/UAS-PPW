import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://pta.trunojoyo.ac.id/welcome/detail/080211100070",
 
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield{
        'Abstrak' : response.css('#content_journal > ul > li > div:nth-child(4) > div:nth-child(2) >  ::text').extract(),


        }

import scrapy

class NonProfitSpider(scrapy.Spider):
    name = "nonprofit"
    start_urls = ['https://news.ycombinator.com/']

    def parse(self, response):
        for title in response.css(''):
            yield {'title': title.css('::text').get()}

            for next_page in response.css('a.next'):
                yield response.follow(next_page, self.parse)

import scrapy

class TechCrunchSpider(scrapy.Spider):
    name="techcrunch"
    allowed_domains=["techcrunch.com"]
    start_urls=[]
    def __init__(self, query="", **kwargs):
        super().__init__(**kwargs)
        self.query = query
        self.start_urls = [f"https://techcrunch.com/search/{query}/"]
    

    def parse(self,response):
       for article in response.css("a.loop-card__title-link"):
        yield {
        "title": article.css("::text").get().strip(),
        "url": article.css("::attr(href)").get()
     }

            
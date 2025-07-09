from scrapy.crawler import CrawlerProcess
from .techcrunch_spider import TechCrunchSpider

def run_scraper(query: str):
    process = CrawlerProcess(settings={"FEEDS": {"output.json": {"format": "json","overwrite":True}}})
    process.crawl(TechCrunchSpider, query=query)
    process.start()

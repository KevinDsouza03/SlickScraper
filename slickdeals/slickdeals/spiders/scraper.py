import requests
import scrapy
from pathlib import Path
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher

path = "E:/Slickdeals-Scraper/output/" #Enter your filepath here
class recentdeals(scrapy.Spider):
    name = "recentdeals"

    custom_settings = {
            
    'FEEDS': {
        f'file:/{path}recentdeals.json': {
            'format': 'json', 
            'overwrite': True,
            'encoding': 'utf8'
            }
        }
    }
    def start_requests(self):
        urls = [
            "https://slickdeals.net/deals/",
            "https://slickdeals.net/deals/?page=2&sort=recent/",
            "https://slickdeals.net/deals/?page=3&sort=recent/",
            "https://slickdeals.net/deals/?page=4&sort=recent/",
            "https://slickdeals.net/deals/?page=5&sort=recent/"
        ] 

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):

        for item in response.css('div.dealRow'): #array for all items on site
            yield{
                "text": item.css('.dealTitle a::text').get(),
                "link": item.css('.dealTitle a::attr(href)').get()
            }
            #Input into json for viewing
        #Title with Price: item.css('.dealTitle a::text').get() ex: 'Amazfit Bip 3 Urban Edition Smart Watch (Black) $24.88'
        #Link: item.css('.dealTitle a::attr(href)').get() ex: '/f/17608467-amazfit-bip-3-urban-edition-smart-watch-black-24-88'

def recent_deals_result():
    dispatcher.connect(signal=signals.item_scraped)
    crawler_process = CrawlerProcess()
    crawler_process.crawl(recentdeals)
    crawler_process.start()
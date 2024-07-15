import requests
import scrapy
import subprocess
from pathlib import Path

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
            "https://slickdeals.net/deals/?page=5&sort=recent/",
            "https://slickdeals.net/deals/?page=4&sort=recent/",
            "https://slickdeals.net/deals/?page=3&sort=recent/",
            "https://slickdeals.net/deals/?page=2&sort=recent/",
            "https://slickdeals.net/deals/",
        ] 

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):

        for item in response.css('div.dealRow'): #array for all items on site
            # title,price = str(item.css('.dealTitle a::text').get()).split('$', 1)
            yield{
                "title": item.css('.dealTitle a::text').get(),
                "price": item.css('div.priceCol span::text').get(),
                "link": "https://slickdeals.net" + item.css('.dealTitle a::attr(href)').get()
            }
            #Input into json for viewing
        #Title with Price: item.css('.dealTitle a::text').get() ex: 'Amazfit Bip 3 Urban Edition Smart Watch (Black) $24.88'
        #Link: item.css('.dealTitle a::attr(href)').get() ex: '/f/17608467-amazfit-bip-3-urban-edition-smart-watch-black-24-88'

def recent_deals_result():
    subprocess.run("scrapy crawl recentdeals", cwd="slickdeals\slickdeals\spiders")
    return 
import requests
import scrapy
import subprocess
from pathlib import Path
path = "E:/Slickdeals-Scraper/output/" #Enter your filepath here
class primeday(scrapy.Spider):
    name = "primeday"

    custom_settings = {
            
    'FEEDS': {
        f'file:/{path}primeday.json': {
            'format': 'json', 
            'overwrite': True,
            'encoding': 'utf8'
            }
        }
    }
    def start_requests(self):
        urls = [
            "https://slickdeals.net/deals/amazon-prime-day/",
        ] 

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):

        for item in response.xpath("/html/body/div[3]/div/main/div[1]/div[2]/ul/li"):
            yield{
                "title": item.css('.bp-c-card_content a::text').get(),
                "originalprice": item.css('.bp-p-dealCard_originalPrice::text').get(),
                "price": item.css('.bp-p-dealCard_price::text').get(),
                "link": "https://slickdeals.net" + item.css('.bp-c-card_content a::attr(href)').get()
            }
            #Input into json for viewing
        #Title with Price: item.css('.dealTitle a::text').get() ex: 'Amazfit Bip 3 Urban Edition Smart Watch (Black) $24.88'
        #Link: item.css('.dealTitle a::attr(href)').get() ex: '/f/17608467-amazfit-bip-3-urban-edition-smart-watch-black-24-88'
        
def prime_day_result():
    subprocess.run("scrapy crawl primeday", cwd="slickdeals\slickdeals\spiders")
    return 

#todo: Fix fetching all items list. Currently only fetching 4. 
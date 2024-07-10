import requests
import scrapy
from pathlib import Path

class recentdeals(scrapy.Spider):
    name = "recentdeals"
    def start_requests(self):
        urls = [
            "https://slickdeals.net/deals/"
        ] #https://slickdeals.net/deals/?page=2&sort=recent

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):

        for item in response.css('div.dealRow'): #array for all items on site
            yield{
                "title": item.css('.dealTitle a::text').get(),
                "link": item.css('.dealTitle a::attr(href)').get()
            }
            #Input into json for viewing
        #Title with Price: item.css('.dealTitle a::text').get() ex: 'Amazfit Bip 3 Urban Edition Smart Watch (Black) $24.88'
        #Link: item.css('.dealTitle a::attr(href)').get() ex: '/f/17608467-amazfit-bip-3-urban-edition-smart-watch-black-24-88'

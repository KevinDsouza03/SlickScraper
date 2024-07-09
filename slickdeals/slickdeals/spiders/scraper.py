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
        page = response.url.split("/")[-2]
        filename = f"recent-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
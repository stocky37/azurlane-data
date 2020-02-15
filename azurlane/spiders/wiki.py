# -*- coding: utf-8 -*-
from scrapy import Spider

from azurlane.scrapers.ship import ShipScraper


class WikiSpider(Spider):
    name = "wiki"
    allowed_domains = ["azurlane.koumakan.jp"]
    start_urls = ["https://azurlane.koumakan.jp/List_of_Ships"]
    slug = "name"

    def __init__(self, *args, **kwargs):
        super(WikiSpider, self).__init__(*args, **kwargs)
        self.shipScraper = ShipScraper()

    def parse(self, response):
        for a in response.css("tr td:first-child a"):
            yield response.follow(a, self.shipScraper.parse)

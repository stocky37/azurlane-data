from abc import ABC

from slugify import slugify


class Scraper(ABC):
    def __init__(self, spider=None):
        self.spider = spider

    def parse(self, response):
        pass

    @staticmethod
    def text(text):
        return text.strip() if text else None

    def slug(self, text):
        return slugify(self.text(text))

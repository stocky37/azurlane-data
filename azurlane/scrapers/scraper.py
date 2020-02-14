from abc import ABC


class Scraper(ABC):
    def __init__(self, spider=None):
        self.spider = spider

    def parse(self, response):
        pass

    @staticmethod
    def text(text):
        return text.strip() if text else None

from scrapy.loader.processors import Compose, Join


def default_processor():
    return Compose(Join(""), str.strip)

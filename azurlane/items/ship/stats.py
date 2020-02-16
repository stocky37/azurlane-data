from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose
from slugify import slugify

from azurlane.items.util import default_processor


class Stats(Item):
    hp = Field()
    fp = Field()
    aa = Field()
    asw = Field()
    lck = Field()
    trp = Field()
    avi = Field()
    rld = Field()
    eva = Field()
    oil = Field()
    acc = Field()
    spd = Field()
    arm = Field()


class StatsLoader(ItemLoader):
    default_item_class = Stats
    default_output_processor = Compose(default_processor(), int)

    arm_out = Compose(default_processor(), slugify)

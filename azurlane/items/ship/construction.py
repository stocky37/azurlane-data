from scrapy import Item, Field
from scrapy.loader import ItemLoader

from azurlane.items.util import default_processor


class Construction(Item):
    time = Field()


class ConstructionLoader(ItemLoader):
    default_item_class = Construction
    default_output_processor = default_processor()

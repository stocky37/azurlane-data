from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, TakeFirst
from slugify import slugify

from azurlane.items.ship import Construction
from azurlane.items.util import default_processor


class Ship(Item):
    dir = "ships"
    id = Field()
    name = Field()
    slug = Field()
    nationality = Field()
    classification = Field()
    construction = Field(serializer=Construction)


class ShipLoader(ItemLoader):
    default_item_class = Ship
    default_output_processor = default_processor()

    slug_out = Compose(default_processor(), slugify)
    nationality_out = Compose(default_processor(), slugify)
    classification_out = Compose(default_processor(), slugify)
    construction_out = TakeFirst()

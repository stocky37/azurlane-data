import json

from scrapy import Item


class JsonPipeline:
    def process_item(self, item, spider):
        filename = spider.settings.get("FILENAME_TEMPLATE").format(
            item.dir, item["slug"]
        )
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.nested_dict(item), f, indent=2, sort_keys=True)
            f.write("\n")
        return item

    def nested_dict(self, item):
        d = dict(item)
        for key, value in d.items():
            if isinstance(value, Item):
                d[key] = self.nested_dict(value)
        return d

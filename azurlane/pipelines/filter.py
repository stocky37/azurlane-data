# filter None values from item
class FilterPipeline(object):
    def process_item(self, item, spider):
        self.filter_falsy_values(item)
        return item

    @staticmethod
    def filter_falsy_values(item):
        for key in list(dict(item).keys()):
            if item[key] is None:
                del item[key]
        return item

from azurlane.items import ShipLoader, ConstructionLoader
from azurlane.scrapers.util import adjacent_cell_text_selector


class ShipScraper:
    def parse(self, response):
        loader = ShipLoader(response=response)
        loader.add_xpath("id", adjacent_cell_text_selector("ID"))
        loader.add_css("name", "h1::text")
        loader.add_css("slug", "h1::text")
        loader.add_xpath("nationality", adjacent_cell_text_selector("Nationality"))
        loader.add_xpath(
            "classification", adjacent_cell_text_selector("Classification")
        )
        loader.add_value("construction", self.parse_construction(response))
        return loader.load_item()

    @staticmethod
    def parse_construction(response):
        loader = ConstructionLoader(response=response)
        loader.add_xpath("time", adjacent_cell_text_selector("Construction Time"))
        return loader.load_item()

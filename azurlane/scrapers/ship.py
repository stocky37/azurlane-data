from azurlane.items import ShipLoader, ConstructionLoader
from azurlane.items.ship import StatsLoader
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
        loader.add_value(
            "stats",
            self.parse_stats(
                response.xpath("//div[@class='nomobile']//div[@title='Base Stats']")
            ),
        )
        loader.add_value("construction", self.parse_construction(response))
        return loader.load_item()

    @staticmethod
    def parse_construction(response):
        loader = ConstructionLoader(response=response)
        loader.add_xpath("time", adjacent_cell_text_selector("Construction Time"))
        return loader.load_item()

    @staticmethod
    def parse_stats(selector):
        def stat_selector(stat):
            return ".//th/img[@alt='{0}']/../following-sibling::td[1]/descendant-or-self::*/text()".format(
                stat
            )

        loader = StatsLoader(selector=selector)
        loader.add_xpath("hp", stat_selector("Health"))
        loader.add_xpath("fp", stat_selector("Firepower"))
        loader.add_xpath("aa", stat_selector("Anti-air"))
        loader.add_xpath("asw", stat_selector("Anti-submarine warfare"))
        loader.add_xpath("lck", stat_selector("Luck"))
        loader.add_xpath("avi", stat_selector("Aviation"))
        loader.add_xpath("rld", stat_selector("Reload"))
        loader.add_xpath("eva", stat_selector("Evasion"))
        loader.add_xpath("oil", stat_selector("Oil consumption"))
        loader.add_xpath("acc", stat_selector("Accuracy"))
        loader.add_xpath("spd", stat_selector("Speed"))
        loader.add_xpath("arm", stat_selector("Armor"))
        return loader.load_item()

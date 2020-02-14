from slugify import slugify

from azurlane.scrapers.scraper import Scraper


class ShipScraper(Scraper):
    def parse(self, response):
        def get_adjacent_cell(text):
            response.xpath(
                "//th[normalize-space()='{0}']/following-sibling::td/text()".format(
                    text
                )
            )

        name = self.text(response.css("h1::text").get())
        yield {
            "_dir": "ships",
            "id": self.text(get_adjacent_cell("ID")),
            "name": name,
            "slug": slugify(name),
        }

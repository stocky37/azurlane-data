from azurlane.scrapers.scraper import Scraper
from azurlane.scrapers.util import get_adjacent_cell_text


class ShipScraper(Scraper):
    def parse(self, response, search_element="*"):
        name = response.css("h1::text").get()
        yield {
            "_dir": "ships",
            "id": self.text(get_adjacent_cell_text(response, "ID")),
            "name": self.text(name),
            "slug": self.slug(name),
            "nationality": self.slug(get_adjacent_cell_text(response, "Nationality")),
            "classification": self.slug(
                get_adjacent_cell_text(response, "Classification")
            ),
            "construction": {
                "time": self.text(get_adjacent_cell_text(response, "Construction Time"))
            },
        }

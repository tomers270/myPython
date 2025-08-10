from qa09.adidas_project.pages import products_page
from playwright.sync_api import expect


class ResultsPage():

    def __init__(self, page):
        self.page = page
        self.products_page = products_page
        self.results_count_label = page.locator("[class = 'heading_count__cdJ1F']")

    def get_results_count(self):
        expect(self.results_count_label).to_be_visible(timeout=10000)
        text = self.results_count_label.inner_text()
        digits = ''.join(ch for ch in text if ch.isdigit())
        if digits:
            return int(digits)
        return 0


    def verify_product_prices(self):
        prices = self.page.query_selector_all("[class = '_sale-color_1dbqy_98']")

        for price in prices:
            price_as_str = price.text_content()
            print(price_as_str)
            price_as_str = price_as_str.replace("$", "")
            price_as_float = float(price_as_str)
            if price_as_float >17:
                print(f"price {price_as_float} is greater than $17")
            assert price_as_float<17, "the price is greater than $17"
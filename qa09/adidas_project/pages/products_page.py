
class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.product_items = page.locator("p[data-testid='product-card-title']")

    def click_product_by_index(self, index):
        self.product_items.nth(index).click()

    def get_product_price_text(self, index):
        price_locator = self.product_items.nth(index).locator("span._sale-color_1dbqy_98")
        return price_locator.inner_text()
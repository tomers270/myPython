from qa09.adidas_project.tests.globals import URL


class HomePage():
    def __init__(self, page):
        self.page = page
        self.search_icon = page.locator("header span.gl-icon__wrapper")
        header=page.locator("header")
        self.help_button = header.get_by_role("link", name = "help")
        self.new_trending_button = page.get_by_text("New & Trending")


    def navigate(self):
        self.page.goto(URL)

    def search_for_product(self, search_value):

        search_field =self.page.get_by_role("textbox", name = "Search")
        search_field.fill(search_value)
        search_field.press("Enter")

    def verify_help_button_exists(self):
        assert self.help_button.is_visible(), "Help button does not exist"

    def verify_new_trending_button_exists(self):
        assert self.new_trending_button.is_visible(), "New & Trending button not found"

    def verify_product_success(self):
        url = self.page.url
        assert url == "https://www.adidas.com/us/search?q=shirt&sitePath=us", "Wrong URL"

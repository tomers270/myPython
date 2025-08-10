from qa09.adidas_project.pages import home_page
from qa09.adidas_project.tests.globals import Product_Name


class TestResultsPage():

    def test_for_search(self, setup_adidas):
        home_page = setup_adidas.home
        results_page = setup_adidas.results
        home_page.search_for_product(Product_Name)
        count = results_page.get_results_count()
        print(f"found {count} results for shirts ")
        assert count > 0

    def test_click_first_product(self, setup_adidas):
        home_page = setup_adidas.home
        products_page = setup_adidas.products
        home_page.navigate()
        home_page.search_for_product(Product_Name)
        products_page.click_product_by_index(0)
        assert "/product" in products_page.page.url, "Did not navigate"

    def test_prices_under_17(self, setup_adidas):
        home_page = setup_adidas.home
        results_page = setup_adidas.results

        home_page.navigate()
        home_page.search_for_product(Product_Name)

        results_page.verify_product_prices()

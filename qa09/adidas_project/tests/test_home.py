from qa09.adidas_project.tests.conftest import setup_adidas
from qa09.adidas_project.tests.globals import Product_Name


class TestHomePage():


        def test_search(self, setup_adidas):
            page = setup_adidas.page
            home_page = setup_adidas.home
            results_page = setup_adidas.results

            home_page.navigate()

            home_page.search_for_product(Product_Name)

            count = results_page.get_results_count()


            assert count>0, "Search returned no results"



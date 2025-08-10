

class TestHelpButton:
    def test_new_trending_exists(self, setup_adidas):
        home_page = setup_adidas.home
        home_page.navigate()
        home_page.verify_new_trending_button_exists()
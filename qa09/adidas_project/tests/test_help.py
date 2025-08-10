

class TestHelpButton:
    def test_help_button_exists(self, setup_adidas):
        setup_adidas.home.navigate()
        setup_adidas.home.verify_help_button_exists()


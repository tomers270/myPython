


class TestpProduct():

    def test_verify_prices_less_than_100(self, setup_swaglabs):
        page, loginPage, productPage = setup_swaglabs
        loginPage.login("standard_user", "secret_sauce")
        productPage.verify_product_prices()

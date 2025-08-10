from types import SimpleNamespace

import pytest
from playwright.sync_api import sync_playwright, expect

from qa09.adidas_project.pages.home_page import HomePage
from qa09.adidas_project.pages.products_page import ProductsPage
from qa09.adidas_project.pages.results_page import ResultsPage
from qa09.adidas_project.tests.globals import URL
from qa09.swaglabs_pom.pages.login_page import loginPage
from qa09.swaglabs_pom.pages.product_page import productPage



@pytest.fixture()
def setup_adidas():
    print("### Test start ###")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(URL)

        yield SimpleNamespace(
            page=page,
            home=HomePage(page),
            products=ProductsPage(page),
            results=ResultsPage(page)
        )

        print("### Test end ###")
        page.close()
        browser.close()
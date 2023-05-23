from library.basic_selenium_actions import *
from library.comparison_actions import *
from constants.xpath.art_of_testing import *
from library.exception_handlers import *
from constants.xpath.saucedemo import *
import time
import pytest


@pytest.fixture
def driver():
    driver = open_browser_to_link("https://www.saucedemo.com/")
    yield driver
    # Teardown driver
    driver.quit()


def test_login(driver):
    wait_until_element_is_visible(driver, txt_box_username)
    enter_text_in_element(driver, txt_box_username, 'standard_user')
    enter_text_in_element(driver, txt_box_password, 'secret_sauce')
    click_element(driver, btn_login)
    wait_until_element_is_visible(driver, "//span[contains(text(), 'Products')]")
    should_be_equal_as_strings(driver, "//span[contains(text(), 'Products')]", "Products")
    
def test_product_search(driver):
    pass

def test_add_to_cart(driver):
    pass

def test_cart_functionality(driver):
    pass

def test_checkout(driver):
    pass
# Testing login is successful
# Product is found successfully
# Add to cart button is working or not
# Check if product is added to cart
# Checkout
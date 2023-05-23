from library.basic_selenium_actions import *
from library.comparison_actions import *
from constants.xpath.art_of_testing import *
from library.exception_handlers import *
from library.data_helper import *
from constants.xpath.saucedemo import *
import time


data = read_csv_data("C:/Users/Amogh/Projects/TGI/Selenium_Framework/constants/data/saucedemo_login.csv")
driver = open_browser("https://www.saucedemo.com/")
wait_until_element_is_visible(driver, txt_box_username)
enter_text_in_element(driver, txt_box_username, data[0]['txt_box_username'])
enter_text_in_element(driver, txt_box_password, data[0]['txt_box_password'])
click_element(driver, btn_login)
time.sleep(2)
wait_until_element_is_visible(driver, lnk_backpack)
click_element(driver, lnk_backpack)
wait_until_element_is_clickbale(driver, btn_add_to_cart)
time.sleep(2)
click_element(driver, btn_add_to_cart)
wait_until_element_is_visible(driver, btn_remove)
time.sleep(10)

# reader = csv.DictReader("C:\Users\harish\Desktop\Selenium_Framework_New\constants\data\saucedemo_login.csv")
#print(reader.fieldname)
#with open(reader) as csvfile:
#    Print(reader["txt_box_username"])

#driver = open_browser("https://www.saucedemo.com/")
#wait_until_element_is_visible(driver, txt_box_username)
#enter_text_in_element(driver, txt_box_username, 'standard_user')
#enter_text_in_element(driver, txt_box_password, 'secret_sauce')
#click_element(driver, btn_login)
#time.sleep(10)
#wait_until_element_is_visible(driver, lnk_backpack)
#click_element(driver, lnk_backpack)
#wait_until_element_is_clickbale(driver, btn_add_to_cart)
#time.sleep(2)
#click_element(driver, btn_add_to_cart)
#wait_until_element_is_visible(driver, btn_remove)
#time.sleep(10)

#driver = open_browser_to_link("https://artoftesting.com/samplesiteforselenium")
#wait_until_element_is_visible(driver, lnk_link_text)
#take_screenshot(driver)
#expect_error(driver, wait_until_element_is_visible, "ksdjkhdsfhfiuefeyiasdah")
#take_screenshot(driver)
#take_screenshot(driver, "firstScreenShot.png")
#time.sleep(30)
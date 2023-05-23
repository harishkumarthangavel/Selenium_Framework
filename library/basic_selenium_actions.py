from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
import datetime

#def open_browser_to_link(url):
#    service = Service("C:/Users/Amogh/Desktop/selenium_framework/Constants/driver/chromedriver.exe")
#    chrome_options = Options()
#    chrome_options.add_argument("--incognito")
#    driver = webdriver.Chrome(service=service, options=chrome_options)
#    driver = webdriver.Chrome(service=service)
#    driver.maximize_window()
#    driver.get(url)
#    return driver

#def open_browser_incognito(url):
#    service = Service("C:/Users/Amogh/Desktop/selenium_framework/Constants/driver/chromedriver.exe")
#    driver = webdriver.Chrome(service=service)
#    driver.maximize_window()
#    driver.get(url)
#    return driver

def open_browser_incognito(url, incognito):
    service = Service("C:/Users/Amogh/Desktop/selenium_framework/Constants/driver/chromedriver.exe", headless=True)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get(url)
    return driver

def open_browser(url, incognito=False, headless=False):
    service = Service("C:/Users/Amogh/Desktop/selenium_framework/Constants/driver/chromedriver.exe")
    chrome_options = Options()
    if incognito:
        chrome_options.add_argument("--incognito")
        
    if headless:
        chrome_options.add_argument("--headless")
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get(url)
    return driver

def click_element(driver, xpath):
    # implicit wait time
    wait_until_element_is_clickbale(driver, xpath, wait_time=10)
    element = driver.find_element(By.XPATH, xpath)
    element.click()

def enter_text_in_element(driver, xpath, text):
    # implicit wait time
    wait_until_element_is_visible(driver, xpath, wait_time=10)
    element = driver.find_element(By.XPATH, xpath)
    element.send_keys(text)

def get_element_text(driver, xpath):
    # implicit wait time
    wait_until_element_is_visible(driver, xpath, wait_time=10)
    element = driver.find_element(By.XPATH, xpath)
    return element.text

def scroll_element_into_view(driver, xpath):
    # implicit wait time
    wait_until_element_is_visible(driver, xpath, wait_time=10)
    element = driver.find_element(By.XPATH, xpath)
    driver.execute_script("arguments[0].scrollIntoView();", element)

def select_value_in_dropdown(driver, xpath, value):
    # implicit wait time
    wait_until_element_is_visible(driver, xpath, wait_time=10)
    element = driver.find_element(By.XPATH, xpath)
    dropdown = Select(element)
    dropdown.select_by_value(value)

def handle_alert(driver, accept=True):
    alert = Alert(driver)
    alert_text_message = alert.text
    if accept:
        alert.accept()
    else:
        alert.dismiss()
    
    return alert_text_message

# explicit wait time
def wait_until_element_is_visible(driver, xpath, wait_time=10):
    wait = WebDriverWait(driver, wait_time)
    try:
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        if element:
            return f"Element found: {xpath}."
    except Exception as e:
        print(f"{e}: Element not found: {xpath}.")
        
        
# explicit wait time
def wait_until_element_is_clickbale(driver, xpath, wait_time=10):
    wait = WebDriverWait(driver, wait_time)
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        if element:
            return f"Element found: {xpath}."
    except Exception as e:
        print(f"{e}: Element not found: {xpath}.")

def take_screenshot(driver, filename=None):
    file_name_ext = filename if filename else datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    screenshot_data = driver.get_screenshot_as_png()
    with open(file_name_ext, 'wb') as file:
        file.write(screenshot_data)


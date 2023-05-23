from .basic_selenium_actions import get_element_text
import logging

logging.basicConfig(
    filename='automation.log',  # Specify the log file path
    level=logging.INFO,  # Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Specify the log message format
)


def should_be_equal(driver, xpath, expected_value):
    element_text = get_element_text(driver, xpath)
    try:
        assert element_text == expected_value
        print(f"Assertion passed, text \"{element_text}\" equal to expected text \"{expected_value}\".")
    except AssertionError as e: # e is referencing the assertionerror
        print(f"Assertion failed, text \"{element_text}\" not equal to expected text \"{expected_value}\".")
        raise AssertionError

def should_be_equal_as_strings(driver, xpath, expected_text, lowercase=False):
    element_text = get_element_text(driver, xpath)
    try:
        if lowercase:
            assert str(element_text).lower() == str(expected_text).lower()
        else:
            assert str(element_text) == str(expected_text)
        print(f"Assertion passed, string \"{element_text}\" equal to expected string \"{expected_text}\".")
    except AssertionError as e: # e is referencing the assertionerror
        print(f"Assertion failed, string \"{element_text}\" not equal to expected string \"{expected_text}\".")
        raise AssertionError

def should_be_equal_as_integers(driver, xpath, expected_number):
    element_text = get_element_text(driver, xpath)
    try:
        assert int(element_text) == int(expected_number)
        print(f"Assertion passed, integer \"{element_text}\" equal to expected integer \"{expected_number}\".")
    except AssertionError as e: # e is referencing the assertionerror
        print(f"Assertion failed, integer \"{element_text}\" not equal to expected integer \"{expected_number}\".")
        raise AssertionError

def should_be_empty(driver, xpath):
    element_text = get_element_text(driver, xpath)
    try:
        assert element_text == None or len(element_text) == 0
        print(f"Assertion passed, element text is empty.")
    except AssertionError as e: # e is referencing the assertionerror
        print(f"Assertion failed, expected empty element text, got \"{element_text}\".")
        raise AssertionError

def should_contain(driver, xpath, expected_text):
    element_text = get_element_text(driver, xpath)
    try:
        assert expected_text in element_text
        print(f"Assertion passed, \"{element_text}\" contains \"{expected_text}\".")
        logging.info(f"Assertion passed, \"{element_text}\" contains \"{expected_text}\".")
    except AssertionError as e: # e is referencing the assertionerror
        # print(f"Assertion failed, \"{element_text}\" does not contain \"{expected_text}\".")
        raise AssertionError(f"{e}: Assertion failed, \"{element_text}\" does not contain \"{expected_text}\".")
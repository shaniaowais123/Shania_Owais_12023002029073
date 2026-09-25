import time

from selenium.webdriver.common.by import By

from pages.login_page import LoginPage

from utilities.config_reader import read_config

from utilities.csv_reader import read_test_data

from utilities.screenshot import take_screenshot


def test_login(driver):

    try:

        
        config = read_config()
        time.sleep(2)

        
        data = read_test_data("data/test_data.csv")
        email = data[0]["email"]
        password = data[0]["password"]
        time.sleep(2)

        
        driver.get(config["url"])
        time.sleep(3)

        
        driver.find_element(
            By.XPATH,
            "//span[text()='My Account']"
        ).click()
        time.sleep(3)

        
        driver.find_element(
            By.LINK_TEXT,
            "Login"
        ).click()
        time.sleep(3)

        
        login_page = LoginPage(driver)
        login_page.enter_email(email)
        time.sleep(2)

        login_page.enter_password(password)
        time.sleep(2)

        login_page.click_login()
        time.sleep(4)

        
        assert "My Account" in driver.page_source
        time.sleep(3)

    except Exception:

        take_screenshot(driver, "login_failed")

        raise
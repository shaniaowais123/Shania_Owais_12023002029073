import time

from pages.home_page import HomePage

from pages.product_page import ProductPage

from pages.cart_page import CartPage

from utilities.csv_reader import read_test_data

from utilities.screenshot import take_screenshot


def test_add_product_to_cart(driver):

    try:

        
        driver.get("https://tutorialsninja.com/demo/")
        time.sleep(3)

        
        data = read_test_data("data/test_data.csv")
        product_name = data[0]["product"]
        time.sleep(2)

        
        home_page = HomePage(driver)
        home_page.search_product(product_name)
        time.sleep(3)

       
        assert home_page.is_product_displayed(product_name)
        time.sleep(2)

       
        driver.find_element(
            "link text",
            product_name
        ).click()
        time.sleep(3)

        
        product_page = ProductPage(driver)
        product_page.click_add_to_cart()
        time.sleep(3)

       
        product_page.go_to_cart()
        time.sleep(3)

        
        cart_page = CartPage(driver)
        assert cart_page.is_product_in_cart(product_name)
        time.sleep(3)

        print("PASS: Product is successfully added to cart")

    except Exception:

        take_screenshot(driver, "cart_failed")

        raise
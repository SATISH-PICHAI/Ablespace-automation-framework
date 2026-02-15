from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutInfoPage:

    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")

    def enter_information(self, fname, lname, zip_code):
        wait = WebDriverWait(self.driver, 10)

        # First Name
        first = wait.until(EC.visibility_of_element_located(self.first_name))
        first.clear()
        first.send_keys(fname)

        # Last Name
        last = wait.until(EC.visibility_of_element_located(self.last_name))
        last.clear()
        last.send_keys(lname)

        # Postal Code
        zip_field = wait.until(EC.visibility_of_element_located(self.postal_code))
        zip_field.clear()
        zip_field.send_keys(zip_code)

        # Continue Button
        continue_button = wait.until(
            EC.element_to_be_clickable(self.continue_btn)
        )

        self.driver.execute_script("arguments[0].scrollIntoView();", continue_button)
        self.driver.execute_script("arguments[0].click();", continue_button)

        # Wait for navigation to next page
        wait.until(EC.url_contains("checkout-step-two"))

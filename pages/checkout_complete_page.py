from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutCompletePage:

    def __init__(self, driver):
        self.driver = driver
        self.success_msg = (By.CLASS_NAME, "complete-header")

    def get_success_message(self):
        wait = WebDriverWait(self.driver, 10)

        # 🔥 First wait for URL change
        wait.until(EC.url_contains("checkout-complete"))

        # Then wait for success message
        element = wait.until(
            EC.visibility_of_element_located(self.success_msg)
        )

        return element.text

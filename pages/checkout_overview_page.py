from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverviewPage:

    def __init__(self, driver):
        self.driver = driver
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.finish_btn = (By.ID, "finish")

    def get_total_amount(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            EC.visibility_of_element_located(self.total_label)
        )
        return element.text

    def click_finish(self):
        wait = WebDriverWait(self.driver, 10)
        finish_button = wait.until(
            EC.element_to_be_clickable(self.finish_btn)
        )
        finish_button.click()

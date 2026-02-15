from selenium import webdriver


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # 🔥 Completely disable password manager + password leak detection
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }

    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    return driver

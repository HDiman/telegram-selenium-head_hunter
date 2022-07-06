from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent


chrome_driver_path = "/Users/dsannikov/Documents/GitHub/ParsingPages/telegram-selenium-head_hunter/driver/chromedriver"

# User-Agent. Important to add (UserAgent(verify_ssl=False)
useragent = UserAgent(verify_ssl=False)

# options
options = webdriver.ChromeOptions()
# options.add_argument(f"user-agent={useragent.random}")

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

url = "https://profi.ru/backoffice/n.php"

try:
    driver.get(url=url)
    time.sleep(100)

    login_input = driver.find_element(By.CLASS_NAME, "ui-input__placeholder_optional")
    login_input.send_keys("+79160585921")

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

# ui-input ui-input-bo login-form__input-login ui-input_desktop ui-input_with-placeholder_empty
# from seleniumwire import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# options
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
chrome_driver_path = "/Users/dsannikov/Documents/GitHub/ParsingPages/telegram-selenium-head_hunter/driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)


# url = "https://profi.ru/backoffice/n.php"
# url = "https://vk.com/"
url = "https://id.vk.com/auth?app_id=7913379&v=1.48.0&redirect_uri=https%3A%2F%2Fvk.com%2Ffeed&uuid=vlYZgdUAB-3jnb4qY5xlk&action=eyJuYW1lIjoibm9fcGFzc3dvcmRfZmxvdyIsInBhcmFtcyI6eyJ0eXBlIjoic2lnbl9pbiJ9fQ%3D%3D"

try:
    driver.get(url=url)
    time.sleep(10)

    # login_input = driver.find_element(By.CLASS_NAME, "ui-input__placeholder_optional")
    # login_input.send_keys("+79160585921")

    login_input = driver.find_element(By.CLASS_NAME, "vkc__TextField__input")
    login_input.send_keys("+79160585921")

    # FlatButton__in

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


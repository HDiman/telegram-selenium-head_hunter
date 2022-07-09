from seleniumwire import webdriver
# from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


# options
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
chrome_driver_path = "/Users/dsannikov/Documents/GitHub/ParsingPages/telegram-selenium-head_hunter/driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)



url = "https://profi.ru/backoffice/n.php"
# url = "https://vk.com/"
# url = "https://id.vk.com/auth?app_id=7913379&v=1.48.0&redirect_uri=https%3A%2F%2Fvk.com%2Ffeed&uuid=vlYZgdUAB-3jnb4qY5xlk&action=eyJuYW1lIjoibm9fcGFzc3dvcmRfZmxvdyIsInBhcmFtcyI6eyJ0eXBlIjoic2lnbl9pbiJ9fQ%3D%3D"
# url = "https://phptravels.com/demo/"


try:
    driver.get(url=url)
    time.sleep(5)

    login_input = driver.find_element(By.CLASS_NAME, "login-form__input-login")
    login_input.clear()
    login_input.send_keys("+79160585921")
    time.sleep(5)

    submit_button = driver.find_element(By.CLASS_NAME, "login-form__button").click()
    input_code = input("Please input number: ")
    time.sleep(5)

    # ui-pin-input
    for i in range(4):
        enter_code = driver.find_element(By.CLASS_NAME, "ui-pin-input")
        enter_code.send_keys(f"{input_code[i]}")
        time.sleep(10)
    time.sleep(60)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


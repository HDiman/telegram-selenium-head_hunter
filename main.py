from seleniumwire import webdriver
# from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Path to chromedriver
chrome_driver_path = "/Users/dsannikov/Documents/GitHub/ParsingPages/telegram-selenium-head_hunter/driver/chromedriver"

# Options
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")

# Creating Driver Object
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

# Link to Main Webpage
url = "https://profi.ru/backoffice/n.php"

# Entering inside the Main page
try:
    # Enter page
    driver.get(url=url)
    time.sleep(5)

    # Enter login with phone number
    login_input = driver.find_element(By.CLASS_NAME, "login-form__input-login")
    login_input.clear()
    login_input.send_keys("+79160585921")
    time.sleep(5)
    submit_button = driver.find_element(By.CLASS_NAME, "login-form__button").click()

    # Input code instead of password
    input_code = input("Please input number: ")
    time.sleep(5)
    for i in range(4):
        enter_code = driver.find_element(By.CLASS_NAME, "ui-pin-input")
        enter_code.send_keys(f"{input_code[i]}")
        time.sleep(2)

    # Waiting for page downloaded
    time.sleep(30)

    # Find out href link to pass for enter inside
    chat_order = driver.find_element(By.XPATH, "//*[@id='BO_REACT_MOBILE_TAB_BAR']/nav/a[2]").get_attribute('href')
    print(chat_order)
    time.sleep(5)

    # inside chat
    driver.get(url=chat_order)
    time.sleep(5)

    # Find out href link to pass for Finished Jobs
    finished_order = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/a[3]").get_attribute('href')
    print(finished_order)
    time.sleep(5)

    # inside chat
    driver.get(url=finished_order)
    time.sleep(5)

    # Subjects
    clients_fin_order = driver.find_elements(By.CLASS_NAME, "client-info__name")
    dates_fin_order = driver.find_elements(By.CLASS_NAME, "lbl")
    addresses_fin_order = driver.find_elements(By.XPATH, "//div[@title='Район']")
    subjects_fin_order = driver.find_elements(By.CLASS_NAME, "subjects")
    descriptions_fin_order = driver.find_elements(By.CLASS_NAME, "aim")
    prices_fin_order = driver.find_elements(By.XPATH, "//div[@title='Ставка']")

    for i in range(len(clients_fin_order)):
        print(f"{i+1}: Клиент: {clients_fin_order[i].text},\n"
              f"заказ от: {dates_fin_order[i].text},\n"
              f"адрес: {addresses_fin_order[i].text},\n"
              f"тема: {subjects_fin_order[i].text},\n"
              f"проблема: {descriptions_fin_order[i].text},\n"
              f"стоимость заказа: {prices_fin_order[i].text}\n")
        time.sleep(5)

    time.sleep(60)





except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


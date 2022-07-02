from selenium import webdriver
import time

chrome_driver_path = "/Users/dsannikov/Documents/GitHub/ParsingPages/telegram-selenium-head_hunter/driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
url = "https://hh.ru/search/vacancy?area=1&clusters=true&enable_snippets=true&ored_clusters=true&search_field=name&search_period=1&text=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82+python&from=SIMILAR_QUERY&hhtmFromLabel=SIMILAR_QUERY&hhtmFrom=vacancy_search_list"


try:
    driver.get(url=url)
    time.sleep(30)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

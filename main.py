# from selenium import webdriver
from seleniumwire import webdriver
import time
from fake_useragent import UserAgent


chrome_driver_path = "/Users/dsannikov/Documents/GitHub/ParsingPages/telegram-selenium-head_hunter/driver/chromedriver"

# User-Agent. Important to add (UserAgent(verify_ssl=False)
useragent = UserAgent(verify_ssl=False)

# options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")

# set proxy
options.add_argument("--proxy-server=23.227.38.25:80")


driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)


# url = "https://hh.ru/search/vacancy?area=1&clusters=true&enable_snippets=true&ored_clusters=true&search_field=name&search_period=1&text=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82+python&from=SIMILAR_QUERY&hhtmFromLabel=SIMILAR_QUERY&hhtmFrom=vacancy_search_list"
# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
# url = "https://2ip.ru"
url = "https://profi.ru/backoffice/n.php"

try:
    driver.get(url=url)
    time.sleep(100)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

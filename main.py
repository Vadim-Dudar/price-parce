from selenium import webdriver
import config, time, fake_useragent
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import  BeautifulSoup as bs


options = webdriver.FirefoxOptions()
options.set_preference('general.useragent.override', fake_useragent.UserAgent().random)
driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))


try:
    query = 'Варочная панель Zigmund & Shtain CI 32.6 I'.replace(' ', '%20').replace('&', '%26')
    driver.get(config.domen + config.search + query)
    soup = bs(driver.page_source, 'lxml')
    print(soup.find('span', class_='p-card__price--new text-subtitle-price-bold').text.replace('от ', '').replace(' ', '').replace('₽', ''))
except:
    pass
finally:
    driver.close()
    driver.quit()

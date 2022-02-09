from selenium import webdriver
import config, time, fake_useragent
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import  BeautifulSoup as bs


options = webdriver.FirefoxOptions()
options.set_preference('general.useragent.override', fake_useragent.UserAgent().random)
driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))


try:
    driver.get(config.url)
    soup = bs(driver.page_source, 'lxml')
    print(soup.find('span', class_='p-card__price--new text-subtitle-price-bold').text.replace('от ', '').replace(' ', '').replace('₽', ''))
except:
    pass
finally:
    driver.close()
    driver.quit()

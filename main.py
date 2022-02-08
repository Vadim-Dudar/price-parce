from selenium import webdriver
import config, time, fake_useragent, requests
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


options = webdriver.FirefoxOptions()
options.set_preference('general.useragent.override', fake_useragent.UserAgent().random)
driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))


try:
    driver.get('https://instagram.com/h0opsy')
    time.sleep(12)
except Exception as ex:
    pass
finally:
    driver.close()
    driver.quit()

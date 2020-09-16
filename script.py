from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.get('https://mail.google.com')


driver.find_element_by_name("identifier").send_keys("xulupes0@gmail.com")
driver.find_element_by_name("identifier").send_keys(Keys.ENTER)
time.sleep(1.0)
driver.find_element_by_name("password").send_keys("3348mazharul")
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(5.0)
#login done


#lets open youtube now
driver.get('https://www.youtube.com/channel/UC-EN-c1TgNYbMnPc0DpBwkQ')
time.sleep(2.0)
driver.find_element_by_class_name("ytd-subscribe-button-renderer").click()
print("Subscribed :)")

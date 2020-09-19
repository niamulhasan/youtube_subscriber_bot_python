from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def subscribe_action(email, password, channel):

    #choose a driver, chrome or firefox
    if(False):
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

        driver = webdriver.Firefox(firefox_profile=firefox_profile)
        driver.get('https://mail.google.com')
    else: 
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")

        caps = options.to_capabilities()

        driver = webdriver.Chrome(desired_capabilities=caps)
        driver.get('https://mail.google.com')




    #mazharulpes19@gmail.com
    driver.find_element_by_name("identifier").send_keys(email)
    time.sleep(6.0)
    driver.find_element_by_name("identifier").send_keys(Keys.ENTER)
    time.sleep(1.0)
    #"3348mazharul"
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("password").send_keys(Keys.ENTER)
    time.sleep(8.0)
    #login done

    #lets open youtube now
    driver.get(channel)
    time.sleep(5.0)
    #click subscribe

    driver.find_element_by_class_name("ytd-subscribe-button-renderer").click()
    print("Subscribed :)")


subscribe_action("mazharulpes17@gmail.com", "3348mazharul", "https://www.youtube.com/channel/UCFWOKous0aDpOhlZuPwhMYA")

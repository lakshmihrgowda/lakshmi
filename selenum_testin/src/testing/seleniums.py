from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome('./chromedriver.exe')
driver.get("https://accounts.google.com/signin/v2/identifier?service=wise&passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&utm_medium=button&utm_campaign=web&utm_content=gotodrive&usp=gtd&ltmpl=drive&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
print(driver.title)
time.sleep(7)
search_bar = driver.find_element_by_xpath("//*[@id=\"identifierId\"]")
search_bar.send_keys("some text")

time.sleep(7000)
driver.close()

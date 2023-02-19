from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
#options.add_argument("incognito")
driver = webdriver.Chrome(options=options)
#driver.get("http://www.google.com")
driver.get("https://amzn.to/3kanXrC")
#imag=driver.find_element(By.XPATH,"(//*[contains(@src, '61pL1J8onTL._SL1500_.jpg')])[2]")
img=driver.find_element(By.ID,"landingImage")
action=ActionChains(driver)
action.move_to_element(img).perform()

from selenium import webdriver
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://google.com")
driver.find_element(By.XPATH,"//*[@id='gb']/div[2]/div[3]/div[1]/div/div[1]/a").click()

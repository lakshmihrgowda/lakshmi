from selenium import webdriver
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://google.com")
driver.find_element(By.XPATH,"//a[@class='gb_p' and @ aria-label='Gmail (opens a new tab)']").click()
driver.find_element(By.XPATH,"//a[@class='gb_p' and @ aria-label='Gmail (opens a new tab)']").click()


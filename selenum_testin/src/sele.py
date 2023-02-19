from selenium import webdriver
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://google.com")
driver.find_element(By.XPATH,"//a[@class='gb_p' and @ aria-label='Gmail (opens a new tab)']").click()
#//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/ul[1]/li[2]/a/div[5]/span
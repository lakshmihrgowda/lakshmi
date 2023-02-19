from selenium import webdriver
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://amazon.com")
driver.find_element(By.XPATH,"//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div/div[1]/span/a").click()
#//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div/div[1]/span/a

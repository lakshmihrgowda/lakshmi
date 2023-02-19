from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
#driver.maximize_window()
driver.get("http://amazon.com")
driver.find_element(By.XPATH,"//*[@id='ivLargeImage']/img").click()
#//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div/div[1]/s
#//*[@id='ivLargeImage']/img
#//img[@draggable='false' and @ alt src='chrome://favicon2/?size=24&scaleFactor=1x&showFallbackMonogram=&pageUrl=https%3A%2F%2Fwww.zee5.com%2F']
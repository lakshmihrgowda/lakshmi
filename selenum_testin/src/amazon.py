from selenium import webdriver
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://amazon.com")
driver.find_element(By.XPATH,"//span[@id='nav-cart-count']").click()
#//*[@id="CardInstancejKWr7q6jjxjkjwUusCYjJg"]/div[2]/div[1]/div/div/div[2]/span/a/div/img
#//*[@id="nav-cart-text-container"]
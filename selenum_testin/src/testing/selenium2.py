from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("http://www.gmail.com")
driver.find_element_by_name('q').send_keys("selenium tutorial")
driver.find_element("name","field-keywords").send_keys("Kurtas")
#driver.find_element("name","q").send_keys("Selenium tutorials python")
driver.find_element(By.XPATH,"///*[@id='gb']/div/div[1]/div/div[1]/a")
#driver.find_element(gmail.LINK_TEXT, 'Login').click()

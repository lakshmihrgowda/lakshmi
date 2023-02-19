#Selenium code to Lunch the browser using URL : 
from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\\chromedriver.exe");
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://www.google.com//");
#to refresh the browser
#driver.refresh()
#to close the browser
#driver.close()
webdriver.find_element_by_name('q').send_keys("selenium tutorial")

from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("http://www.google.com")
#driver.find_element_by_name('q').send_keys("selenium tutorial")
#driver.find_element("name","field-keywords").send_keys("Kurtas")
driver.find_element("name","q").send_keys("Selenium tutorials python")



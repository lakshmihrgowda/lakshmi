from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
#from idlelib.idle_test.test_colorizer import source
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("start-maximized")
#options.add_argument("incognito")
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

action=ActionChains(driver)
resizable=driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")

action.scroll_by_amount(1600, 0).perform()
#action.click_and_hold(resizable).move_by_offset(0,50).perform()





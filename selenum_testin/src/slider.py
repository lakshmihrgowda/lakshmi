from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from idlelib.idle_test.test_colorizer import source
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
#options.add_argument("incognito")
driver = webdriver.Chrome(options=options)
#driver.get("http://www.google.com")
driver.get("https://testautomationpractice.blogspot.com/")
slide=driver.find_element(By.XPATH,"//*[contains(@class,'ui-slider-handle')]")
action=ActionChains(driver)
# action.double_click(slide).perform()
#action.drag_and_drop_by_offset(slide,160,0).perform()
action.click_and_hold(slide).move_by_offset(100,0).perform()
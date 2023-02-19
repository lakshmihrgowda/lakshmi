from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#from tkinter import Radiobutton

options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)
driver.switch_to.frame("frame-one1434677811")
first_name=driver.find_element(By.XPATH,"//input[@type='text' and @ name='RESULT_TextField-1']")
first_name.send_keys("Lakshmi")
last_name=driver.find_element(By.XPATH,"//input[@type='text' and @ name='RESULT_TextField-2']")
last_name.send_keys("H R")
#Radiobutton=driver.find_element(By.XPATH,"//span[@class='question top_question']")
#Radiobutton.select()
#class="question top_question"
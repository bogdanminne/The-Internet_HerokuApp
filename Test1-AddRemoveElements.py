#imports

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

#Initializing web driver
website = 'https://the-internet.herokuapp.com/add_remove_elements/'
driver = webdriver.Chrome()
driver.get(website)

#Testing add/remove element functinality
add_element = driver.find_element(By.CSS_SELECTOR, "#content > div > button")
add_element.click()
add_element.click()

sleep(2)

delete_element = driver.find_element(By.CLASS_NAME, 'added-manually')
delete_element.click()

sleep(2)

#Closing session
driver.quit()

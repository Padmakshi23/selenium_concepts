import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.db4free.net/")

driver.find_element(By.XPATH, "//a[@href='/phpMyAdmin']").click()
# print(driver.title)
# print(driver.current_url)

# print(driver.window_handles)
# print(driver.window_handles[0])
# print(driver.window_handles[1])

driver.switch_to.window(driver.window_handles[1])


driver.find_element(By.ID,"input_username").send_keys("padmakshi")
driver.find_element(By.ID,"input_password").send_keys("welcome@123")
driver.find_element(By.ID,"input_go").click()

time.sleep(5)

#driver.close()

time.sleep(5)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demo.openemr.io/b/openemr")

driver.find_element(By.ID,"authUser").send_keys("admin")
driver.find_element(By.ID,"clearPass").send_keys("pass")
select_lang=Select(driver.find_element(By.XPATH,"//select[@name='languageChoice']"))
select_lang.select_by_visible_text("English (Indian)")
driver.find_element(By.ID,"login-button").click()

driver.find_element(By.XPATH, "//div[text()='Patient']").click()
driver.find_element(By.XPATH, "//div[text()='New/Search']").click()
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@name='pat']"))
time.sleep(5)

driver.find_element(By.ID, "form_fname").send_keys("Padmakshi")

driver.find_element(By.ID, "form_lname").send_keys("Jain")

driver.find_element(By.ID, "form_DOB").send_keys("2000-23-01")

driver.find_element(By.XPATH, "//option[text()='Female']").click()

driver.find_element(By.ID, "create").click()

driver.switch_to.default_content()

driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='modalframe']"))

driver.find_element(By.XPATH, "//input[@value='Confirm Create New Patient']").click()

driver.switch_to.default_content()

time.sleep(5)

alert_text = driver.switch_to.alert.text

print(alert_text)

driver.switch_to.alert.accept()

driver.find_element(By.XPATH, "//div[@class='closeDlgIframe']").click()

driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@name='pat']"))

print(driver.find_element(By.XPATH, "//h2[contains(text(),'Medical Record Dashboard')]").text)

driver.switch_to.default_content()

time.sleep(5)
driver.quit()

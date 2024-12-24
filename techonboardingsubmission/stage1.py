
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time

#Opening BrowserStack and clicking on pricing and toggling price - Chrome

driver = webdriver.Chrome()
driver.get("https://www.browserstack.com/")
driver.maximize_window()

print(driver.title)
time.sleep(3)
link = driver.find_element(By.LINK_TEXT,'Pricing')
link.click()
time.sleep(3)
btn = driver.find_element(By.CLASS_NAME,'switch-wrap')
btn.click()
time.sleep(3)

choose = driver.find_element(By.XPATH,'/html/body/main/div[4]/div[3]/div/div[2]/div[2]/div[1]/div[5]/div/div[2]/div[6]')
choose.click()

driver.quit()


#Opening BrowserStack and clicking on pricing and toggling price - Firefox

driver = webdriver.Firefox()
driver.get("https://www.browserstack.com/")
driver.maximize_window()

print(driver.title)
time.sleep(3)
link = driver.find_element(By.LINK_TEXT,'Pricing')
link.click()
time.sleep(3)
btn = driver.find_element(By.CLASS_NAME,'switch-wrap')
btn.click()
time.sleep(3)

choose = driver.find_element(By.XPATH,'/html/body/main/div[4]/div[3]/div/div[2]/div[2]/div[1]/div[5]/div/div[2]/div[6]')
choose.click()
driver.quit()

#Opening BrowserStack and clicking on pricing and toggling price - Safari

driver = webdriver.Safari()
driver.get("https://www.browserstack.com/")
driver.maximize_window()

print(driver.title)
time.sleep(3)
link = driver.find_element(By.LINK_TEXT,'Pricing')
link.click()
time.sleep(3)
btn = driver.find_element(By.CLASS_NAME,'switch-wrap')
btn.click()
time.sleep(3)

choose = driver.find_element(By.XPATH,'//*[@id="live-plans"]/div[1]/div[5]/div/div[2]/div[6]/form/input[1]')
choose.click()
driver.quit()
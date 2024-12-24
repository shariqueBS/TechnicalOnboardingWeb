from selenium import webdriver
from selenium.webdriver.common.by import By
import time

grid_url = "http://localhost:4444"

#Opening BrowserStack, clicking on pricing and chosing monthly desktop plan - Firefox

options = webdriver.ChromeOptions()
assert options.capabilities['browserName'] == 'chrome'
driver = webdriver.Remote(command_executor=grid_url, options=options)

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

#Opening BrowserStack, clicking on pricing and chosing monthly desktop plan - Firefox

options = webdriver.FirefoxOptions()
assert options.capabilities['browserName'] == 'firefox'
driver = webdriver.Remote(command_executor=grid_url, options=options)

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

#Opening BrowserStack, clicking on pricing and chosing monthly desktop plan - Safari

options = webdriver.SafariOptions()
assert options.capabilities['browserName'] == 'safari'
driver = webdriver.Remote(command_executor=grid_url, options=options)

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


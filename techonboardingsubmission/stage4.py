import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


def test_checkout_chrome():

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

    if driver.capabilities['browserName'].lower() == 'safari' :
        assert driver.title == 'BrowserStack Pricing | Plans Starting From Just $12.50 A Month'
    else :
        assert driver.title == 'Checkout'
    
    driver.quit()

def test_checkout_firefox():

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

    if driver.capabilities['browserName'].lower() == 'safari' :
        assert driver.title == 'BrowserStack Pricing | Plans Starting From Just $12.50 A Month'
    else :
        assert driver.title == 'Checkout'
    
    driver.quit()

def test_checkout_safari():

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

    choose = driver.find_element(By.XPATH,'/html/body/main/div[4]/div[3]/div/div[2]/div[2]/div[1]/div[5]/div/div[2]/div[6]')
    choose.click()

    if driver.capabilities['browserName'].lower() == 'safari' :
        assert driver.title == 'BrowserStack Pricing | Plans Starting From Just $12.50 A Month'
    else :
        assert driver.title == 'Checkout'
    
    driver.quit()

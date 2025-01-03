import pytest
from selenium.webdriver.common.by import By
import time

def test_checkout(selenium):
    selenium.get('https://www.browserstack.com')

    selenium.maximize_window()
    print(selenium.title)
    time.sleep(3)
    link = selenium.find_element(By.LINK_TEXT,'Pricing')
    link.click()
    time.sleep(3)
    btn = selenium.find_element(By.CLASS_NAME,'switch-wrap')
    btn.click()
    time.sleep(3)
    btn.click()
    time.sleep(3)

    #negative test case
    assert selenium.title != 'Live for teams page | BrowserStack'

    choose = selenium.find_element(By.XPATH,'/html/body/main/div[4]/div[3]/div/div[2]/div[2]/div[1]/div[5]/div/div[2]/div[6]')
    choose.click()
    time.sleep(3)

    #positive test case
    assert selenium.title == 'Checkout'

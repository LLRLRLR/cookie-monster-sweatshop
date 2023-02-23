from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get("http://orteil.dashnet.org/experiments/cookie/")

def get_money():
    money = int(driver.find_element(By.ID, 'money').text.replace(',', ''))
    return money

def click():
    cookie = driver.find_element(By.ID, 'cookie')
    cookie.click()

def get_prices():
    store = driver.find_elements(By.CSS_SELECTOR, '#store b')
    all_items = [item.text for item in store if item.text != '']
    pattern = re.compile(r'([^-]+) - ([\d,]+)')
    price_dict = {
        pattern.match(item).group(1).replace(" ", ""): int(pattern.match(item).group(2).replace(",", "")) 
        for item in all_items
        }
    return pd.Series(price_dict)

def buy_powerups(data_lst: list ,data_money: int):
    affordable = data_lst[data_lst <= data_money]
    if not affordable.empty:
        item_id = "buy" + affordable.index[-1]
        item = driver.find_element(By.ID, item_id)
        item.click()    
      


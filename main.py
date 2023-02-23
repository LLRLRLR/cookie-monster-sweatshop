from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from functions import get_money, click, get_prices, buy_powerups


game_is_on = True
timeout = 15
while game_is_on:
    if time.time() > timeout:
        current_money = get_money()
        current_price = get_prices()
        buy_powerups(current_price, current_money)
        timeout = time.time() + 5
    else:
        click()
        
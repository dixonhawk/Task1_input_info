from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
import pyautogui

name_file_screen = 'Screenshot.png'

def creation():
    df = pd.read_excel('challenge.xlsx')
    list_df = df.values.tolist()
    for i in list_df:
        input_info(i)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get('https://www.rpachallenge.com/')

assert driver.current_url == 'https://www.rpachallenge.com/', 'Ошибка, не корректный адрес сайта'

def input_info(input_list):
    start_button = driver.find_element('class name','btn-large.uiColorButton')
    first_name = driver.find_element('xpath', '//*[@ng-reflect-name="labelFirstName"]')
    last_name = driver.find_element('xpath', '//*[@ng-reflect-name="labelLastName"]')
    company_name = driver.find_element('xpath', '//*[@ng-reflect-name="labelCompanyName"]')
    role_company = driver.find_element('xpath', '//*[@ng-reflect-name="labelRole"]')
    address = driver.find_element('xpath', '//*[@ng-reflect-name="labelAddress"]')
    email = driver.find_element('xpath', '//*[@ng-reflect-name="labelEmail"]')
    phone = driver.find_element('xpath', '//*[@ng-reflect-name="labelPhone"]')
    submit_button = driver.find_element('class name', 'btn.uiColorButton')

    start_button.click()
    first_name.click()
    first_name.send_keys(input_list[0])
    last_name.click()
    last_name.send_keys(input_list[1])
    company_name.click()
    company_name.send_keys(input_list[2])
    role_company.click()
    role_company.send_keys(input_list[3])
    address.click()
    address.send_keys(input_list[4])
    email.click()
    email.send_keys(input_list[5])
    phone.click()
    phone.send_keys(input_list[6])
    submit_button.click()
    return

creation()
time.sleep(3)
pyautogui.screenshot().save(name_file_screen)
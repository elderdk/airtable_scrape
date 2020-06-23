import os
import time
import glob
import sys
import datetime
import pandas as pd
import subprocess
from . import excel
from . import parse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


def main(url, fname, wait_time = 1, sheet_name = 'Sheet1', headless = True):
        
    dirname = os.path.dirname(os.path.realpath(__file__))

    chromedriver = os.path.join(dirname, 'chromedriver.exe')

    options = Options()
    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    options.add_argument("user-agent={userAgent}")
    options.headless = headless
    driver = webdriver.Chrome(chromedriver, options=options)

    excel_file = excel.make_file(dirname, fname)
    excel_full_path = os.path.join(dirname, fname)

#access the websitse
    print('Opening the website...')
    driver.get(url)

#wait until the login page is loaded
    try:
        print('accessed')

        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.expandButtonLeft')))
        expand_first_row = driver.find_element_by_css_selector(".expandButtonLeft")
        expand_first_row.click()

        time.sleep(1)

        next_button = ActionChains(driver).key_down(Keys.LEFT_CONTROL).key_down(Keys.LEFT_SHIFT).send_keys('.')
        select_count = driver.find_element_by_css_selector(".selectionCount")
        select_count = select_count.get_attribute("innerHTML").split(' ')[0]


        with pd.ExcelWriter(path=excel_full_path, mode='w') as writer:
            # for i in range(select_count):
            for i in range(10): #This is for test
                
                data, labels = parse.make_data(driver.page_source)
                df = pd.DataFrame(data=data, index=[i], columns=labels)

                print(f"{i+1} / {int(select_count)}", flush = True)

                next_button.perform()

                if i == 0:
                    header = True
                    startrow = 0
                else:
                    header = False
                    startrow = i+1

                df.to_excel(writer, startrow=startrow, header=header, index=False, sheet_name = sheet_name)

                time.sleep(wait_time)

    finally:
        os.startfile(excel_full_path)
        driver.close()
        print('Driver closed')
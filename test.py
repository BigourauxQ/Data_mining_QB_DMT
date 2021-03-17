from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd# specify the url

options = Options()
options.add_argument('--headless')
#options.add_argument('--disable-gpu')  # maybe needed if running on Windows.

urlpage = 'https://www.kaggle.com/vishalsubbiah/pokemon-images-and-types' 
print(urlpage)
# run firefox webdriver from executable path of your choice
driver = webdriver.Chrome(chrome_options=options)
# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(10)
# driver.quit()
results = driver.find_elements_by_class_name("mdc-menu-surface--anchor")
print('Number of results', len(results), results[0].find_element_by_tag_name('div'))
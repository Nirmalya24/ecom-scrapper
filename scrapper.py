from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import time

path = '/Users/nirmalya/Downloads/chromedriver'
chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument("--window-size=1920,1200")
chrome_options.add_argument(' -- incognito')
browser = webdriver.Chrome(path, options=chrome_options)
browser.get('https://walmart.com')
down_arrow = browser.find_element_by_xpath('//*[@id="global-search-dropdown-toggle"]/span/img')
search_button = browser.find_element_by_xpath('//*[@id="global-search-submit"]/span/img')


print(browser.page_source)
browser.quit()


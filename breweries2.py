import time
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/Users/Nealy/Documents/web-apps-2/scraping/chromedriver')
driver.get('https://www.brewersassociation.org/directories/breweries/');

# page_source is a variable created by Selenium - it holds all the HTML
html = driver.page_source

#the code clicks the x button that closes the pop up box
driver.find_element_by_xpath("//div[@class='modal-body']//button[@class='close']").click()

# it is necessary to wait so the page loads so it allows me to click on the list in the next step
time.sleep(10)

#the code below clicks on the United States in the drop down menu
driver.find_element_by_xpath("//li[@id='country']").click()
driver.find_element_by_xpath("//li[@data-country-id='United States']").click()

#code below waits for the list of breweries to load/be visible before it starts executing BeautifulSoup
#don't forget to import By if you want to use this again in the future
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"status-bar")))

#start BeautifulSoup code
#added this sleep because I thought that BeautifulSoup might be scraping quicker than the information loaded
time.sleep(5)

bsObj = BeautifulSoup(html, "html.parser")



#Prof McAdams: Sorry for the weird names.
list2 = bsObj.find("div", {"class":"entry"})
cookie = list2.find("div", {"id":"ajax-content"})

print(cookie)

#driver.quit()

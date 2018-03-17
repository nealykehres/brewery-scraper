import time
import csv
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import shutil

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

# bsObj = BeautifulSoup(html, "html.parser")
innerHTML = driver.execute_script("return document.body.innerHTML")
bsObj = BeautifulSoup(innerHTML, "html.parser")


brewery_boxes = bsObj.findAll("div", {"class":"brewery"})

#this function goes through all of the brewery boxes and finds the information for each brewery then adds it to a list.

url_list = []

def get_info(brewery):

    name = brewery.find("li", {"class":"name"}).get_text()
    address = brewery.find("li", {"class":"address"}).get_text()
    city = brewery.find("li", {'class': None}).get_text()
    brewery_type = brewery.find("li", {"class":"brewery_type"}).get_text()
    try:
        url = brewery.find("li", {"class":"url"}).find("a")["href"]
    except AttributeError:
        url = brewery.find("li", {"class":"url"})
    #url_boxes = bsObj.findAll("li", {"class":"url"}).find("a")["href"]
    #for url in url_boxes:
        #url_list.append(url.find("a")["href"])

    brewery_list = [name, address, city, brewery_type, url]
    return brewery_list

#needed to write a new function in order to append the URLS to a list
def get_list(links):
    try:
        url = brewery.find("li", {"class":"url"}).find("a")["href"]
    except AttributeError:
        url = brewery.find("li", {"class":"url"})
    url_list.append(url)
    #print(url_list)

#now write the info to the csv file and append to the url list
breweries_file = open('breweries_file.csv', 'w')
writer = csv.writer(breweries_file)
writer.writerow(("brewery", "address", "city", "type", "url"))
for brewery in brewery_boxes[:100]:
    writer.writerow(get_info(brewery))
    get_list(brewery)
    #url_list.append(brewery.findAll("li", {"class":"url"}))

breweries_file.close()

#now get screenshots
for url in url_list:
    date_stamp = str(datetime.datetime.now()).split('.')[0]
    date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
    file_name= date_stamp + ".png"
    try:
        driver.get(url)
        driver.get_screenshot_as_file(file_name)
        #move file to external hardrive
        shutil.move(file_name, "/Volumes/My Passport for Mac/brewerypics")
    #sleep 1 second just to make sure each file name is unique.
        time.sleep(1)
    except:
        print("None available")

driver.close()

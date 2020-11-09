from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import urllib.request
from selenium.webdriver.support.ui import Select
import os

def downloadImages(urls, folder):

    try:
        os.mkdir(folder)
    except OSError:
        print ("Creation of the directory %s failed" % folder)
        return
    else:
        print ("Successfully created the directory %s " % folder)
        
    count = 0
    for url in urls:
        f = open(folder + "/" + str(count) + ".png",'wb')
        f.write(urllib.request.urlopen(url).read())
        f.close()
        count = count + 1

def getImageUrls(url):
    driver = webdriver.Safari()
    driver.get(url)

    try:
        filter = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "select[id=category-filter]"))
        )
    finally:
        #print(filter.text)
        
        select = Select(driver.find_element_by_id('category-filter'))
        select.select_by_value('1')
        
#        driver.implicitly_wait(1) # seconds
        


    imageURLs = []

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=card-container-image]"))
        )
    finally:


        divs = driver.find_elements_by_css_selector("div[id*=card-profile]")
        
        for div in divs:
            try:
                image = div.find_element_by_xpath("./a/div/div[2]/div[@class='card-container-image']/img")
                source = image.get_attribute("src")
                print(source)
                imageURLs.append(source)
            except:
                div.send_keys(Keys.PAGE_DOWN);
                try:
                    image = div.find_element_by_xpath("./a/div/div[2]/div[@class='card-container-image']/img")
                    source = image.get_attribute("src")
                    print(source)
                    imageURLs.append(source)
                except:
                    print("Couldn't get it")
                

        driver.close()


    print(imageURLs)
    return imageURLs
    
#'ESTJ', 'ESFJ', 'ISTP', 'ISFP', 'ESTP', 'ESFP', 'INTJ', 'INTP', 'ENTJ', 'INFJ', 'INFP', 'ENFJ', 'ENFP'
types = ['ESTP', 'ESFP', 'INTJ', 'INTP', 'ENTJ', 'INFJ', 'INFP', 'ENFJ', 'ENFP']

for index, type in enumerate(types):

    adjusted_index = index + 1
    url = 'https://www.personality-database.com/mbti-type/' + str(adjusted_index) + '/' + type
    
    imageURLs = getImageUrls(url)

    downloadImages(imageURLs, type)


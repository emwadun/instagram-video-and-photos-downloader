'''
* Here we need to achieve the following:
    1. Log into instagram account
    2. Seach 'Mikel Artetas' Instagram account
    3. Download the posts / photos
    4. Close the browser

* We need to install selenium and wget libraries in our virtual environment activated called 'instaapp':
#pip install selenium
#pip install wget

* My laptop also has chromedriver installed: https://chromedriver.chromium.org/
MAKE SURE YOU HAVE STARTED CHROMEDRIVER.exe or specify its path in the driver variable that 
you set below

'''
from ast import keyword
from selenium import webdriver
from selenium.webdriver.common.keys  import Keys
import os
import wget

keyword = 'Arteta'
images_href = []

#I am specifying the chromedriver that is in my 
driver = webdriver.Chrome()

def launchInstragramInBrowser():
    driver.get('https://www.instagram.com')
    driver.implicitly_wait(10)

    #lets click on the button to accept all cookies
    driver.find_element_by_xpath('/html/body/div[4]/div/div/button[2]').click()

def instagramLogin():
    #Lets supply Instagram username and password for automation. We dont want to hardcode the values for security reasons.
    username = input("Enter username: ")
    password = input("Enter password: ")

    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()

    #lets dismiss the message to save the password that shows up on the screen. It did not work
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()

def turnOffInstagramNotificitations():
    #also lets dismiss message to turn on instagram notifications
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()   

def searchInstagramAccount():
    #Now lets search a 'mikelarteta' Instagram account
    #we can also use input() function to avoid hardcoding. Hardcoding here is just for test purposes
    driver.implicitly_wait(10)
    searchword = 'mikelarteta'
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(searchword)


def clickOnFirstSearchResult():
    #now lets click on the first result to go to the Instagram account
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()


def findAndPrintImages():
    images = driver.find_elements_by_class_name("_bz0w")

    for img in images:
        href = img.find_element_by_tag_name("a").get_attribute("href")
        images_href.append(href)

    print(images_href)

def createDirectory():
    #Lets create a directory named Arteta_pics on our computer for us to use to store images.
    global path
    path = os.getcwd()
    path = os.path.join(path, keyword + "_pics")    
    #lets create the folder if it doesnt exist:
    if not os.path.exists(path):
        os.mkdir(path)


def downloadImages():
    counter = 0
    for image in images_href:
        save_as = os.path.join(path, keyword + str(counter) + '.jpg')
        wget.download(image, save_as)
        counter += 1

    driver.implicitly_wait(20)
    driver.close()


def instagramAutoMainFunction():
    #ORDER OF EXECUTION
    #1:
    launchInstragramInBrowser()

    #2:
    instagramLogin()

    #3:
    turnOffInstagramNotificitations()

    #4:
    searchInstagramAccount()

    #5:
    clickOnFirstSearchResult()

    #6:
    findAndPrintImages()

    #7:
    createDirectory()

    #8:
    downloadImages()


#Here we now call the main function that wraps all the 8 functions. We can call it in Flask now !
instagramAutoMainFunction()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
from csv import writer

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

argumentArray = {'London', 'Istanbul', 'Amsterdam', 'Prague', 'Paris', 'Berlin', 'Munich', 'Moscow', 'Ibiza', 'Bangkok', 'Hvar', 'Marmaris', 'St. Petersburg', 'Dublin', 'Madrid', 'Barcelona', 'Rome', 'Milan', 'Stockholm', 'Brighton', 'Athens', 'Venice', 'New York City' , 'San Francisco', 'Miami'}

#https://www.tripadvisor.co.uk/Search?geo=1&searchNearby=&pid=3826&redirect=&startTime=1563560694952&uiOrigin=MASTHEAD&q=London&supportedSearchTypes=find_near_stand_alone_query&enableNearPage=true&returnTo=https%253A__2F____2F__www__2E__tripadvisor__2E__co__2E__uk__2F__Home__2D__g1&searchSessionId=AC98737AF729E0BC4B32BDFD46A864861563560612163ssid&social_typeahead_2018_feature=true&sid=AC98737AF729E0BC4B32BDFD46A864861563560698089&rf=1

firstPartLink = "https://www.tripadvisor.co.uk/Search?geo=1&searchNearby=&pid=3826&redirect=&startTime=1563560694952&uiOrigin=MASTHEAD&q="
secondPartLink = "&supportedSearchTypes=find_near_stand_alone_query&enableNearPage=true&returnTo=https%253A__2F____2F__www__2E__tripadvisor__2E__co__2E__uk__2F__Home__2D__g1&searchSessionId=AC98737AF729E0BC4B32BDFD46A864861563560612163ssid&social_typeahead_2018_feature=true&sid=AC98737AF729E0BC4B32BDFD46A864861563560698089&rf=1"

browser = webdriver.Chrome()

with open('richCityData.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['city', 'popularity', 'description', 'image']
    csv_writer.writerow(headers) # write headers first.

    for i in argumentArray:

        link = firstPartLink + i + secondPartLink
        browser.get(link)
        sleep(5)

        title = browser.find_elements_by_xpath("//div[@class='result-title']")
        popularityElement = browser.find_elements_by_xpath("//div[@class='review-count']")

        city = ''
        popularity = ''
        descToWrite = ''
        imgUrl = ''

        if title:
            city = title[0].text
        else:
            continue

        if popularityElement:
            popularity = popularityElement[0].text

        title[0].click()
        sleep(2)

        root_window = browser.window_handles[0]
        opened_window = browser.window_handles[1]

        browser.switch_to.window(opened_window)
        sleep(5)

        description = browser.find_elements_by_xpath("//div[@class='common-text-ReadMore__content--2X4LR']")

        if description:
            descToWrite = description[0].text

        imgElement = browser.find_elements_by_xpath("//img[@class='home_img']")

        if imgElement:
            imgUrl = imgElement[0].get_attribute("src")
        else:
            secondAttemptElement = browser.find_elements_by_xpath("//div[@class='homepage-homepage-hero-HomepageHero__hero--2vsJc']")
            if secondAttemptElement:
                url = secondAttemptElement[0].get_attribute("style")
                imgUrl = url.split('(', 1)[1].split(')')[0]

        browser.close()
        sleep(2)
        browser.switch_to.window(root_window)

        csv_writer.writerow([city, popularity, descToWrite, imgUrl])

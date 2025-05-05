from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


response=requests.get("https://appbrewery.github.io/Zillow-Clone/")
zillow_web_page=response.text
soup=BeautifulSoup(zillow_web_page,"html.parser")

#links:
links=soup.select(".StyledPropertyCardDataWrapper a")
link_list=[link.get("href") for link in links]
for link in link_list:
    print(link)

# #prices:
prices=soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
prices_list=[price.text.split("/")[0].split("+")[0] for price in prices]
for price in prices_list:
    print(price)

#address:
addresses=soup.find_all("address")
addresses_list=[addresse.text.strip() for addresse in addresses]
for address in addresses_list:
    print(address)

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScfDakyAQ-3kX2qIA93MuQSoI4lM-BIwRN7lGxCZUR5RcNt2A/viewform?usp=sf_link")




count=0
while count < len(prices_list):
    time.sleep(1)
    address_field = driver.find_element(By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    price_field = driver.find_element(By.XPATH,
                                      value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field = driver.find_element(By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    time.sleep(1)
    address_field.click()
    address_field.send_keys(link_list[count])

    price_field.click()
    price_field.send_keys(addresses_list[count])

    link_field.click()
    link_field.send_keys(prices_list[count])

    submit_button=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScfDakyAQ-3kX2qIA93MuQSoI4lM-BIwRN7lGxCZUR5RcNt2A/viewform?usp=sf_link")

    count=count+1
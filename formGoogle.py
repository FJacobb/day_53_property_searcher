import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Form:
    def __init__(self):
        self.driver = webdriver.Chrome("c:/Users/festu/OneDrive/Documents/chromedriver.exe")
    def adds(self, data):
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfSo2bk_y6IovyKdDYEujJXsdpHyenRbAVx2XnkOAz1QwNBPQ/viewform")
        time.sleep(4)
        address = self.driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        address.send_keys(data["add"])
        price = self.driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        price.send_keys(data["price"])
        link = self.driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        link.send_keys(data["link"])
        self.driver.find_element(By.XPATH,value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span").click()
        time.sleep(2)
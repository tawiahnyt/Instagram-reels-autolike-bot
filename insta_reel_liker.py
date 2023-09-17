from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time


class InstaLikes:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('https://instagram.com/')
        time.sleep(15)
        print('Success')

    def validation(self):
        try:
            save_login = self.driver.find_element(By.XPATH, '//div[text()="Not Now"]')
            save_login.click()
            time.sleep(5)
        except selenium.common.exceptions.NoSuchElementException:
            pass
        try:
            notification = self.driver.find_element(By.XPATH, '//button[text()="Not Now"]')
            notification.click()
            time.sleep(5)
        except selenium.common.exceptions.NoSuchElementException:
            pass
        print('validation successful')

    def login(self, user, pass_w):
        username = self.driver.find_element(By.NAME, 'username')
        username.send_keys(user)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(pass_w)
        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login.click()
        time.sleep(5)
        print('login successful')

    def load_reels(self):
        self.validation()
        time.sleep(5)
        reels = self.driver.find_element(By.XPATH, '//*[contains(text(),"Reels")]')
        reels.click()
        time.sleep(5)
        print('reels loaded')
        print('proceeding to liking reels')

    def like_reels(self):
        reels = self.driver.find_elements(By.XPATH, '//*[text()="Like"]//ancestor::span[1]')
        print(len(reels))
        for reel in reels:
            try:
                reel.click()
                print('reels liked successfully')
                # reel.send_keys(Keys.DOWN)
                # Keys.DOWN.click()
                time.sleep(1)
            except selenium.common.exceptions.NoSuchElementException:
                pass
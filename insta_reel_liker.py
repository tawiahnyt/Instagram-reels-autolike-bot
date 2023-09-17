# Import the Selenium WebDriver
from selenium import webdriver

# Import the By class to find elements by their ID, class name, etc.
from selenium.webdriver.common.by import By

# Import the exceptions module to catch exceptions
import selenium.common.exceptions

# Import the time module to wait for elements to appear
import time


class InstaLikes:

    def __init__(self):
        # Create a Firefox browser instance
        self.driver = webdriver.Firefox()
        # Maximize the browser window
        self.driver.maximize_window()
        # Navigate to the Instagram home page
        self.driver.get('https://instagram.com/')
        # Wait for 15 seconds for the page to load
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
        # Find the username element
        username = self.driver.find_element(By.NAME, 'username')
        # Send the username to the field
        username.send_keys(user)
        # Find the password element
        password = self.driver.find_element(By.NAME, 'password')
        # Send the password to the field
        password.send_keys(pass_w)
        # Find the login button
        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        # Click the login button
        login.click()
        # Wait for 5 seconds
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
        # Find reels by looking for the text "Like" and then finding the parent span of the element
        reels = self.driver.find_elements(By.XPATH, '//*[text()="Like"]//ancestor::span[1]')
        # Print the number of reels found
        print(len(reels))
        # Loop through each reel and try to click it
        for reel in reels:
            try:
                reel.click()
                print('reels liked successfully')
                time.sleep(1)
            # If an exception is thrown, just pass and continue
            except selenium.common.exceptions.NoSuchElementException:
                pass
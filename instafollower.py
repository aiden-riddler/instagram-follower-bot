import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
chrome_driver_path = '/home/aiden/Documents/chromedriver/chromedriver'
SIMILAR_ACCOUNT = '_b.e.tt.u1'
USERNAME = '_be.tt.u_'
PASSWORD = 'Clover4'


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get('https://www.instagram.com')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(USERNAME)
        self.driver.find_element_by_name('password').send_keys(PASSWORD)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

    def find_followers_updated(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(5)
        followers = self.driver.find_element(By.CSS_SELECTOR, 'ul li:nth-of-type(3) a')
        followers.click()

        time.sleep(5)
        modal = self.driver.find_elements(By.CSS_SELECTOR, 'ul')[2].find_element(By.XPATH, './..')
        for i in range(30):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(4)

    def find_followers(self):
        sleep(5)
        search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(SIMILAR_ACCOUNT)
        search.send_keys(Keys.ENTER)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()
        time.sleep(6)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/ul/div/li[2]/div/div[3]/button').click()
        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]').click()

    def follow_updated(self):
        print("Following")
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'ul')[2].find_elements(By.CSS_SELECTOR, 'li button')
        for btn in all_buttons:
            try:
                btn.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                self.driver.find_element(By.XPATH, '//button[text()="Cancel"]').click()

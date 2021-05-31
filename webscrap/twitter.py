from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class TwitterBot(object):

    driver = None
    texts = ['']

    @staticmethod
    def main():
        driver = webdriver.Chrome()
        driver.get('https://twitter.com/?lang=en')
        driver.find_element_by_xpath("//a[@href='/login']")
        # driver.find_element_by_xpath('//a[@href="/explore"]').click()

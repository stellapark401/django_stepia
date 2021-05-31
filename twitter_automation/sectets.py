from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options


def get_credentials() -> dict:
    credentials = {}
    with open('credentials.txt') as fh:
        for line in fh.readlines():
            try:
                k, v = line.split(': ')
            except ValueError:
                print('fill out the credential in the file.')
                exit(0)
            credentials[k] = v.rstrip(' \n')
    return credentials


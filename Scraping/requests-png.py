'''
Created on 2021. 6. 5.

@author: pjh
'''

from selenium.webdriver import Firefox, FirefoxOptions

url = "http://www.naver.com/"

options = FirefoxOptions()
options.add_argument('-headless')

browser = Firefox(options=options)

browser.get(url)

browser.save.screenshot("Website.png")

browser.quit()


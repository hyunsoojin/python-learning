'''
Created on 2021. 6. 5.

@author: pjh
'''


from selenium.webdriver import Firefox, FirefoxOptions

options = FirefoxOptions()
options.add_argument('-headless')
browser = Firefox(options=options)

browser.get("https://google.com")

r = browser.execute_script("return 100 + 50")
print(r)
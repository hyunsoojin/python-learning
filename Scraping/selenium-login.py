'''
Created on 2021. 6. 5.

@author: pjh
'''

from selenium.webdriver import Chrome, ChromeOptions

USER = "jhs7251"
PASS = "!lozza245800"

options = ChromeOptions()
#options.add_argument('-headless')
browser = Chrome(options=options)

url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print("로그인 페이지에 접근합니다.")

e = browser.find_element_by_id("id")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("pw")
e.clear()
e.send_keys(PASS)

form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()
print("로그인 버튼을 클릭합니다.")


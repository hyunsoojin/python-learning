'''
Created on 2021. 6. 5.

@author: pjh
'''

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

USER = "jhs7251"
PASS = "!lozza24580"

session = requests.session()
login_info = {
    "m_id" : USER,
    "m_passwd" : PASS
}

url_login = "https://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info)
res.raise_for_status()

url_mypage = "https://www.hanbit.co.kr/myhanbit/myhanbit.html"
res= session.get(url_mypage)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
mileage = soup.select_one(".mileage_section1 span").getText()
ecoin = soup.select_one(".mileage_section2 span").getText()

print("마일리지: ", mileage)
print("이코인: " , ecoin)
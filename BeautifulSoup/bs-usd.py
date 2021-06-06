'''
Created on 2021. 6. 5.

@author: pjh
'''

from bs4 import BeautifulSoup

import urllib.request as req

url = "https://finance.naver.com/"
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

price = soup.select_one("#content > div.article2 > div.section1 > div.group1 > table > tbody > tr.up.bold > td:nth-child(2)").string

print("usd/krw =", price)


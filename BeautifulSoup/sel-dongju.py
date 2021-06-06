'''
Created on 2021. 6. 5.

@author: pjh
'''

from bs4 import BeautifulSoup
import urllib.request as req

url = "https://ko.wikipedia.org/wiki/%EC%9C%A4%EB%8F%99%EC%A3%BC#%EC%9E%91%ED%92%88"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

a_list = soup.select("#mw-content-text > div.mw-parser-output > ul:nth-child(50) > li")

for a in a_list:
    name = a.text
    print("-", name)
    
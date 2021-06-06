'''
Created on 2021. 6. 5.

@author: pjh
'''

from bs4 import BeautifulSoup

fp = open("fruits-vegitables.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

li_list = soup.select("li")


print(soup.select_one("li:nth-of-type(8)").text)
print(soup.select_one("#ve-list > li[data-lo='us']")[1].text)
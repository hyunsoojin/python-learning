'''
Created on 2021. 6. 5.

@author: pjh
'''

import requests
r = requests.get("http://api.aoikujira.com/time/get.php")

text = r.text
print(text)

bin = r.content
print(bin)

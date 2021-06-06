'''
Created on 2021. 6. 6.

@author: pjh
'''

import json

price = {
        'data': '2018-05-10',
        "price": {
            "Apple": 80,
            "Orange": 55,
            "Banana": 40
        }}

s = json.dumps(price)
print(s)
'''
Created on 2021. 6. 6.

@author: pjh
'''

import scrapy

class Book1Spider(scrapy.Spider):
    name = 'book'
    
    start_url=[
            'https://wikibook.co.kr/list/'
    ]
    
    def parse(self, response):
        title = response.css('title')
        print(title.extract())

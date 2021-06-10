'''
Created on 2021. 6. 8.

@author: User
'''

from konlpy.tag import Okt

okt = Okt()
malist = okt.pos("아버지 가방에 들어가신다.", norm=True, stem=True)
print(malist)

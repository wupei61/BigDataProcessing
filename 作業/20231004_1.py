# -*- coding: utf-8 -*-
"""20231004-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/170xs_qCavXFkvJA039llmR88Lj7uDL5j
"""

import requests
 from bs4 import BeautifulSoup
 url = 'http://ehappy.tw/bsdemol.htm'
 html = requests.get(url)
 html.encoding = 'UTF-8'
 sp = BeautifulSoup(html.text, 'lxml')
 print(sp.title)
 print(sp.title.text)
 print(sp.hl)
 print(sp.p)
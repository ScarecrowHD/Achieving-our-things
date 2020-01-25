# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 10:45:59 2020

@author: Chens
"""

import re
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import time


'''daily hotpoint ranking'''

url = 'https://s.weibo.com/top/summary'
headers={
    	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

hotpoint = requests.get(url, headers=headers)
info = BeautifulSoup(hotpoint.text, 'lxml')   ### 获取网页链接
title = info.find_all('td', {'class': 'td-02'})   ##获取热搜标题
rank = info.find_all('td', {'class': 'td-01 ranktop'})  ##获取热搜排名

pattern1 = re.compile('target="_blank"(.*?)<\/a>\s*<span>(\d*)<\/span>')
title_info = re.findall(pattern1, str(title))
pattern2 = re.compile('<td class="td-01 ranktop">(\d*)<\/td>')
rank_data = re.findall(pattern2, str(rank))

curtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))    
data_lst = []

for i in range(len(title_info)):
    temp = []
    temp.append(title_info[i][0].strip('>'))
    temp.append(int(title_info[i][1]))
    temp.append(int(rank_data[i]))
    data_lst.append(temp)



        
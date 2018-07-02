# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 11:50:00 2018


第四题：求出未来5天天气
1.打印每天的6:00,12:00,18:00的天气(城市,温度，情况，气压，最高温度，最低温度)
2.同上写出[英文版的]
3.根据天气的情况，给出建议：例如，今天下雨，提示带伞。今天温度高，穿衬衫...三个件以上
4.根据温度打印出问题折线图
    28——————————————————————————————
    30——————————————————————————————————
    10——————————————————
5.打印出其他10个城市的天气，计算出天气排名，按着大到小的顺序。

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》list列表-》index 0 字典-》main字典-》temp变量
city=data['city']['name']
temp=data['list'][8]['main']['temp']
pre=data['list'][8]['main']['pressure']
temp_max=data['list'][8]['main']['temp_max']
temp_min=data['list'][8]['main']['temp_min']
time=data['list'][8]['dt_txt']
tqqk=data['list'][8]['weather'][0]['description']
print('日期：{}'.format(time),'城市：{}'.format(city),'天气情况：{}'.format(tqqk),
      '温度：{}'.format(temp),'气压：{}'.format(pre),
      '最高温：{}'.format(temp_max),'最低温：{}'.format(temp_min))

 city=data['city']['name']
 n=15
 i=8
 while n>0 :
     if n%3==2 : 
         
      
for i in ['8''11''14''17']:
temp=data['list'][i]['main']['temp']
pre=data['list'][i]['main']['pressure']
temp_max=data['list'][i]['main']['temp_max']
temp_min=data['list'][i]['main']['temp_min']
time=data['list'][i]['dt_txt']

print('日期：{}'.format(time),'城市：{}'.format(city),
      '温度：{}'.format(temp),'气压：{}'.format(pre),
      '最高温：{}'.format(temp_max),'最低温：{}'.format(temp_min))



   
    


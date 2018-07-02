# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 09:45:15 2018
题目十五：未来三天 天气类天气对象
1.定义一个天气类Weather 静态的属性(temp,description,pre) 动态属性(msg打印当前天气属性)
2.创建3天的天气对象，并调用msg方法



@author: Administrator
"""

class Weather:
    def __init__(self,temp,description,pre):
        self.temp=temp
        self.description=description
        self.pre=pre
    def msg(self):
        print('今天的温度是：{}\t天气描述：{}\t气压：{}'.format(self.temp,self.description,self.pre))
a=Weather('20','晴','500')
b=Weather('25','晴','600')
c=Weather('28','晴','700')
a.msg()
b.msg()
c.msg()


#----------------跟联网数据融合------------------------

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
class Weather:
    def __init__(self,data,temp,description,pre):
        self.data=data
        self.temp=temp
        self.description=description
        self.pre=pre
    def msg(self):
        print('今天的日期是：{}，今天的温度是：{}\t天气描述：{}\t气压：{}'.format(self.data,self.temp,self.description,self.pre))
for i in range(len(data['list'])):
    rq=data['list'][i]['dt_txt']
    temp=data['list'][i]['main']['temp']
    pressure=data['list'][i]['main']['pressure']
    description=data['list'][i]['weather'][0]['description']
    aa=Weather(rq,temp,description,pressure)#跟函数的调用是一样的吧
    aa.msg()
    
    
    
    
#-----------------------------------------------------------------------
'''

题目十六：高考派2300数据统计
1.根据2300下载的两百多M文件，统计招生总人数
2.统计7各地域的人数各是多少
3.计算比例

'''
import json
rs=open('./rstrue.txt','r')
rs=rs.readlines()
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
u=0
j=0
l=0
m=0
o=0
p=0
sum=0
for line in rs:   
    dddd=json.loads(line)
    if dddd['status']==1:
        for i in range(len(dddd['data'])):
            city=dddd['data'][i]['city']
            v=dddd['data'][i]['sub_type']
            z=dddd['data'][i]['plan']
            if city=='黑龙江'or city=='吉林'or city=='辽宁':
                if v=='1':
                    a +=int(z)
                else:
                    b +=int(z)
            elif city=='福建'or city=='江西'or city=='山东'or city=='上海'or city=='江苏'or city=='浙江'or city=='安徽':
                if v=='1':
                    c +=int(z)
                else:
                    d +=int(z)
            elif city=='河南'or city=='湖北'or city=='湖南':
                if v=='1':
                    e +=int(z)
                else:
                    f +=int(z)
            elif city=='广东'or city=='广西'or city=='海南':
                if v=='1':
                    g +=int(z)
                else:
                    h +=int(z)     
            elif city=='四川'or city=='贵州'or city=='云南'or city=='重庆'or city=='西藏':
                if v=='1':
                    u +=int(z)
                else:
                    j +=int(z)                     
            elif city=='北京'or city=='天津'or city=='山西'or city=='河北'or city=='内蒙古':
                if v=='1':
                    l +=int(z)
                else:
                    m +=int(z)                    
            elif city=='陕西'or city=='甘肃'or city=='青海'or city=='宁夏'or city=='新疆':
                if v=='1':
                    o +=int(z)
                else:
                    p +=int(z)                                      
        sum=a+b+c+d+e+f+g+h+u+j+l+m+o+p
        
print('东北文科:{}\t东北理科：{}\t东北总人数：{}'.format(a,b,a+b))
print('华东文科:{}\t华东理科：{}\t华东总人数：{}'.format(c,d,c+d))
print('华中文科:{}\t华中理科：{}\t华中总人数：{}'.format(e,f,e+f))
print('华南文科:{}\t华南理科：{}\t华南总人数：{}'.format(g,h,g+h))
print('西南文科:{}\t西南理科：{}\t西南总人数：{}'.format(u,j,u+j))
print('华北文科:{}\t华北理科：{}\t华北总人数：{}'.format(l,m,l+m))
print('西北文科:{}\t西北理科：{}\t西北总人数：{}'.format(o,p,o+p))

print('招生总人数：{}'.format(sum))  




#----------------------------------------




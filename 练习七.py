# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 12:55:01 2018
练习七:全球天气未来3天
1.使用多选其一，完成天气的提醒
2.一定要多ci使用到for循环,偶尔用一次while循环
3.初步学会使用debug，知道里面的设置断点，下一步执行，下一个断点执行。
4.《闪屏的制作》进入我们天气程序的时候，有一个温馨图形的提示。使用循环实现，
  要知道是什么意思，照抄网上代码不行。
@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)

for i in range(21):
   city=data['city']['name']
   temp=data['list'][i]['main']['temp']
   pre=data['list'][i]['main']['pressure']
   temp_max=data['list'][i]['main']['temp_max']
   temp_min=data['list'][i]['main']['temp_min']
   time=data['list'][i]['dt_txt']
   tqqk=data['list'][i]['weather'][0]['description']
   print('日期：{},城市：{},天气情况：{},温度：{},气压：{},最高温：{},最低温：{}'.format(time,city,tqqk,temp,pre,temp_max,temp_min))
   if tqqk=='小雨':
       print('温习提示：天雨路滑，请注意出行安全，记得携带雨具')
   elif tqqk=='中雨':
       print('温习提示：请携带雨具，注意防寒保暖')
   elif tqqk=='大雨':
       print('温习提示：请尽量避免出门，锁好门窗，注意防洪')
   elif tqqk=='多云':
       print('温习提示：可以进行适当的户外活动，注意安全')             
   elif tqqk=='晴':
       print('温习提示：外出注意做好防晒')
                 
for i in range(1,10):
    if i==1:
        print('__'*25)      
    elif i==2:
        print('|','**'*23,'|')
    elif i==5:
        print('|*',' '*17,'天气 预报',' '*17,'*|')
    elif i==8:
        print('|','**'*23,'|')
    elif i==9:
        print('~~'*25)      
    elif i!=1 and i!=9 and i!=5 and i!=8:
        print('|*',' '*44,'*|')
     
print('--'*10,end='')
print('*'*5,end='')
print('--'*10)
print('|',end=' '*44)
print('|')
print('|',end=' '*44)
print('|')
print('|',end=' '*19)
print('weather',end =' '*18)
print('|')
print('|',end=' '*44)
print('|')
print('|',end=' '*44)
print('|')
print('--'*10,end='')
print('*'*5,end='')
print('--'*10)














   

























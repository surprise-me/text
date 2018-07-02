# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:21:27 2018
第十题：火车票交互查询
1.动态输入出发站和到达站，然后查询火车票情况
2.将火车余票站中的三字码转换成车站名
3.按照出发时间排序，按照历时时间排序
@author: Administrator
"""

#如果是定义的一个函数猜需要return返回，不是函数则不需要
bm=open('./火车站编码.csv','r',encoding='utf-8').readlines()
def zh(where):   
    for i in bm:
        szm=' '
        if where==i.split(',')[0]:
            szm=i.split(',')[1]
            break
    return szm

t=input('time')
q1=input('qidian')
q2=zh(q1)
z1=input('zhongdian')
z2=zh(z1)

import urllib.request as r#导入联网工具包，命令为r
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'
url=url.format(t,q2,z2).replace('\n','')
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)  

p='      '
title='车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split('p')
for i in title:
    print(i.center(20),end='  ')
print(' ')
n=len(data['data']['result'])
for i in range(n):    
    g=data['data']['result'][i]
    s=g
    g=s.split('|')
    hc=[g[3],[g[6],g[7]],[g[8],g[9]],g[10],g[32],g[31],g[30],'--',g[23],'--',g[28],'--',g[29],g[26],'--',g[1]]
    a=list(data['data']['map']) 
    for i in range(2):
        for j in range(len(a)):
            if hc[1][i]==a[j]:
                w=a[j]
                hc[1][i]=data['data']['map'][w]
    for i in hc:
        print(str(i).center(10).replace('[',' ').replace(']',' '),end=' ')
    print(' ')
print(' ')
 
result=data['data']['result']
data_map=data['data']['map']
title='时间{}车次{}'.format(p,p)
title=title.split(p) 
ls2=[]
for q in title:
    print(q.center(6),end=' ')
print('\n')
for j in range(n):
    s=result[j]
    ls =s.split("|")    
    ls1=[ls[10],ls[3]]
    ls2.append(ls1)  
ls4=sorted(ls2)
for w in ls4:
    print(str(w).center(6).replace('[',' ').replace(']',' '),end='   ')
    print('\n')





















        




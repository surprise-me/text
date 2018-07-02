# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:06:17 2018

题目十四：家长帮大数据爬虫项目
1.根据all_school.txt获取全中国学校网址编号：1304，生成一个2300列表
2.根据http://www.gaokaopai.com/daxue-zhaosheng-学校编号.html 获取全国城市的编号 例如北京：11
3.班级团队(需要下载142600(2300*31*2)次)：
    中国划分区域-分组(城市)
    区域分组员
    如何下载策略-分时间下载
    执行人物2300-分配到自己的任务一般是2300
    保存数据---组长全部合并--班长统计
4.待定

@author: Administrator
"""
#--------学校编号----------------------------------------------
import urllib.request as r#导入联网工具包，命令为r
url='file:///C:/Users/Administrator/Desktop/%E7%AC%AC%E5%85%AD%E6%AC%A1/all_school.txt'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
numbel=re.compile('http://www.gaokaopai.com/daxue-jianjie-(.*?).html').findall(data)
for i in range(len(numbel)):
    print(numbel[i],end='\t')

#-------------城市编号------------------------------------
url='http://www.gaokaopai.com/daxue-zhaosheng-477.html'
data='id=477&type=1&city=23&state=1'.encode()
req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
data=r.urlopen(req).read().decode('utf-8')
print(data)
import re
a=re.compile('<li data-val=(.*?)data-id=(.*?)onclick=(.*?)>(.*?)</li>').findall(data)
for i in range(2,33):
    print('城市：{}\t编码：{}'.format(a[i][3],a[i][2]).replace("$.setVar('claimCity', ",'').replace(')"','').replace('"',''))


#----------爬取------------------------------
import urllib.request as r 
f=open('D:/renshu11.txt','w')
for i in range(len(numbel)):
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
    data='id={}&type=2&city=23&state=1'.format(numbel[i]).encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    d=r.urlopen(req).read().decode('utf-8','ignore')
    if d.startswith('{'):
        print('胜利了{}次'.format(i))
    else:
        while True:
            print('下载失败，重新下载中...')
            url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
            data='id={}&type=2&city=46&state=1'.format(numbel[i]).encode()
            req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
            d=r.urlopen(req).read().decode('utf-8','ignore')
            if d.startswith('{'):
                print('胜利了{}次'.format(i))
                break
    f.write(d+'\n')
f.close()
print('哈哈哈哈哈，你是最棒的')

#-----------------解析-----------------------------------------   
import json
rs=open('D:/rs.txt','r')
rs=rs.readlines()
a=0
b=0
c=0
d=0
e=0
f=0
sum=0
for line in rs:   
    dddd=json.loads(line)
    if dddd['status']==0:
        city=dddd['data']['city_name']#招生城市
        print('在{}并没有招生计划额'.format(city))
    else:
        for i in range(len(dddd['data'])):
            city=dddd['data'][i]['city']
            v=dddd['data'][i]['sub_type']
            z=dddd['data'][i]['plan']
            if city=='黑龙江':
                if v=='1':
                    a +=int(z)
                else:
                    b +=int(z)
            elif city=='吉林':
                if v=='1':
                    c +=int(z)
                else:
                    d +=int(z)
            elif city=='辽宁':
                if v=='1':
                    e +=int(z)
                else:
                    f +=int(z)
        sum=a+b+c+d+e+f
print('黑龙江文科:{}\t黑龙江理科：{}'.format(a,b))
print('吉林文科:{}\t吉林理科：{}'.format(c,d))
print('辽宁文科:{}\t辽宁理科：{}'.format(e,f))
print('招生总人数：{}'.format(sum))  




 






















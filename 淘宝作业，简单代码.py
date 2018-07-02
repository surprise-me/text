# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 14:57:06 2018
第七题：保存淘宝数据(小组项目)
1.每个组员爬取100页数据(同一种商品)，条件是北京，上海，广州，成都...商品名，价格，付款，店铺名,地址
2.保存的商品信息有(同第六题),并且是以为csv格式保存
3.单个组员求出当前城市的商品的众数(最多的价格)
4.小组文件合并，求出商品的平均价格

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='https://s.taobao.com/search?q=%E5%B8%BD%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180623&ie=utf8&loc=%E7%BE%8E%E5%9B%BD%2C%E8%8B%B1%E5%9B%BD%2C%E6%B3%95%E5%9B%BD%2C%E7%91%9E%E5%A3%AB%2C%E6%BE%B3%E5%A4%A7%E5%88%A9%E4%BA%9A%2C%E6%96%B0%E8%A5%BF%E5%85%B0%2C%E5%8A%A0%E6%8B%BF%E5%A4%A7%2C%E5%A5%A5%E5%9C%B0%E5%88%A9%2C%E9%9F%A9%E5%9B%BD%2C%E6%97%A5%E6%9C%AC%2C%E5%BE%B7%E5%9B%BD%2C%E6%84%8F%E5%A4%A7%E5%88%A9%2C%E8%A5%BF%E7%8F%AD%E7%89%99%2C%E4%BF%84%E7%BD%97%E6%96%AF%2C%E6%B3%B0%E5%9B%BD%2C%E5%8D%B0%E5%BA%A6%2C%E8%8D%B7%E5%85%B0%2C%E6%96%B0%E5%8A%A0%E5%9D%A1%2C%E5%85%B6%E5%AE%83%E5%9B%BD%E5%AE%B6&ajax=true'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)

f=open('./hat.csv','w')#csv表格文件，以逗号分割
f.write('商品名,价格,付款,店铺名,地址\n')
for i in range(36):
    title=data['mods']['itemlist']['data']['auctions'][i]['title']
    view_price=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    view_sales=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    nick=data['mods']['itemlist']['data']['auctions'][i]['nick']
    item_loc=data['mods']['itemlist']['data']['auctions'][i]['item_loc']
    print('商品名:{}，价格:{}，付款:{}，店铺名:{},地址:{}'.format(title,view_price,view_sales,nick,item_loc))
    f.write('{},{},{},{},{}\n'.format(title,view_price,view_sales,nick,item_loc))
f.close()#关闭文件，保存文件

f=open('./hat.csv','a')#csv表格文件，以逗号分割
for i in range(1,100):
    data=i*44
    import urllib.request as r#导入联网工具包，命令为r
    url='https://s.taobao.com/search?q=%E5%B8%BD%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180623&ie=utf8&loc=%E7%BE%8E%E5%9B%BD%2C%E8%8B%B1%E5%9B%BD%2C%E6%B3%95%E5%9B%BD%2C%E7%91%9E%E5%A3%AB%2C%E6%BE%B3%E5%A4%A7%E5%88%A9%E4%BA%9A%2C%E6%96%B0%E8%A5%BF%E5%85%B0%2C%E5%8A%A0%E6%8B%BF%E5%A4%A7%2C%E5%A5%A5%E5%9C%B0%E5%88%A9%2C%E9%9F%A9%E5%9B%BD%2C%E6%97%A5%E6%9C%AC%2C%E5%BE%B7%E5%9B%BD%2C%E6%84%8F%E5%A4%A7%E5%88%A9%2C%E8%A5%BF%E7%8F%AD%E7%89%99%2C%E4%BF%84%E7%BD%97%E6%96%AF%2C%E6%B3%B0%E5%9B%BD%2C%E5%8D%B0%E5%BA%A6%2C%E8%8D%B7%E5%85%B0%2C%E6%96%B0%E5%8A%A0%E5%9D%A1%2C%E5%85%B6%E5%AE%83%E5%9B%BD%E5%AE%B6&bcoffset=4&p4ppushleft=1%2C48&s={}&ntoffset=4&ajax=true'
    data=r.urlopen(url.format(data)).read().decode('utf-8')
    #讲str类型转换为dict
    import json
    data=json.loads(data)   
    for i in range(44):
        title=data['mods']['itemlist']['data']['auctions'][i]['title']
        view_price=data['mods']['itemlist']['data']['auctions'][i]['view_price']
        view_sales=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
        nick=data['mods']['itemlist']['data']['auctions'][i]['nick']
        item_loc=data['mods']['itemlist']['data']['auctions'][i]['item_loc']
        print('商品名:{}，价格:{}，付款:{}，店铺名:{},地址:{}'.format(title,view_price,view_sales,nick,item_loc))
        f.write('{},{},{},{},{}\n'.format(title,view_price,view_sales,nick,item_loc))
f.close()#关闭文件，保存文件


















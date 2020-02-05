
# coding: utf-8


from pyecharts import Map

import numpy as np
value = np.log10(np.array([1052, 104, 98, 83, 75, 69, 60, 51, 44, 40, 39, 33, 31, 19, 19, 18, 18, 15, 15, 13, 11, 10, 9, 7, 7, 5, 5, 4, 4, 3,3,1,1]))
attr = ["湖北","浙江","广东","河南","重庆","湖南","安徽","北京","四川","上海","山东","广西","江苏","海南","辽宁","江西","福建","陕西","黑龙江","河北","云南","天津","山西","内蒙古","甘肃","香港","贵州","吉林","宁夏","台湾","新疆","青海","西藏"]
map = Map("截至 2020-1-26 12:13:19 数据统计", width=1000, height=800)
map.add("",attr,value,is_map_symbol_show=True,maptype="china", is_visualmap=True, visual_text_color='#000', 
    is_label_show=True,     visual_range=[np.min(value),np.max(value)],visual_range_color=['#ffffe0','#ff0000','#8B3a3a'])



import requests
import re
import json



#从新浪的网页中抓取曀数据
r = requests.get("https://interface.sina.cn/news/wap/fymap2020_data.d.json?1580718993853&&callback=sinajp_15807189938694110947357636703")


#给返回的response指定字符编码
r.encoding = r.apparent_encoding


#正则出结果
json_str = re.search("\(+([^)]*)\)+", r.text).group(1)

#也可以用字符串的lstrip()和rstrip()函数来处理字符串
h = h.lstrip('sinajp_15807189938694110947357636703(\n \n\n\n').rstrip('\n\n\n);')

html = f'{json_str}'
#用loads（）json数据转换成成字典类型
table = json.loads(f"{html}")



#遍历出城市名和确认数据，我只取河南省的
n = []#城市名
c = []#确认数据
for ppp in table['data']['list']:
    if ppp['name']=='河南':
        for pp in ppp["city"]:
            n.append(pp['name'])
            c.append(int(pp['conNum']))

#导入pyecharts库
from pyecharts import Map
import numpy as np

#先把地图Map实例化
map = Map('河南2020.2.5疫情图',width = 1000 ,height=800)

cc = np.log10(np.array(c))



#再用这个实例的add（）方法
map.add('',n,c,is_map_symbol_show=True,maptype="河南", is_visualmap=True, visual_text_color='#000', 
    is_label_show=True,     visual_range=[np.min(c),np.max(c)],visual_range_color=['#ffffe0','#ff0000','#8B3a3a'])



#导出地图
map.render()


h = r.text




jh = json.loads(h)



for i in table['data']['list']:
    if i['name'] == '河南':
        for aa in i['city']:
            print(aa['name'],aa['conNum'])
            
            



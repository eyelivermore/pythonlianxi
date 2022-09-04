# -*- coding: utf-8 -*-
import os
from unicodedata import name
#设定文件路径

path='D:\网店图片\京东宸雯图片\二建一书通关\详情1'
i=1
#对目录下的文件进行遍历
for file in os.listdir(path):
#判断是否是文件
    if os.path.isfile(os.path.join(path,file))==True:    
        #设置新文件名
        #new_name=file.replace(file,f"{myname}.jpg")
        #文件的名字等于列表索引
        
        mmfile = "一书"+file[-6:]
        #mmfile = f"二教材{i}"+file[-4:]
        new_name=file.replace(file,mmfile)
        
        print(mmfile)
        os.rename(os.path.join(path,file),os.path.join(path,new_name))
        i+=1


        #重命名，os.path.join(路径，文件名)连接路径和文件名的

        #结束
print ("End")
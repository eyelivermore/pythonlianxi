# -*- coding: utf-8 -*-
import os
from unicodedata import name
#设定文件路径
lname = ["消防共9本",'机电专业教材3本套装','二建建筑专业教材3本套装',
'二建市政专业教材3本套装',
'二建水利专业教材3本套装',
'二建公路专业教材3本套装',
'二建水利专业教材试卷',
'二建建筑专业教材试卷',
'二建公路专业教材试卷',
'二建市政教材',
'二建机电教材',
'一建市政教材',
'一建建筑教材',
'一建机电专业教材',
'一建建筑8本套装',
'一建机电8本',
'一建市政8本',
'二级消防教材共2本',
'2022年司法考试历年真题试卷司法真题试卷',
'初级会计教材+试卷4本套装',
 '二级消防教材+习题 共4本',
'二级消防6本',
 '中级教材+试卷 共6本',
 '消防教材+习题 共6本']
path='C:\\Users\\Fsir\\Desktop\\新建'
i=0
#对目录下的文件进行遍历
for file in os.listdir(path):
#判断是否是文件
    if os.path.isfile(os.path.join(path,file))==True:
#设置新文件名
        #new_name=file.replace(file,f"{myname}.jpg")
        print(file)
        mmfile = lname[i]+file[-4:]
        #mmfile = f"二教材{i}"+file[-4:]
        new_name=file.replace(file,mmfile)
        print(mmfile)
#重命名，os.path.join(路径，文件名)连接路径和文件名的
        os.rename(os.path.join(path,file),os.path.join(path,new_name))
        i+=1
#结束
print ("End")
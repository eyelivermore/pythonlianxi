
# coding: utf-8


import os
import re


#文件所在目录路径
path = 'D:/迅雷下载/亮剑30集全/'
#得到文件名列表
falelist = os.listdir(path)

for i in falelist:
    rst = re.search(r'[0-9]{2}',i)#正则出文件名中的每一集的数字
    if rst !=None:
        print(rst.group())
        oldname = path+os.sep+i #原文件名
        print('旧名是',oldname)
        newname = path+'亮剑'+rst.group()+'.mkv'#新文件名
        print('新名是',newname)
        os.rename(oldname,newname)#rename(原文件名,旧文件名)修改文件名    

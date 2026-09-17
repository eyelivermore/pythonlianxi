from sys import argv
from os.path import exists

script,from_file, to_file  = argv
#得到3个参数给3个变量
print(f"Copying from {from_file} to {to_file}")

#
in_file = open(from_file,encoding='utf-8')
#打开原文件
indata = in_file.read()
#赋值给indata

print(f"The input file is {len(indata)} bytes long")
#计算indata的长度
print(f"Does the output file exist? {exists(to_file)}")
print("Ready hit RETURN to contimue, CTRL-C to whort.")
input("?")

out_file = open(to_file,'w',encoding ='utf-8')
#创建复本文件
out_file.write(indata)
#写入原文件

out_file.close()
in_file.close()
print("操作完毕")
#关闭out_file,in_file 这两个对象 
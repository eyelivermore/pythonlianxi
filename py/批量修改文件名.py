import os

def rename(path):
    n = 1
    #获取文件夹里的全部文件名，存入列表
    filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）

    for files in filelist:#遍历所有文件

        Olddir=os.path.join(path,files);#原来的文件路径

        if os.path.isdir(Olddir):#如果是文件夹则跳过

            continue

        filename=os.path.splitext(files)[0];#文件名

        filetype=os.path.splitext(files)[1];#文件扩展名

        Newdir=os.path.join(path,f"{n}"+filetype);#新的文件路径

        os.rename(Olddir,Newdir);#重命名
        n += 1
aa = 'D:\pythonlianxi\zhaopian'        
rename(aa)
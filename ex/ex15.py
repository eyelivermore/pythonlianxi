from sys import argv

script,filename = argv
#把argv前面收到的两个参数传给两变量
txt = open(filename, encoding = 'utf-8')
#txt对象,打开filname收到的文件用,编码方式'UTF-8'
print(f"Here's you file {filename}!")
#打印这个变量
print(txt.read())
#用read()方法,读取txt这个对象
print("'Type the filename again:")
#打印
file_again = input(">")
#输入文件名
txt_again = open(file_again ,encoding = 'UTF-8')
#得到txt_again这个对象,打开输入的文件名, 用'UTF-8'编码方式
print(txt_again.read())
#打印Read()方法读到的内容
txt.close()
#关闭txt对象
txt_again.close()
#关闭txt_again对象
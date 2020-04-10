"""format是格式化字符串用的"""

name = ['黄涛','灰雁',"春艳"]
spouse = ['荣芳', "九九",'黄某涛']
age = [21.111,22.222,33.333]

#第一个大括号里面放的是变量n,第二个大括号里面放的是变量s
for n, s, a in zip(name,spouse,age):
    print('姓名:{},爱人:{},年龄:{}'.format(n,s,a))

#还可以对数字进行格式改变

for n, s, a in zip(name,spouse,age):
    print('姓名:{1},爱人:{0},年龄:{2:.0f}'.format(n,s,a))





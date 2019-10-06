import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import random

def tc_1(g):
    
    ls = []
    gf = []

    for i in range(10,g,10):
        
        y_jin = 0.0049#佣金
        pt_fei = 0.005#平台费
        js_fei = 0.003#交收费
        y_jin = y_jin*i
        if y_jin < 0.99:
            y_jin = 0.99
        pt_fei = pt_fei*i
        if pt_fei < 1:
            pt_fei = 1
        js_fei = js_fei*i

        z_fei = y_jin + pt_fei + js_fei

        gf.append(i)

        ls.append(z_fei)
    return np.array(ls) ,np.array(gf)

def tc_2(g):
    ls = []

    
    for i in range(10,g,10):
        y_jin = 5#佣金
        js_fei = 0.003#交收费
        js_fei = js_fei*i
        if js_fei<3:
            js_fei = 3
        z_fei = y_jin+js_fei
        ls.append(z_fei)
    return np.array(ls)
def f_bi(i):
    s = random.randint(1,3)
    f = i/s



x,y = tc_1(1500)

x2 = tc_2(1500)

plt.ylabel("总费用" ,fontproperties = "SimHei", fontsize = 15)
plt.xlabel("股票数" ,fontproperties = "SimHei", fontsize = 15)

matplotlib.rcParams["font.family"]='SimHei'
matplotlib.rcParams["font.size"] = 10
plt.plot(y,x,"r",label = '套餐一')
plt.plot(y,x2,"b",label = "套餐二")
plt.legend()
plt.show()






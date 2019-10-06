def tongji(name):
    '''词条统计'''
    counts = {}#定义一个字典
    with open(name,"r") as f:
        for i in f.readlines():
            i = i.replace("\n","")
            counts[i] = counts.get(i,0)+1
    print(counts.items())
    items = list(counts.items())
    items.sort(key = lambda x:x[1] , reverse = True)
    print(len(items))
    for t in range(0,len(items)):
        w, wo = items[t]
        print("{}这个销售了{}个".format(w,wo))


name = "淘宝数据2.csv"
tongji(name) 
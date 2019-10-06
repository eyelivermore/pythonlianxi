"""问题是 

所有囚犯站一排每次报到积数就枪毙
报到偶数就留下
这样一直持续下去 只到最后一个人就把他放了
如果你想被放到那么最开始你应该站在什么位置
"""
#先生成一个列表1到100
lsa = [i for i in range(1,101)]
#每次都枪毙积数编号的囚犯
def lsdel(xs):
    xx = []
    for x,i in enumerate(xs):
        x+=1
        if x%2 == 0:
            xx.append(i)
    return xx

#一轮一轮的枪毙下去
def zcdel(xf):
    while len(xf)!=1:
        xf = lsdel(xf)
        print(xf)
    return xf
print(lsa)#第一步显示所有囚犯
ls = lsdel(lsa)#第二步先枪毙一轮积数的囚犯
print(ls)#第三步显示剩下的囚犯
xff = zcdel(ls)#第四步,就这样一轮一轮枪毙下去只到最后一个
print(f"最开始应该站在第{xff}位")


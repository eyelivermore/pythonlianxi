def exrate(r,x):
    """
       汇率互换函数
       r:代表币种
       x:代表金额
       港币10000元可以换成多少人民币就是exrate("h",10000)
    """
    
    hk = 100#港币
    rmb = 86.51#人民币
    if r in ["H" ,'h']:
        return rmb/hk*x
    elif r in ["r", "R"]:
        return hk/rmb*x


    

print(exrate('h',10000))


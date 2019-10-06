#输入温度
humidity = input("请输入温度")
#判断是是摄氏转换成华氏底
if humidity[-1] in ["C","c"]:
    #输入的字符串转去掉引号
    humidity_f = eval(humidity[:-1])
    #计算华氏度
    f = (humidity_f+32)*1.8
    print("输入的是{}摄氏度转换成华氏度是{:.2f}F度".format(humidity,f))
 
#郑州是华氏度转换成摄氏度
elif humidity[-1] in ["F","f"]:
    #输入的字符串去掉引号
    humidity_c = eval(humidity[:-1])
    #计算摄氏度
    c = (humidity_c-32)/1.8
    print("输入的是{}华氏度转换成摄氏度是{:.2f}C".format(humidity,c))
else:
    print("您输入的是:{}请检查格式".format(humidity))
    
    
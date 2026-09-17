def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f"you have {cheese_count} cheeses!")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    print("Man that s enough for a party!")
    print("get a bianket.\n")

print("We can just qive the function numbers directlyi\
       我们来看一下用数值做参数")
cheese_and_crackers(20,30)

print("OR we cao use variables from our scripti\
         我们也可以用变量来做参数")
amount_of_cheese =10
amount_of_crackers=50
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("我们来看一下函数相加")
cheese_and_crackers(10+20,5+6)

print("我看来看一下函数与变量相加")
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)
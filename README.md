
# 这是一个python小白的学习记录


```python
print("hello python")
print("python是一个很有意思的计算机语言")
```

    hello python
    python是一个很有意思的计算机语言
    

## python的数据分为:
### 数字类型
* 整形 int 是正或负整数，不带小数点。Python3 整型是没有限制大小的
* 浮点型 float 浮点型由整数与小数部分组成，浮点型也可以使用科学计数法表示2.5e2 = 2.5 x 102 = 250
* 复数complex 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。


# 序列类型 

####  可变也是可修改序列
###### 字符串 str
* a= "Apples Oranges Crows Telephone Light Sugar"

###### 列表 list 
* more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#### 不可变是不能修改序列
* 元组 tuple

#### 映射类型
* 集合（set）是一个无序不重复元素的序列(&交  |并  -差  ^补)
* 字典 (dict) 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割

# 程序结构

## 判断语句
* if
* elif
* else

## 循环语句
* for in 
* while


```python
ls=[i for i in range(9)]
print(ls)    
    
x=0    
while x<9:
    print(x,end =" ")
    x+=1
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    0 1 2 3 4 5 6 7 8 

# python是一个面向对象的语言 一切皆是对象

* class 来定义类
* def 定义函数 在类里面叫做方法

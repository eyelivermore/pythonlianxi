def add(a,b):
    """加法"""
    print(f"{a}加{b}是多少")
    return a+b

def subtract(a,b):
    """减法"""
    print(f"{a}减去{b}是多少?")
    return a-b

def multiply(a,b):
    """乘法"""
    print(f"{a}乘以{b}是多少?")
    return a*b

def divide(a,b):
    """除法"""
    print(f"{a}除以{b}是多少")
    return a/b

print("let's do some math with just functions\n \
让我们用函数做一些数学运算")

age = add(30,5)
height = subtract(70,4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"加法:{age},减法:{height},乘法:{weight},除尘:{iq}")

what = add(age,subtract(height,multiply(weight,divide(iq,2))))
print(f"变成了,{what},你可以手工试一下")

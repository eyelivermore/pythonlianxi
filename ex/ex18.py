
def print_two(*args):
    #传入一个参数列表
    arg1,arg2, arg3 = args
    #把args收到的参数无组 分别赋值给前面三个变量
    print(f"arg1: {arg1},arg2: {arg2},arg3: {arg3}")

def print_two_argsin(arg1,arg2):
    print(f"arg1: {arg1},arg2: {arg2}")

def print_one(arg1):
    print(f'arg1:{arg1}')

def print_none():
    print("i got nothin',")

print_two("Zed","Shaw","Two")
print_two_argsin("zed","Shaw")
print_one("first!")
print_none()
import sys





'''
如果想在开始工作之前加一个密码验证功能可以这样
'''

def log(text):
    def decorator(n):
        def wrapper(*args,**kw):
            i = input('请输入密码:')
            if i =='abc':
                print(text,':halle,密码正确，欢迎回来')
            else:
                print(text,'密码错误，你无法进入')
                sys.exit(0)
            return n(*args,**kw)
        return wrapper
    return decorator 

@log('fenglei')
def now():
    print('请开始工作')

now()
print("%s"% now.__name__)    

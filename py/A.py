'''
为什么要用
if __name__ == "__main__"
当A.py直接运行时
__name__ 是== '__main__'的
当A.py当成模块民导入时 
__name__  == 'A'  
A.py会被程序直接运行 
'''
name = 'python文件 A.py'
print('name是:',name)

def fun_A():
    print('调用方法A')

def print_name():
    print('A.py __name__的值是:',__name__)

if __name__ == '__main__':
    print('程序入口')
    fun_A()
    print_name()
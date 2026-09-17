class Parent:
    def override(self):
        print("父亲PARENT override()方法")
    def implicit(self):
        print("父类PARENT implicit()方法")
    def altered(self):
        print("父类PARENT altered()方法")
class Child(Parent):
        #覆盖了父类的override方法
    def override(self):
        print("子类中的方 override()方法重写")
    def altered(self):
        #这一条语句覆盖了父类的同一条语句
        print ("子类CHILD, BEFORE PARENT altered()方法")
        #调用了父类的这个altered()方法
        super(Child, self).altered()
        #又回到子类继续运行
        print ("CHILD, AFTER PARENT altered()")

# 改变一下试试
#用组合的方式来调用相当于父类中的方法
class Other:
    def override(self):
        print("OTHER override()")
    def implicit(self):
        print("OTHER implicit()")
    def altered(self):
        print("OTHER altered()")

class Child_one:
    def __init__(self):
        #实例化Other这个类然后就可以调用这个类的方法了
        self.other = Other()
    def implicit(self):
        self.other.implicit()
    def override(self):
        print("CHILD override()")
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")



#这个是继承的演示在在电脑端修改
dad = Parent()
son = Child()
dad.implicit()
#调用了父类的这个implicit()方法
son.implicit()
dad.override()
#覆盖了父类的override()方法
son.override()
dad.altered()
#覆盖了父类的这个方法其中super调用了父类的这个方法一次
son.altered()

#组合调用类的方法
son_a = Child_one()
son_a.implicit()
son_a.override()
son_a.altered() 



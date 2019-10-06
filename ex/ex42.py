class Animal:
    pass
## 继承了动物类
class Dog(Animal):
    def __init__(self, name):
    ## 初始化name属性
        self.name = name
## 继承了动物类
class Cat(Animal):
    def __init__(self, name):
    ## 初始化名字
        self.name = name
## 定义一个人类
class Person:
    name = "Hans"
    def __init__(self, name,age,gender):
    ## 名字属性
        self.name = name
        self.age = age
        self.gender = gender
    ## 人有一个宠物
        self.pet = None
    @classmethod #类方法装饰器
    def show(cls):
        print('我是人类的名字叫{}'.format(cls.name))
    @property#这个装饰器可以把方法当属性来用
    def Say(self):
        print("我是人类,我有说话功能,的名字是:{}".format(self.name))
        return self.name

## 定义一个员工类
class Employee(Person):
    def __init__(self, name, age, salary, gender):
    ## 找到父类的name
        super(Employee, self).__init__(name,age,gender)
    ## 人类要有薪水
        self.salary = salary
    @staticmethod
    def word(salary):
        print("hello:我是员工类,我的工资是{}".format(salary)) 
    #这是一个静态装饰器 这是装饰器不能有self,只可以被类直接访问,
    #没有装饰器不加self 对象是不能请问的

    # def show(self):
    #     print("我的名字叫{}".format(self.name))
## 鱼类
class Fish:
    pass
## 三文鱼
class Salmon(Fish):
    pass
## 比目鱼继承了鱼类
class Halibut(Fish):
    pass
## rover是狗
print("go")
rover = Dog("Rover")
## satan是猫
satan = Cat("Satan")
## mary是人类
mary = Person("Mary",25,'wman')
Person.show()
mary.show()
## 给mary的宠物起一个名字叫satan
mary.pet = satan
## frank是员工,薪水120000
frank = Employee("Frank", 35, 120000,"man")
## frank的宠物起一个名字叫rover

#frank.age = 25
#frank.gender = 'man'
frank.pet = rover
print(frank.name,frank.pet.name,frank.salary)
frank.word(10000)
frank.show()
#把方法当做属性调用
print(frank.Say)
## flipper是鱼
flipper = Fish()
## crouse是三文鱼
crouse = Salmon()
## harry是比目鱼
harry = Halibut()



'''
集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
'''
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
"""
可以用大括号({})创建集合。
注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典，下一节我们会介绍这个数据结构

"""
a = set()

# 以下演示了两个集合的操作
a = set('abcd')
b = set('cdef')

print('a集合中的字母\n',a)
print('b集合中的字母\n',b)

print('a-b:集合a中包含，b中不包含,也叫集体的差集\n',a-b)

print('a|b:集合a或b中包含的所有元素,也叫集合的并集\n',a|b)

print('a&b:集合a和b中都包含了的元素，也中集集合的交集\n',a&b)

print('a^b:不同时包含于a和b的元素,也叫集合中的补集\n',a^b)

print('集合的增，删，改，查')
print('集合的增加用add(x)和update(x)函数')
a.add("f")
print('a.add("f")',a)
print('删用remove(x)删除指定元素')
a.remove('f')
print('a.remove("f")',a)
print('集合中的元素不能修改')

print('判断元素 x 是否在集合 s 中，存在返回 True，不存在返回 False。')
print('"f" in a 判断f是否在a集合中',"f" in a)
print("set")
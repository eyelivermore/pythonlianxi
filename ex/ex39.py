# 定义一个字典states
states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
        }
# 定义一个字典cities
cities = {
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
        }
# 给字典cities添加两个键值对
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
# 打印NY和OR的值
print ('-' * 10)
print ("NY State has: ", cities['NY'])
print ("OR State has: ", cities['OR'])
# 打印值
print ('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print ("Florida's abbreviation is: ", states['Florida'])
# 花式打印cities的值
print ('-' * 10)
print ("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

print ('-' * 10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))
# 打印键值对用items()函数
print ('-' * 10)
for abbrev, city in cities.items():
    print ("%s has the city %s" % (abbrev, city))

print ('-' * 10)
for state, abbrev in states.items():
    print ("%s state is abbreviated %s and has city %s" % (
    state, abbrev, cities[abbrev]))
print ('-' * 10)
# 函数get的用法,如果存在返回默认值,要么返回None
state = states.get('BeiJing')
if not state:
    states["BeiJing"] = 'BJ'
    print("Sorry, no BJ.")

city = cities.get('SH', 'SH')
if  city:
   cities[city] = 'ShangHai'  
   print("The city for the state 'SH' is: %s" % city)
print(states,"\n",cities)
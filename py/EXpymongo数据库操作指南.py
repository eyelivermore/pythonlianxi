#pymongo的增删改查使用说明
import pymongo
import datetime
#--------------------------------------------------------
"""#与mongoClient建立连接"""
client = pymongo.MongoClient("localhost",27017)
#也可以使用MongoClient URI格式
#client = pymongo.MongoClient("mongodb://localhost:27017/")

"""#获取数据库"""
#MongoDB的单个实例可以支持多个独立的数据库。
# 可以使用client实例上的属性样式访问来访问数据库data_base
db = client.data_base
#也可以便用字典样式获取数据库
# db = client["data_base"]

#-----------------------------------------------------
"""#获取集合(也叫表)"""
collection = db.text_collection
#或使用字典样式访问
#collection = db["text_collection"]
"""关于MongoDB中的集合（和数据库）
的一个重要注意事项是它们是懒惰创建的
也就是只有插入真正数据时才会创建"""

#-----------------------------------------------------------------
#建立真正的数据文件就是每一行数据
"""使用JSON样式的文档表示（并存储）MongoDB中的数据。在PyMongo中，
我们使用字典来表示文档。"""
post = {"作者": "Mike",
        "内容": "My first blog post!",
        "标签": ["mongodb", "python", "pymongo"],
        "时间": datetime.datetime.utcnow()}

"""插入文档"""
#要将文档插入集合，我们可以使用以下 insert_one()方法：
#第一步先指定一个表,也叫集合
posts = db.posts
#用这个实例加上insert_one()方法把post数据放入后面的括号里
#这样就在服务器上建立了posts这个表并在里面添加了数据
posts.insert_one(post)#返回的是inserted_id字段

#批量插入insert_mony()
posts.insert_many(new_posts)#new_posts是一个列表





#----------------------------------------------------------
"""查询"""
#用find_one()来查询一条数据
posts.find_one()#将要返回的字段设为1
#用find()查询多个文档
#除了 _id 你不能在一个对象中同时指定 0 和 1，
# 如果你设置了一个字段为 0，则其他都为 1，反之亦然。
new_find = posts.find({},{"作者":1,"标签":1})#可以用for循环迭代出每一个数据

#计数count()
posts.count()
#与查询结果匹配的计数
posts.find({"author": "Mike"}).count()

#范围查询
#超过指定日期的帖子,按作者进行排序
d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"日期": {"$lt": d}}).sort("作者"):
    print(post)



#用正则表达式查询
myquery = { "作者": { "$regex": "^M" } }
my_data = posts.find(myquery)
for i in my_data:
    print(i)

#返回指定条数用limit()方法
myresult = posts.find().limit(3)

#---------------------------------------------------

"""修改"""
#我们可以在 MongoDB 中使用 update_one() 方法修改文档中的记录。
#该方法第一个参数为查询的条件，第二个参数为要修改的字段。
myquery = {"内容": "My first blog post!"}
newvalues = {"$set":{"内容":"平凡的世界"}}
posts.update_one(myquery,newvalues)

#如果要修改所有匹配到的记录，可以使用 update_many()
myquery = {"作者":{"$regex":"^M"}}
newvalues = {"$set":{"内容":"good"}}
posts.update_many(myquery,newvalues)#找到作者是M开头的,替换内容字段的值为good

#-----------------------------------------------------------------------------

"""删除数据"""
#我们可以使用 delete_one() 方法来删除一个文档，
#该方法第一个参数为查询对象，指定要删除哪些数据

myquery = { "作者":"Mike" }
posts.delete_one(myquery)

#我们可以使用 delete_many() 方法来删除多个文档，
#该方法第一个参数为查询对象，指定要删除哪些数据
myquery = { "标签": {"$regex": "^F"} }
x = posts.delete_many(myquery)
#delete_many() 方法如果传入的是一个空的查询对象，则会删除集合中的所有文档

#我们可以使用 drop() 方法来删除posts集合
posts.drop()

#-----------------------------------------------------------------------

"""排序"""

#sort() 方法可以指定升序或降序排序。
#sort() 方法第一个参数为要排序的字段，
#第二个字段指定排序规则，1 为升序，-1 为降序，默认为升序
mydata = posts.find().sort("作者",1)
for i in mydata:
    print(i)


import pymysql

id = 'AXP'
name = 'American Express'
price = "91.00"
db = pymysql.connect(host='localhost',user='root', password='Lovegame3998', port=3306 , db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name, price) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, name, price))
    db.commit()
except:
    db.rollback()
db.close()


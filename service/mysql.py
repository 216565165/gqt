import pymysql

db = pymysql.connect(host="localhost", user="cyi", password="cyi", database="db_cyi",charset="utf8")
cursor = db.cursor()
data=[("user01", '1234'),
      ("user02", '1234'),
      ]
try:
    cursor.executemany("insert into tb_username(username,password) values (%s,%s)",data)
    db.commit()
except:
    db.rollback()
db.close()
import pymysql
import pymysql.cursors

connection = pymysql.connect(
    host="10.100.33.60",
    user="tbobo",
    password="223068750",
    database="world",
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connection.cursor()

cursor.execute("SELECT * from `country`")

result = cursor.fetchall()

print(result[3]['HeadOfState'])

print(type(result))
import pymysql
import pyodbc

db = pymysql.connect("localhost","manoj","root","manoj")

cur = db.cursor()

cursor.execute("Drop table")

# Create table

sql = """CREATE TABLE EMPLOYEE (
      name CHAR(40) NOT NULL,
      salary INT 

)"""

sql1 = """CREATE TABLE COMPANY (
      first_name CHAR(40) NOT NULL,
      last_name CHAR(40) NOT NULL,
      age INT NOT NULL)"""


cursor.execute(sql)

cursor.execute(sql1)

db.close()

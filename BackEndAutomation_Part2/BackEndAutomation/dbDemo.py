import mysql.connector
from utilities.configurations import *

# host, database, user, password
# conn = mysql.connector.connect(host='localhost',database='PythonAutomation',
#           user='root',password='rahulshettyacademy')

conn = getConnection()
print(conn.is_connected())
cursor = conn.cursor()
cursor.execute("select * from CustomerInfo")
# row = cursor.fetchone()
# print(row)
# print(row[3])
# row = cursor.fetchone()
# rowAll = cursor.fetchall()
# print(rowAll) #list of tuples

rows = cursor.fetchall()
print(type(rows))
print(rows)
sum1 = 0
for row in rows:  # ('selenium', datetime.date(2020, 6, 7), 120, 'Africa')
    sum1 = sum1 + row[2]

print(sum1)
assert sum1 == 361

query = "update customerInfo set Location = %s where CourseName = %s"
data = ("UK", "Jmeter")
cursor.execute(query, data)
conn.commit()
conn.close()

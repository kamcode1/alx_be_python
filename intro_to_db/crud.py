import mysql.connector

mydatabase = mysql.connector.connect(
    host = "192.168.1.189",
    user = "root",
    password = "Theodora123!",
    database = "staff"
)
mycursor = mydatabase.cursor()
# mycursor.execute("SHOW DATABASES")
# mycursor.execute("SELECT * FROM employee")

for i in mycursor:
    print(i)
def create_record(id, first_name, last_name, position, salary):
    query = "INSERT INTO employee (id, first_name, last_name, position, salary) VALUES(%s, %s, %s, %s, %s)"
    values = (id, first_name, last_name, position, salary)
    mycursor.execute(query, values)
    mydatabase.commit()
    print("Record added successfully")
create_record(2, "sam", "Noah", "security", 150000)

# mycursor.execute("INSERT INTO employee (id, first_name, last_name, position, salary) values(3, 'yaf', 'Noah', 'driver', 70000)")
# mycursor.execute("SELECT * FROM employee")

# for i in mycursor:
#     print(i)
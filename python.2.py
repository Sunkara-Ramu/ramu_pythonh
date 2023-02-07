'''import mysql.connector

my_db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Nithin3090@',
    port = '3306',
    database = 'gaming_club'
)
print('Conncted to DB')
my_cursor = my_db.cursor()
my_cursor.execute.fetchall()
print('The employees are')
for employee in employees:
    print(employee)

for employee in employees:
    print('Employee Name:',employee[1],end=',')
    print('Designation:' + employee[2])

my_cursor.close()
print('Database successfully disconnected')'''

'''import mysql.connector
class DB_connections:
    def get_connections(self):
        connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Nithin3090@',
    port = '3306',
    database = 'gaming_club'
)
        return connection
    def create_table(self):
        query = ''''''
        create table students(id int primary key auto_increment, name varchar(50) not null,
        semester int branch varchar(50), phone_num varchar(10) unique);
        ''''''
        try:
            connection = self.get_connections()
            db_cursor = connection.cursor()
            db_cursor.execute(query)
            print('Table created successfully')
        except:
            print('Error while creating table')
        finally:
            db_cursor.close()
            connection.close()

    def insert_row(self):
        pass
    def read_all_rows(self):
        pass
    def read_rows_by_id(self):
        pass
    def update_row_by_id(self):
        pass
    def delete_row_by_id(self):
        pass

db_oprs = DB_connections()
db_oprs.create_table()'''


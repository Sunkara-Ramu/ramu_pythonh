from hcl_database_connection import MysqlDatabaseConnection
class Booking(MysqlDatabaseConnection):
    def available_seats(self):
        try:
            self.cursor.callproc("get_no_avl_tkt")
            self.r=self.cursor.stored_results()
            print(self.r)
        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
def book(self):
    pass

b1=Booking()
#b1.connect("localhost","root","Ramu@1213,"hcl_vijayawada")
#sts=b1.available_seats()

#seat_avl={}

#seat_avl['Train_name']=sts[0]
#seat_avl['Seats']=sts[1]
#print(seat_avl)
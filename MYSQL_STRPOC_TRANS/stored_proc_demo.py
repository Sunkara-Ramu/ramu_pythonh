from mysql.connector import Error
from hcl_database_connection import MysqlDatabaseConection
class HclstoredProcedure(MysqlDatabaseConection):
    try:
        self.cursor.callproc("get_cust")
        for r in self.cursor.stored_results():
            print(r.fetchall())
    except Exception as e:
        print(e)
    finally:
        if(self.connection.is_connected()):
            self.cursor.close()
            self.connection.close()
connect_obj=HclstoredProcedure();
connect_obj.connecct("localhost","root","Aptech@123","hcl_vijayawada")
connect_obj.execute_str_procedure()
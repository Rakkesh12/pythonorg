import pyodbc
server= 'HCL-02-27\SQLEXPRESS'
database='file_results'
username='admin'
password='Rakkesh@123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor=cnxn.cursor()
class employee:
   def create_table_in_python(self):
      query = '''create table sai_123(
                     Emp_Name varchar(50),
                     Salary int,
                     project varchar(20))'''
      cursor.execute(query)
      query1='''select * from sai_123'''
      cursor.execute(query1)
   def insert_values_in_python(self,Emp_Name,Salary,Project):
      #query='''insert into sai_1234(Emp_Name,Salary,project)
      #values(manoj,100000,python)'''
      query = '''insert into sai_1234(Emp_Name,Salary,project) values({0} {1} {2}'''
      insert_query=query.format(Emp_Name,Salary,Project)
      cursor.execute(insert_query)
obj_1=employee()
obj_1.create_table_in_python()








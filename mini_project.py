import pyodbc
# for connecting the database to python we have to import python open database connector(pyodbc)
class ProgrammingError(Exception):
   def __str__ (self):
       return("it will give the programming error")
#for connecting the database to python we need to give some neccesray credientails like server,database,username,password
server= 'HCL-02-27\SQLEXPRESS'
database='file_results'
username='admin'
password='Rakkesh@123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor=cnxn.cursor()
class employee:
    #this method is used to create the table in database
   def create_table_in_python(self):
      try:
         query = '''create table sai_123
                    (
                     Emp_id int,
                     Emp_Name varchar(50),
                     Salary int,
                     project varchar(20)
                     )
                     '''
         cursor.execute(query)
         cursor.commit()
      except pyodbc.ProgrammingError:
          #if you get any error in the try method this except method will execute
         print("the TABLE is already exist in the DATABASE")
      except ProgrammingError as error_1:
          print(error_1)
class rakkesh_error(Exception):
    def __str__(self):
        return("Bouns should be less than 2")

class employee_1:
    bouns=2
    all_projects=['python','c,','java']
    #here we are intilizaling the id ,name,salary,project
    def __init__(self,id,Emp_Name,salary,project):
        self.id=id
        self.salary=salary
        self.Emp_name=Emp_Name
        self.project=project
        if self.project in self.all_projects:
            #first we are giving self.project name if the project name is present in the all_projects the insert_values_in_python will exceute
            self.insert_values_in_python()
        else:
            #if the project is not present  in the self.project else statement will execute
            print("project name is not in the list")
    #this method will update the salary of the particular emp_id
    def updating_salary(self,id):
        query="update sai_123 set salary={0} where Emp_id={1}"
        insert_query=query.format(self.salary,id)
        #print(insert_query)
        cursor.execute(insert_query)
        cursor.commit()
    #here we adding bouns to the salary
    def adding_bonus(self,id,bouns):
        try:
            if(bouns<=self.bouns):
                bouns_1=(self.bouns)*10
                self.salary=(self.salary)+bouns_1
                self.updating_salary(id)
            else:
                raise rakkesh_error
        except rakkesh_error as a:
            print(a)
            #print("bouns shoud be less than 2")
    #this method will insert values in the database
    def insert_values_in_python(self):
        query = "insert into sai_123 values({0},'{1}',{2},'{3}')"
        insert_query = query.format(self.id,self.Emp_name, self.salary, self.project)
        cursor.execute(insert_query)
        cursor.commit()
    #this method is used to dispaly the details of the employee in the table
    def display_employee_details(self):
        query='''select * from sai_123'''
        result_1=cursor.execute(query)
        for i in result_1:
            # i variable  can access each data from result_1  it will print the data
            print(i)
    # this method will delete all the data in the table
    def droping_table(self):
        query="drop table sai_123"
        cursor.execute(query)
        cursor.commit()
    # this  method is used to change the project for the particular employee id
    def change_project(self,id,project):
        #we will get valueerror
        query="update sai_123 set project='{0}' where Emp_id='{1}' "
        cursor.execute(query.format(project,id))
        cursor.commit()
    #for deleting the data for a particular employee id this method is used
    def deleting_rows(self,id):
        query="delete from sai_123 where Emp_id='{0}' "
        cursor.execute(query.format(id))
        cursor.commit()

obj_1=employee()
obj_1.create_table_in_python()
#obj_1.insert_values_in_python('arha',200,'c')
obj_2=employee_1(52130789,"rakkesh",9960,"python")
obj_2.display_employee_details()
obj_2.adding_bonus(52130789,1.5)
#obj_2.insert_values_in_python()
obj_2.change_project(52130789,"java")
#obj_2.deleting_rows(52130789)
#obj_2.droping_table()
#obj_2.display_employee_details()
#obj_2.updating_salary(52130789)
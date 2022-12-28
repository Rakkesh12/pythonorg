import pyodbc
from capstone_1 import employee

class employee_1:
    bouns=2
    project=['python','c,','java']
    def __init__(self,salary,Emp_name):
        self.salary=salary
        self.Emp_name=Emp_name
        for i in self.project:
            self.project=i
    def updating_salary(self):
        self.adding_bonus()
        query='''update sai_123 set salary ={0}'''
        insert_query=query.format(self.salary)
        self.cursor.execute(insert_query)
        self.cursor.commit()
    def adding_bonus(self):
        self.salary=(self.salary)*(self.bouns)//100
    def display_employee_details(self):
        query='''select * from sai_1234'''
        self.cursor.execute(query)
    def checking_the_project(self):
        for i in range(self.project):
            if(self.project[i]!='c#'):
                print(self.project[i])
            else:
                print("c# is not ur project")
    def inserting_employee_details(self):
        self.





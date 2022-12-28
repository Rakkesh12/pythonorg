"""file=open("rakesh.txt",'r')
print(file.read())


with open("rakesh.txt",'r') as file: #context manager
    for line in file: #it will print all lines in the file by using the for loop
        print(line)

with open("rakesh.txt",'r') as y:
    print(y.readline()) #we can  read how characters we will use this
    print(y.tell())
    print(y.isatty())
    print(y.close())
with open("rakesh.txt",'w') as file:
    file.writelines("name is changed to govind"
                    "nmae is siva")
with open("rakesh.txt",'r') as file:
    print(file.read())"""

"""file=open("rakesh.txt",'r+')
file.write("file operations")
file.read()
file.close()
"""
"""file1=open("rakesh.txt",'a+')
file1.write("this is rakkesh")
print(file1.read())
file1.close()"""

"""with open("govid.txt",'r+') as file:
    file.writelines("rakkesh5"
                    "how are u what are u doing")
    file.writelines("rakesh44")
    file.write("varma")

'''#with open("govind.txt",'w') as file:
    file.write("rakkesh7")
'''
with open("govid.txt",'r') as file:
    print(file.read())"""


"""with open("govid.txt",'r') as file:
    for line_1 in file:
    
    #print(file.read())"""

"""f_1=open("govind.txt",'a')
f_1.write("this is rakkesh\n")
f_1.writelines("hope ur doing well\n")
f_1.close()"""

"""f_2=open("govind.txt",'w+')
li=["he is govind \n","he is working in hcl\n","now acting in blueflims"]
for i in li:
    f_2.writelines(i)
#f_2.read()
f_2.close()"""

"""f_3=open("govind.txt",'r+')
print(f_3.read())
print(f_3.writable())"""
#f_3.write("now in hollywood")

"""import os
for i in range(65,91):
    f=chr(i)
    #os.remove(f+".txt")#to remove the files we will use this
    #with open((f+'.txt'),'x') as file:
        #file.write(f)
        #file.writelines()"""
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







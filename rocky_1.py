"""import win32api

avaliableDrives=win32api.GetLogicalDriveStrings()
print(avaliableDrives)
drives=[drivestr for drivestr in avaliableDrives.split('\000') if drivestr]
print(drives)"""


import pyodbc
import threading
import time
start=time.perf_counter()
print(start)
Server='HCL-02-27\SQLEXPRESS'
database='file_results'#in this database we can call any table by using cursor.execute(values=cursor.execute('select *from Rocky12')
username='admin'
password='Rakkesh@123'
#def complete():
cnxn=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+Server+';DATABASE='+database+';UID='+username+';PWD='+password)
print(cnxn)
cursor=cnxn.cursor()
print(cursor)
#cursor.execute("show databases")
#cursor.execute('''INSERT INTO  Rocky123 (NameOfFile,File_Location,SearchCount)values ('rakkesh','E:\Danger_boys\Selvam\Thiagu\Kombu\sabari',1)''')
#cnxn.commit()

#values=cursor.execute('select *from Rocky123')#cursor will store the table values
cursor.execute('select *from Rocky12')
result=cursor.fetchone()# by using this we can call only one data by using fetchone
#by using fetchall we call all the data
for i in result:#here we can call directly by using cursor
    print(i)

"""raki_1= []
for i in range(2):
    raki=threading.Thread(target=complete)
    raki.start()
    raki_1.append(raki)

for i in range(2):
    i.join()"""

#Threading

"""import time
start=time.perf_counter()
print(start)
def calculate():
    #return x+y
    a_1=int(input("enter the number"))
    b_1=int(input("enter the number"))
    c_1=a_1+b_1
    print(c_1)
    print("sleep for 5 seconds")
    time.sleep(5)
    print("completed sleep")
calculate()
calculate()
finish=time.perf_counter()
print(finish-start)"""
"""a=calculate(10,20)
b=calculate(30,40)
print(a)
print(b)"""

"""import time
import threading
start=time.perf_counter()
print(start)
def calculate():
    print("sleep for 5 seconds")
     print("completed sleep")

t1=threading.Thread(target=calculate)
t2=threading.Thread(target=calculate)

t1.start()
t2.start()

t1.join()
t2.join()
finish=time.perf_counter()
print(finish)
print(start)"""

import concurrent.futures
import time
start=time.perf_counter()
def calculate(sex):
    print("batting for {}".format(sex))
    time.sleep(sex)
    return "completed batting with in {}".format(sex)

with concurrent.futures.ThreadPoolExecutor() as executor:
    baby=[executor.submit(calculate, i*3) for i in range(3)]
    for baby_boy in concurrent.futures.as_completed(baby):
        print(baby_boy)
        print(baby_boy.result())

finish=time.perf_counter()
print(finish)


# Multithreding 
## When To use multithreding
### IO bound Task 
### Concrut exicution

import threading
import time

def print_number():
    for i in range(5):
        time.sleep(1)
        print(f"number of column {i}")

def print_letter():
    for letter in "abcde":
        time.sleep(1)
        print(f"Letter are {letter}")


# Creat multi thred
t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letter)

t=time.time()
t1.start()
t2.start()
# print_number()
# print_letter()

# wait for thred after to  complete 
t1.join()
t2.join()  # when first preority to complete thred after all code executing the

finished_time =time.time()-t
print(finished_time)
# print(time.ctime(t))  #here ctime use to provides to mm/date/year

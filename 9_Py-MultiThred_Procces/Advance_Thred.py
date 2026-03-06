## Multithreding with Thred poll exicuting

from concurrent.futures import ThreadPoolExecutor
import time 

def print_number(number):
    time.sleep(1)
    return f"Number : {number}"

numbes =[1,2,3,4,5]

with ThreadPoolExecutor(max_workers=3) as executer:
    results =executer.map(print_number,numbes)

for result in results:
    print(result)    
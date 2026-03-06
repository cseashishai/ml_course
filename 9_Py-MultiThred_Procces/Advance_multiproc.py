## Multiproccesing with Thred poll exicuting

from concurrent.futures import ProcessPoolExecutor
import time

def print_number(number):
    time.sleep(1) # here sleep working to exicuting time to get 1 sec
    return f"squre: {number*number}"

numbes =[1,2,3,4,5,12,13,14,15,16 ]

if __name__=="__main__": # it is naccesary that be use when you call multiproccess 

    with ProcessPoolExecutor(max_workers=3) as execute:
        results =execute.map(print_number,numbes)  # map use to be multiple cpu uses

    for result in results:
        print(result)   
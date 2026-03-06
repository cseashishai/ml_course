## Procces that run Parallel
## CPU -bound Task -task that perpform havy task (eg - Mathamatic computation ,datahandle)
## Parllel execution -Multiple core of the cpu

# if __name__=="__main__":  it is always to use it 

import multiprocessing
import time

def squre_num():
    for i in range(5):
        time.sleep(1)
        print(f"Square :{i*i}")

def cub_num():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cub is :{i * i * i}")        

if __name__=="__main__": #is used to ensure that certain code runs only when the Python file is executed directly

## Creat of two procces
    p1=multiprocessing.Process(target=squre_num)
    p2=multiprocessing.Process(target=cub_num)
    t =time.time()

    #start the procces 
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    t =time.time()
    final_time =time.time() - t
    print(final_time)
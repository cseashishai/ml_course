'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation

Factorial calculations, especially for large numbers, involve significant computational work. 
Multiprocessing can be used to distribute the workload across multiple CPU cores, 
improving performance.
'''
import multiprocessing
import math
import sys
import time


# Increse the maximum number to digit for linneur convertation
sys.set_int_max_str_digits(100000)

##function to compute factorial number is given is true


def factorial_number(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"factorial number {number} is {result}")
    return result

if __name__=='__main__':
    number=[5000,1000,6000,4000]

    start_time = time.time()

    ## creat a pool worker of  multiple proccess
    with multiprocessing.Pool() as pool:
        results=pool.map(factorial_number,number)

    end_time=time.time()

    print(f"result: {results}")
    print(f'time taken :{end_time-start_time} seconds')
    final_time =time.time() - start_time
    print(final_time)
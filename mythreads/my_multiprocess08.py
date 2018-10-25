from multiprocessing import Pool
import time

def f(n):
    return n * n

def run_with_processes():

   arr = [1,2,3,4,5,6]
   p = Pool()
   result = p.map(f, arr)
   print(result)

if __name__ == '__main__':
    run_with_processes()

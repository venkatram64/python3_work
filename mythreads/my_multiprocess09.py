from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for x in range(1000):
        sum += x * x
    return sum

def run_with_processes():
    t1 = time.time()
    p = Pool()
    result = p.map(f, range(100000))
    p.close()
    p.join()
    t2 = time.time()
    print("Time taken ", (t2 - t1))

    t3 = time.time()
    result = []

    for x in range(100000):
        result.append(f(x))

    print("Result is ", result)
    t4 = time.time()

    print("Serial processing is ", (t4 - t1))


if __name__ == '__main__':
    run_with_processes()

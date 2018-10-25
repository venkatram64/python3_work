import multiprocessing
import time


def square_it(num, q):
    for n in num:
        time.sleep(0.2)
        square = n * n
        print('Square of {} is {} '.format(n, square))
        q.put(square)



def run_with_processes():

    arr = [2, 3, 8, 9]
    start = time.time()
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=square_it, args=(arr,q))
    p.start()
    print('{} has started'.format('square_it'))
    p.join()
    end = time.time()
    print("Outside the process")
    while q.empty() is False:
        print(q.get())
    print('take take to complete the task :', str(end - start))


if __name__ == '__main__':
    run_with_processes()

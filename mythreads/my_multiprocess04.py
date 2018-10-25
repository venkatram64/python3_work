import multiprocessing
import time


def square_it(num, squre_result):

    print('Calculate square numbers. ')
    for idx, n in enumerate(num):
        time.sleep(0.2)
        square = n * n
        print('Square of {} is {} '.format(n, square))
        squre_result[idx] = square

    print("Within process")
    print(squre_result[:])



def run_with_processes():
    arr = [2, 3, 8, 9]
    start = time.time()
    squre_result = multiprocessing.Array('i', 4)
    p = multiprocessing.Process(target=square_it, args=(arr, squre_result))
    p.start()
    print('{} has started'.format('square_it'))
    p.join()
    end = time.time()
    print("Outside the process")
    print(squre_result[:])
    print('take take to complete the task :', str(end - start))


if __name__ == '__main__':
    run_with_processes()

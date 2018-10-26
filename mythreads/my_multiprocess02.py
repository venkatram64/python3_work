import multiprocessing
import time

squre_result = []
def square_it(num):
    global squre_result
    print('Calculate square numbers. ')
    for n in num:
        time.sleep(0.2)
        square = n * n
        print('Square of {} is {} '.format(n, square))
        squre_result.append(square)

    print("Within process ", squre_result)



def run_with_processes():
    arr = [2, 3, 8, 9]
    start = time.time()

    p = multiprocessing.Process(target=square_it, args=(arr,))
    p.start()
    print('{} has started'.format('square_it'))

    p.join()

    end = time.time()

    print("Outside the process ", squre_result)

    print('take take to complete the task :', str(end - start))


def run_without_processes():
    arr = [2, 3, 8, 9]
    start = time.time()
    square_it(arr)
    end = time.time()
    print('take take to complete the task :', str(end - start))


if __name__ == '__main__':
    #run_without_processes()
    run_with_processes()

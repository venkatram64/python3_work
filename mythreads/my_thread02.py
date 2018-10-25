
import threading
import time

def sleeper(n, name):
    print('Hi, I am {}. Going to sleep for 5 seconds\n'.format(name))
    time.sleep(n)
    print('{} has woken up from sleep\n'.format(name))


def run_threads():

    threads_list = []
    start = time.time()

    for i in range(5):
        t = threading.Thread(target=sleeper, name='thread{}'.format(str(i)),
                             args=(5, 'thread{}'.format(i)))
        t.start()
        print('{} has started'.format(t.name))
        threads_list.append(t)

    for t in threads_list:
        t.join()

    end = time.time()
    print('time taken: {}'.format(str(end - start)))
    print("All five threads completed their tasks. ")
    print("Main thread is executed. ")


def run_without_threads():
    start = time.time()

    for i in range(5):
        sleeper(5, 'thread{}'.format(i))

    end = time.time()
    print('time taken: {}'.format(str(end - start)))
    print("All five threads completed their tasks. ")
    print("Main thread is executed. ")


if __name__ == '__main__':
    #run_threads()
    run_without_threads()
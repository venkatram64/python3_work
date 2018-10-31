'''
This class is  generates a fib sequence
'''

class FibIter:

    def __init__(self, first=0, second=1, max=51):
        self.first = first
        self.second = second
        self.max = max


    def __iter__(self):
        return self

    def __next__(self):
        next_val = self.first + self.second
        if next_val > self.max:
            raise StopIteration()
        self.second = self.first
        self.first = next_val
        return next_val




if __name__ == '__main__':

    my_fib = FibIter()

    for i in my_fib:
        print(i)



class MyIterator:

    def __init__(self, num):
        self.num = num

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= self.num:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration



myIterObj = MyIterator(20)
myIter = iter(myIterObj)

for x in myIter:
    print(x)

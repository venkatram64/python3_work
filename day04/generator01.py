#Generator example

def square_numbers(nums):
    for i in nums:
        yield (i * i)


if __name__ == '__main__':

    nums_of_squares = square_numbers([1, 2, 3, 4, 5, 6])
    for num in nums_of_squares:
        print(num)


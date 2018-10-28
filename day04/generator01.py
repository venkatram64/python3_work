#Generator example

def square_numbers(nums):
    for i in nums:
        yield (i * i)


if __name__ == '__main__':

    squares_of_nums = square_numbers([1, 2, 3, 4, 5, 6])
    for num in squares_of_nums:
        print(num)


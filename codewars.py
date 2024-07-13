# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# For example, for [1, 2, 2] it should return 9 because 1**2 + 2**2 + 2**2 = 9

def square_sum(numbers):
    #your code here
    sum = 0
    for number in numbers:
        sum += number**2
    return sum

print(square_sum([1, 2]))

def square_sum_solution(numbers):
    test = (x ** 2 for x in numbers) # генератор <generator object square_sum_solution.<locals>.<genexpr> at 0x0000013A2607CD60>
    print(test)
    return sum(test)


print(square_sum_solution([1, 2]))

# Given two integers a and b, which can be positive or negative,
# find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.


def get_sum(a, b):
    if a > b:
        c = b, a+1
    else:
        c = a, b+1

    if a != b:
        return sum(list(range(*c)))
    elif a == b:
        return b

def get_sum_solution(a,b):
    return sum(range(min(a, b), max(a, b) + 1))

print(get_sum(4468, -541))
print(get_sum_solution(4567, -58))
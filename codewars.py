# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# For example, for [1, 2, 2] it should return 9 because 1**2 + 2**2 + 2**2 = 9

def square_sum(numbers):
    # your code here
    sum = 0
    for number in numbers:
        sum += number ** 2
    return sum


print(square_sum([1, 2]))


def square_sum_solution(numbers):
    test = (x ** 2 for x in
            numbers)  # генератор <generator object square_sum_solution.<locals>.<genexpr> at 0x0000013A2607CD60>
    print(test)
    return sum(test)


print(square_sum_solution([1, 2]))


# Given two integers a and b, which can be positive or negative,
# find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.


def get_sum(a, b):
    if a > b:
        c = b, a + 1
    else:
        c = a, b + 1

    if a != b:
        return sum(list(range(*c)))
    elif a == b:
        return b


def get_sum_solution(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


print(get_sum(4468, -541))
print(get_sum_solution(4567, -58))


# In this kata you will create a function that takes a list of non-negative integers and strings
# and returns a new list with the strings filtered out.
def filter_list(l):
    '''return a new list with the strings filtered out'''
    return [s for s in l if isinstance(s, int)]


print(filter_list([1, 2, 'a', 'b']))


# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
#
# If the function is passed a valid PIN string, return true, else return false.

def validate_pin(pin):
    if pin.isnumeric():
        if len(pin) == 4 or len(pin) == 6:
            return True
        else:
            return False
    return False


print(validate_pin("098765"))

def validate_pin_solution(pin):
    return len(pin) in (4, 6) and pin.isdigit()

def stray(arr):
    return min(arr, key=arr.count)
    # for i in arr: # мой варик
    #     if arr.count(i) == 1:
    #         return i

# Когда мы вызываем min(arr, key=arr.count), функция min() найдет элемент,
# для которого arr.count(x) минимален, то есть элемент с минимальным количеством вхождений.
print(stray([1, 1, 1, 3]))

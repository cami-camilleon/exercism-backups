def square(number):
    if number < 1 or number > 64:
        raise ValueError ("square must be between 1 and 64")
    
    sum = 1

    for i in range(1, number):
        sum = sum * 2

    return sum


def total():
    sum = 0

    for i in range(64):
        sum = sum + square(i+1)

    return sum

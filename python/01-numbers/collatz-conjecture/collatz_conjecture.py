def steps(number):
    if number < 1:
        raise ValueError('Only positive integers are allowed')

    num = number
    sum = 0

    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1

        sum = sum + 1

    return sum

#steps(12)
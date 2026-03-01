def square_root(number):
    for i in range(number):
        if number == 1:
            return 1
        if i * i > number:
            return i - 1

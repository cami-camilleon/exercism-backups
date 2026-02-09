def is_armstrong_number(number):
    sum = 0
    for item in str(number):
        sum = sum + int(item) ** len(str(number))

    return sum == number
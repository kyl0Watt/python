def is_armstrong(number):
    acc = 0
    for i in str(number):
        acc =+ int(i) ** len(str(number))
    return number == acc

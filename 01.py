import random


def random_average(n):
    numbers = []
    total = 0

    try:
        for n in range(n):
            numbers.append(random.randint(1, 100))
    except TypeError:
        print("Only numbers allowed as argument.")
        return
    except Exception as e:
        print(e)
        return

    for n in numbers:
        total += n

    try:
        print("Wylosowane liczby: " + str(numbers))
        return total / len(numbers)
    except ZeroDivisionError:
        print("Natural number required as parameter, greater than 0.")


print(random_average(0))

import math


def square(x):
    return math.ceil(x*x)


num_x = float(input("Введите длину стороны квадрата: "))
print(f"Площадь квадрата: {square(num_x)}")

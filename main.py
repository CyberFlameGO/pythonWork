import math
import pyperclip


def quad_calc(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        return None
    elif d == 0:
        x = (-b + math.sqrt(d)) / (2 * a)
        return x
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2


while True:
    a_val = float(input("Enter a: "))
    b_val = float(input("Enter b: "))
    c_val = float(input("Enter c: "))
    val1, val2 = quad_calc(a_val, b_val, c_val)
    val1 = round(val1, 2)
    val2 = round(val2, 2)
    print(val1, val2)
    pyperclip.copy(str(val1) + ", " + str(val2))

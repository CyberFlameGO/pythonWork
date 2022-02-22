import cmath

aval = int(input("Enter a: "))
bval = int(input("Enter b: "))
cval = int(input("Enter c: "))


def quad_calc(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        return None
    elif d == 0:
        x = (-b + cmath.sqrt(d)) / (2 * a)
        return x
    else:
        x1 = (-b + cmath.sqrt(d)) / (2 * a)
        x2 = (-b - cmath.sqrt(d)) / (2 * a)
        return x1, x2


print(quad_calc(aval, bval, cval))


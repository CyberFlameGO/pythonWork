"""
Math work
"""
import math
import numpy as np


def main():
    """
    Main function
    """
    match input("What rule do you wanna use? ").lower().strip():  # for now, this is for painful trig work, though if I
        # use this
        # project more,
        # I'll adapt the match-case to ask for the topic too
        case "cos":
            while True:
                b_val = float(input("Enter b: ").strip())
                c_val = float(input("Enter c: ").strip())
                angle_val = float(input("Enter angle in degrees: ").strip())
                print(cosine_rule(b_val, c_val, angle_val))
        case "invcos":
            while True:
                a_val = float(input("Enter a: ").strip())
                b_val = float(input("Enter b: ").strip())
                c_val = float(input("Enter c: ").strip())
                print(inverted_cos_rule(a_val, b_val, c_val))
        case "sin":
            while True:
                b_val = float(input("Enter b: ").strip())
                c_val = float(input("Enter c: ").strip())
                angle_val = float(input("Enter angle in degrees: ").strip())
                print(sine_rule(b_val, c_val, angle_val))
        case "area":
            while True:
                b_val = float(input("Enter b: ").strip())
                c_val = float(input("Enter c: ").strip())
                angle_val = float(input("Enter angle in degrees: ").strip())
                print(triangle_area(b_val, c_val, angle_val))
        case "y":
            pass
        case _:
            pass


def cosine_rule(b, c, angle):
    """
    Cosine rule
    :param b:
    :type b:
    :param c:
    :type c:
    :param angle: Angle in degrees
    :type angle:
    :return:
    :rtype:
    """
    return math.sqrt((b ** 2 + c ** 2 - 2 * b * c * math.cos(angle * math.pi / 180)))


def inverted_cos_rule(a, b, c):
    """
    Inverted cosine rule in degrees
    """
    return math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180 / math.pi


def sine_rule(b, c, angle):
    """
    Sine rule
    :param b:
    :type b:
    :param c:
    :type c:
    :param angle: Angle in degrees
    :type angle:
    :return:
    :rtype:
    """
    return math.sqrt((b ** 2 + c ** 2 - 2 * b * c * math.sin(angle * math.pi / 180)))


def triangle_area(b, c, angle):
    """
    Triangle area
    :param b:
    :type b:
    :param c:
    :type c:
    :param angle: Angle in degrees
    :type angle:
    :return:
    :rtype:
    """
    return 0.5 * b * c * math.sin(angle * math.pi / 180)


if __name__ == '__main__':
    main()

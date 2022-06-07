"""
Blood donor programme program
"""

checking: bool = True

while checking:
    try:
        donor_age = int(input("Enter your age: "))
        checking = False
    except ValueError:
        print("Please enter a number")


if donor_age < 16 or donor_age > 65:
    print("You are not eligible to donate blood at this age.")
else:
    print("You are eligible to donate blood.")

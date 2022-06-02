def calc(a, r, n):
    return (a * ((r ** n) - 1)) / (r - 1)


def main():
    while True:
        an = float(input("Enter the amount: "))
        rn = float(input("Enter the rate: "))
        nn = int(input("Enter n: "))
        print(calc(an, rn, nn))


if __name__ == "__main__":
    main()

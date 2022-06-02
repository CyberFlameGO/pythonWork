def calc(a, d, n):
    return a + (n - 1) * d


def main():
    while True:
        an = float(input("Enter the amount: "))
        dn = float(input("Enter the diff: "))
        nn = int(input("Enter n: "))
        print(calc(an, dn, nn))


if __name__ == "__main__":
    main()

def calc(a, d, n):
    return n/2 * (a + (a + d) * n)


def main():
    while True:
        an = float(input("Enter the amount: "))
        dn = float(input("Enter the diff: "))
        nn = int(input("Enter n: "))
        print(calc(an, dn, nn))


if __name__ == "__main__":
    main()

from circle import Circle

def main():
    c1 = Circle(5)
    c2 = Circle(7)

    print("Comparisons:")
    print("c1 == c2:", c1 == c2)
    print("c1 <  c2:", c1 < c2)
    print("c1 <= c2:", c1 <= c2)
    print("c1 >  c2:", c1 > c2)
    print("c1 >= c2:", c1 >= c2)

    print("\nArithmetic:")
    c3 = c1 + 3
    c4 = c2 - 2
    print("c1 + 3 =", c3)
    print("c2 - 2 =", c4)

    print("\nIn-place:")
    c1 += 2
    print("c1 after += 2 ->", c1)

    c2 -= 1
    print("c2 after -= 1 ->", c2)


if __name__ == "__main__":
    main()

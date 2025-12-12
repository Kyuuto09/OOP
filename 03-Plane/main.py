from airplane import Airplane

def main():
    a1 = Airplane("Boeing 737", 180, 50)
    a2 = Airplane("Airbus A320", 160, 120)

    print("Equality (same type?):")
    print(a1 == a2)

    print("\nComparisons by max passengers:")
    print("a1 > a2:", a1 > a2)
    print("a1 < a2:", a1 < a2)
    print("a1 >= a2:", a1 >= a2)
    print("a1 <= a2:", a1 <= a2)

    print("\nArithmetic (return new objects):")
    a3 = a1 + 20
    a4 = a2 - 30
    print(a3)
    print(a4)

    print("\nIn-place modifications:")
    a1 += 10
    print("a1 after += 10:", a1)

    a2 -= 40
    print("a2 after -= 40:", a2)


if __name__ == "__main__":
    main()

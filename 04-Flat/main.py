from flat import Flat

def main():
    f1 = Flat(50.0, 60000)
    f2 = Flat(45.0, 55000)
    f3 = Flat(50.0, 75000)

    print("Equality / Inequality:")
    print(f"f1 == f2: {f1 == f2}")
    print(f"f1 == f3: {f1 == f3}")
    print(f"f1 != f3: {f1 != f3}")

    print("\nPrice comparison:")
    print(f"f1 > f2: {f1 > f2}")
    print(f"f2 < f3: {f2 < f3}")
    print(f"f1 <= f3: {f1 <= f3}")
    print(f"f3 >= f1: {f3 >= f1}")

if __name__ == '__main__':
    main()

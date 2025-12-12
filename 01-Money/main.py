from money import Money, Product

def main():
    # Create a Money instance
    price = Money(10, 50)  # 10.50

    # Create a product
    apple = Product("Apple", price)

    print("Before price reduction:")
    print(apple)

    # Reduce price
    apple.reduce_price(minor=30)  # reduce by 0.30

    print("\nAfter price reduction:")
    print(apple)


if __name__ == "__main__":
    main()
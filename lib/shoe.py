class Shoe:
    def __init__(self, brand, size, color, price):
        if not brand:
            raise ValueError("Brand cannot be empty")

        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size <= 0:
            raise ValueError("Size must be a positive integer")

        if not color:
            raise ValueError("Color cannot be empty")

        if not (isinstance(price, (int, float))):
            raise TypeError("Price must be a number")
        if price < 0:
            raise ValueError("Price must be non-negative")

        self.brand = brand
        self.size = size
        self.color = color
        self.price = price

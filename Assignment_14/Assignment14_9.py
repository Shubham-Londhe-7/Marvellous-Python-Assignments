class Product:
    def __init__(self, product_name, product_price):
        self.name = product_name
        self.price = product_price
    
    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        return False

def main():
    obj1 = Product('pen', 10)
    obj2 = Product('pencil', 10)
    obj3 = Product('eraser', 5)

    print(obj1 == obj2)  # True: 10 == 10
    print(obj1 == obj3)  # False: 10 != 5
    print(obj2 == obj3)  # False: 10 != 5

if __name__ == "__main__":
    main()

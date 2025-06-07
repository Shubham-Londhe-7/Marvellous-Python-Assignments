
class Book:
    def __init__(self):
        self.__price = 0

    def setPrice(self, value):
        self.__price = value
    
    def getPrice(self):
        print("Price is :",self.__price)

def main():
    obj1 = Book()
    obj1.setPrice(100)
    obj1.getPrice()

    obj2 = Book()
    obj2.setPrice(200)
    obj2.getPrice()

if __name__ == "__main__":
    main()
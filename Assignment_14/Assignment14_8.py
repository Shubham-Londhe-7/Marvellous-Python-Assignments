
class Vehicle:
    def start(self):
        print("Inside Vahicle(Base) start")
    
class Car(Vehicle):
    def start(self):
        super().start()
        print("Inside Car(Derived) start")

def main():
    obj1 = Car()
    obj1.start()
    print("--------------------------")
    obj2 = Vehicle()
    obj2.start()

if __name__ == "__main__":
    main()
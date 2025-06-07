class Person:
    def __init__(self, per_name, per_age):
        self.name = per_name
        self.age = per_age

class Teacher(Person):
    def __init__(self, per_name, per_age, sub, per_salary):
        super().__init__(per_name, per_age)  # class Person constructor(__init__) call
        self.subject = sub
        self.salary = per_salary

    def Display(self):
        print("Name of teacher : " + self.name)
        print("Age is :", self.age)
        print("Subject : " + self.subject)
        print("Salary :", self.salary)

def main():
    obj1 = Teacher("Shubham", 45, "Mathematics", 10000)
    obj1.Display()

if __name__ == "__main__":
    main()

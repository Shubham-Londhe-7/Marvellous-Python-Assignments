
class Employee:
    def __init__(self, emp_name, ID, emp_salary):
        self.name = emp_name
        self.emp_id = ID
        self.salary = emp_salary

    def Display(self):
        print("Emplyee name : "+ self.name)
        print("Employee ID :",self.emp_id)
        print("Employee salary :",self.salary)

def main():
    obj1 = Employee("Shubham",1,10000)
    obj1.Display()

if __name__ == "__main__":
    main()
class Employee:
    def __init__(self, Salary, Department, Name):
        self.__salary = Salary  #private
        self._department = Department      #protected
        self.name = Name        #public
    

    def Display(self):
        print("Name : ", self.name)
        print("Department : ", self._department)
        print("Salary : ", self.__salary)      
    

def main():
    obj = Employee(10000, 'HR', 'Virat Kohli')
    obj.Display()       # All the members can be accessed within the method of that class

    print(obj.name)         #public member is accessible with it's object
    print(obj._department)  #protected is also accessed
    # print(obj.__salary)     #private is not accessible
    
    

if __name__ == "__main__":
    main()
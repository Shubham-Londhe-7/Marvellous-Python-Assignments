
class Student:
    School_Name = "Primary School"

    def __init__(self, std_name, std_rollNo):
        self.name = std_name
        self.roll_no = std_rollNo
    
    def displayDetails(self):
        print("Name of Student : "+self.name)
        print("Roll no of student :",self.roll_no)
        print("Name of School : "+Student.School_Name)

    def changeSchool(self,school):
        Student.School_Name = school

def main():
    obj1 = Student("Shubam",61)
    obj1.displayDetails()

    obj1.changeSchool("High School")
    obj1.displayDetails()

if __name__ == "__main__":
    main()
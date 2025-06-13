
def main():
    fobj = open("student.txt","w")
    fobj.write("Shubham\n")
    fobj.write("Aayush\n")
    fobj.write("Vipul\n")
    fobj.write("Prithvi\n")
    fobj.write("Yash\n")

    fobj.close()

if __name__ == "__main__":
    main()
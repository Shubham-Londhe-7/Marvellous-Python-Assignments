
class BookStore:
    NoOfBooks = 0

    def __init__(self, bookName, authorName):
        self.Name = bookName
        self.Author = authorName
        BookStore.NoOfBooks += 1
    
    def Display(self):
        print("Name of Book is : "+self.Name)
        print("Name of Author is : "+self.Author)
        print("Number of books :",BookStore.NoOfBooks)

def main():
    Obj1 = BookStore("Linux System Programming","Robert Love")
    Obj1.Display()
    print("-----------------------------------------------------------------")
    Obj2 = BookStore("C Programming","Dennis Ritchie")
    Obj2.Display()

if __name__ == "__main__":
    main()
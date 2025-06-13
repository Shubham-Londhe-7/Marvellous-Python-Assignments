import os

def Display(fname):
    fname = os.path.abspath(fname)

    if(os.path.isfile(fname) == False):
        print("No file present")

    fobj = open(fname, 'r')
    lineList = fobj.readlines()
    
    for line in lineList:
        # print(line)
        line = line.replace("\n", "")
        words = line.split(" ")
        Cnt = 0
        for word in words:
            Cnt = Cnt + 1
        if(Cnt >= 5):
            print(line)


    fobj.close()



def main():
    print("The lines which contain more than 5 words are: ")
    Display('source.txt')

if __name__ == "__main__":
    main()
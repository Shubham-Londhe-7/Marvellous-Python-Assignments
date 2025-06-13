import schedule
import time
import datetime

def Display():
    fobj = open("Marvellous.txt","a")
    data = time.asctime()
    fobj.write(data)
    fobj.write("\n")
    fobj.close()
    print("Running...")

def main():
    fobj = open("Marvellous.txt","w")
    fobj.close()
    schedule.every(5).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
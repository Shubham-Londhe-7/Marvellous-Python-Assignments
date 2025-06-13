import schedule
import time
import datetime

def Display():
    print(datetime.datetime.now())

def main():
    print("This script is used to print current date and time evry minute")
    schedule.every(1).minute.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ == "__main__":
    main()
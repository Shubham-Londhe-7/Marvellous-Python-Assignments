import schedule
import time

def Display():
    print("Jay Ganesh...")

def main():
    print("This script prints 'Jay Ganesh...' in every 2 seconds")
    schedule.every(2).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ == "__main__":
    main()
import schedule
import time

def Display():
    print("Do coding..!")

def main():
    print("This script prints 'Do coding..!' in every 30 minutes")
    schedule.every(30).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ == "__main__":
    main()
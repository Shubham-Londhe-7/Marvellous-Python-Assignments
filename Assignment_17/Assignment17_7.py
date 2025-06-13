
import datetime
import schedule
import time

def File_backup():
    print("Backup completed")
    fobj = open("backup_log.txt","a")
    current_time = time.asctime()
    fobj.write("Backup done at : \t")
    fobj.write(current_time)
    fobj.write("\n\n\n\n")
    fobj.close()
    print("running...")
    

def main():
    fobj = open("backup_log.txt","w")
    fobj.close()
    schedule.every(1).hour.do(File_backup)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
import psutil
import sys
import os
import time
import smtplib
from email.message import EmailMessage

def MakeDirectoryLog(DirectoryName):
    timestamp = time.ctime()
    FileName = "Process%s"%timestamp
    FileName = FileName.replace(":","")
    FileName = FileName.replace(" ","_")
    FileName = os.path.join(DirectoryName,FileName)

    fobj = open(FileName,"w")
    fobj.write('This file is created at ')
    fobj.write(timestamp+"\n")
    fobj.close()

    return FileName

def ProcInfoLog(File):
    Border = "-"*80
    fobj = open(File,'a')
    fobj.write(Border+"\n")
    fobj.write("\t\t Current running processes \t\t")
    fobj.write("\n")
    fobj.write(Border+"\n")

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['name','pid','username'])
        fobj.write(str(info))
        fobj.write("\n\n")
    
    fobj.write(Border+"\n")
    fobj.write(Border+"\n")

    fobj.close()

    return File


def SendMail(DirectoryName, recaiver_mail):
    FileName = MakeDirectoryLog(DirectoryName)
    LogFile = ProcInfoLog(FileName)

    sender_mail = "roronoagreatestswordsman@gmail.com"
    sender_password = "ijaz httg zodv edda"

    body = "Information about running processes"
    # Create email
    msg = EmailMessage()
    msg['Subject'] = "Running Process Log"
    msg['From'] = sender_mail
    msg['To'] = recaiver_mail
    msg.set_content(body)

    # Attach file
    fobj = open(LogFile, 'rb')
    msg.add_attachment(fobj.read(), maintype='application', subtype='octet-stream', filename=fobj.name)

    # Send email
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(sender_mail, sender_password)
    smtp.send_message(msg)
    smtp.quit()

    print("Email sent successfully!")


def main():
    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This automation script is used to send email with logfile contains information about running process")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("python ScriptName.py  DirectoryName  ReceiverEmail")
        
    elif(len(sys.argv) == 3):
        os.mkdir(sys.argv[1])
        SendMail(sys.argv[1], sys.argv[2])

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == "__main__":
    main()
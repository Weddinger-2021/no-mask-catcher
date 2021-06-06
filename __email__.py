import smtplib
from datetime import datetime
import calendar

my_date = datetime.now()
my_day = calendar.day_name[my_date.weekday()]

def send_email():
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("pypandas.mask.catcher@gmail.com" , "key") # need key

    subject = "No Mask Warning "
    body = "Dear esteemed security department ...."
    
    msg = f'Subject: {subject}\n {my_date}/{my_day}\n\n {body}'
    print(msg)
    
    s.sendmail(
        'pypandas.mask.catcher@gmail.com',
        'muhannadmughrabi@gmail.com',
        msg
    )
    print("EMAIL HAS BEEN SENT!") # should fire when email sent succesfully 



    
if __name__ == "__main__":
    send_email()

import os
import face_recognition
import cv2
from face_recognition.api import face_encodings
import numpy as np
import re 
import json as j
import datetime
import calendar
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


date_time = datetime.datetime.now()
formatted_date = date_time.strftime("%Y-%m-%d")
formatted_time = date_time.strftime("%H:%M:%S")
formatted_full = formatted_date + f"-{formatted_time}"
stripped_time = formatted_time.replace(":" , "")
stripped_date = formatted_date.replace("-" , "")
stripped_full = stripped_date + f"-{stripped_time}"
my_day = calendar.day_name[date_time.weekday()]

pics = []
known_face_encodings = []
file = 'employees.json'



def employee(index):
    """
    A function that takes an index and return the employee info
    """
    # print("It's a picture of me!")
    info = json_data[index]
    send_email(info, formatted_full , my_day)

def send_email(info = None, f_full="" , day=""):
    with open(cap_frame_name, 'rb') as f:
        img_data = f.read()
        f.close()
    
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("pypandas.catcher@gmail.com" , "kzmclxljulmpvaxg") # need key for muhannd scqokvmkxwtqgvoe   muhannadalmughrabi233@gmail.com
    calling = "Mr"
    gend = "his"
    msg = MIMEMultipart()
    msg['Subject'] = 'No Mask Warning'
    
    if info != None:

        if info["Gender"] == "female": 
            calling = "Mrs"
            gend = "her"
    
        body = MIMEText(f'''      Dear esteemed security department, 
        Our system detected {calling}. {info["Name"]} from {info["Department"]} department
        {gend} job id {info["Job_Id"]} who is not wearing a mask at {f_full} on {day}, 
        please check attached photo below''')

    else: 

        body = MIMEText(f'''      Dear esteemed security department, 
    Our system detected a visitor who is not wearing a mask at {f_full}, 
    please check attached photo below.''')
    
    msg.attach(body)
    image = MIMEImage(img_data, name=os.path.basename(cap_frame_name))
    msg.attach(image)
    s.sendmail(
        'pypandas.catcher@gmail.com',
        'pypandas.mask.catcher@gmail.com', 
        msg.as_string()
    )
    s.quit()
    print(msg)
    print("EMAIL HAS BEEN SENT!") # should fire when email sent succesfully 

def recognize_face(known_face_encodings):
    """
    takes a list of encoded pictures and compare them with the incoming frame from the video
    to recognize if he/she was an employee or not.
    """
    face_from_cam = face_recognition.load_image_file(cap_frame_name)
    face_from_cam_encodings = face_recognition.face_encodings(face_from_cam)[0]
    cout = 0
    for face in known_face_encodings: 
        results = face_recognition.compare_faces([face], face_from_cam_encodings)
        name  = 'unknown'
        if results[0] == True:
            employee(cout)
            # print("it is an employee")
            break
        cout += 1
    if results[0] == False:
        # print ("not employee")
        send_email(None, formatted_full , my_day)

        # for none employers code. take a screen shot and send an e-mail

### possibly in recognize_face function 
def encode_known_pics(pics):
    """
    A function that takes employees pics list and encode them
    """
    for pic in pics:
        known_face = face_recognition.load_image_file(pic)
        known_face_encodings.append(face_recognition.face_encodings(known_face)[0])
    recognize_face(known_face_encodings)

## read json file & append the values to lists
def open_files(file = 'employees.json'):

    with open(file, 'r') as jd:
        global json_data
        json_data = j.load(jd)
        for p in json_data:
            pics.append(p["photos"])
        encode_known_pics(pics)
    
def detect_mask():
    """
    A function to detect if a person is wearing a mask or not
    """
    pass

def red_alert():
    pass



def access_cam():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=1.0, fy=1.0, interpolation=cv2.INTER_AREA)
        cv2.imshow('Input', frame)

        c = cv2.waitKey(1)
        if c == ord('c'): ## calls a screen shot function 
            global cap_frame_name
            cap_frame_name = f"./assets/{stripped_full}.jpg"
            cv2.imwrite(cap_frame_name, frame)
            open_files(file)

        if c == ord('b'): ## press Esc to exit 
            break

    cap.release()
    cv2.destroyAllWindows()

access_cam()


# if __name__ == "__main__":
#     encode_known_pics(pics)
#     access_cam()


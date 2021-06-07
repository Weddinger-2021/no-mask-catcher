import face_recognition
import cv2
from face_recognition.api import face_encodings
import numpy as np
import re 
import json as j
import datetime

date_time = datetime.datetime.now()
pics = []
known_face_encodings = []



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
            cap_frame_name = f'./assets/{date_time}.jpg'
            cv2.imwrite(cap_frame_name, frame)

        if c == ord('b'): ## press Esc to exit 
            break

    cap.release()
    cv2.destroyAllWindows()

access_cam()
# frame from the cv
face_from_cam = face_recognition.load_image_file(cap_frame_name)
face_from_cam_encodings = face_recognition.face_encodings(face_from_cam)[0]

def employee(index):
    """
    A function that takes an index and return the employee info
    """
    # print("It's a picture of me!")
    info = json_data[index]
    send_email(info, date_time)

def send_email(info = None, d_time = '9:00'):
    calling = "Mr"
    gend = "his"
    if info != None:

        if info["Gender"] == "female": 
            calling = "Mrs"
            gend = "her"

        print(f'''      Dear esteemed security department, 
        Our system detected {calling}. {info["Name"]} from {info["Department"]} department
        {gend} job id {info["Job_Id"]} who is not wearing a mask at {d_time}, 
        please check attached photo below.{cap_frame_name}''')
        ### the correct email validation and connection

    else: 
        print(f'''      Dear esteemed security department, 
    Our system detected a visitor who is not wearing a mask at {d_time}, 
    please check attached photo below.{cap_frame_name}''')
        ### the correct email validation and connection

def recognize_face(known_face_encodings):
    """
    takes a list of encoded pictures and compare them with the incoming frame from the video
    to recognize if he/she was an employee or not.
    """
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
        send_email(None, date_time)
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
with open('employees.json', 'r') as jd:
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


# if __name__ == "__main__":
#     encode_known_pics(pics)
#     access_cam()

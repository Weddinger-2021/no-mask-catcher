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

# frame from the cv
face_from_cam = face_recognition.load_image_file('./assets/noor.jpg')
face_from_cam_encodings = face_recognition.face_encodings(face_from_cam)[0]

def employee(index):
    """
    A function that takes an index and return the employee info
    """
    pass


def send_email(info = None, d_time = '9:00'):
    pass

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
            print("it is an employee")
            break
        cout += 1
    if results[0] == False:
        print ("not employee")
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
    

def detect_mask():
    """
    A function to detect if a person is wearing a mask or not
    """
    pass

def red_alert():
    pass



if __name__ == "__main__":
    encode_known_pics(pics)

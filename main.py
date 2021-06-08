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
import tensorflow
# from tensorflow.keras.models import load_module
from tensorflow.keras import models
from tensorflow.keras.models import save_model, load_model


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
            detect_screen = detect_mask(cap_frame_name)
            if detect_screen > 0.5:
#                 state = False
                return cap_frame_name
            elif detect_screen ==0:
                print("Retry Again")
            else:
#                 return cap_frame_name
                print("Welcome!")

        if c == ord('b'): ## press Esc to exit 
            break

    cap.release()
    cv2.destroyAllWindows()

# access_cam()
# frame from the cv
# face_from_cam = face_recognition.load_image_file(cap_frame_name)
# face_from_cam_encodings = face_recognition.face_encodings(face_from_cam)[0]

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


def detect_mask(screenshot):
    """
    A function to detect if a person is wearing a mask or not
    """
    face_model = cv2.CascadeClassifier('data_set/convs/haarcascade_frontalface_default.xml')
    img = cv2.imread(screenshot)

    img = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)

    faces = face_model.detectMultiScale(img,scaleFactor=1.1, minNeighbors=4)

    out_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

#     for (x,y,w,h) in faces:
#         cv2.rectangle(out_img,(x,y),(x+w,y+h),(0,0,255),1)
        
    model = load_model("./saved_model", compile = True)

    sample_mask_img = cv2.imread(screenshot)
    sample_mask_img = cv2.resize(sample_mask_img,(128,128))
    sample_mask_img = np.reshape(sample_mask_img,[1,128,128,3])
    sample_mask_img = sample_mask_img/255.0
    model.predict(sample_mask_img)
    mask_label = {0:'OK!',1:'Busted'}
    dist_label = {0:(0,255,0),1:(255,0,0)}
    MIN_DISTANCE = 0

    if len(faces)>=1:
        label = [0 for i in range(len(faces))]
        for i in range(len(faces)-1):
            for j in range(i+1, len(faces)):
                dist = distance.euclidean(faces[i][:2],faces[j][:2])
                if dist<MIN_DISTANCE:
                    label[i] = 1
                    label[j] = 1
        new_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) #colored output image
        for i in range(len(faces)):
            (x,y,w,h) = faces[i]
            crop = new_img[y:y+h,x:x+w]
            crop = cv2.resize(crop,(128,128))
            crop = np.reshape(crop,[1,128,128,3])/255.0
            mask_result = model.predict(crop)
            cv2.putText(new_img,mask_label[round(mask_result[0][0])],(x, y+90),             cv2.FONT_HERSHEY_SIMPLEX,0.5,dist_label[label[i]],2)
            cv2.rectangle(new_img,(x,y),(x+w,y+h),dist_label[label[i]],1)
        return mask_result
            
    else:
        print("Cannot detect face")
        return 0  
        
    

def red_alert():
    pass


if __name__ == "__main__":
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
    # longest pasth: access_cam -> detect_mask() -> encode_know_pics -> recognize_face -> employee -> Email #3
    cap_frame = access_cam() # path to screenshot #1
    face_from_cam = face_recognition.load_image_file(cap_frame)
    face_from_cam_encodings = face_recognition.face_encodings(face_from_cam)[0]
    ## read json file & append the values to lists
    with open('employees.json', 'r') as jd:
        json_data = j.load(jd)
        for p in json_data:
            pics.append(p["photos"])
        encode_known_pics(pics) 
    
    
    
    


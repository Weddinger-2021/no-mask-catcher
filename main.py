import face_recognition
import cv2
from face_recognition.api import face_encodings
import numpy as np
import re 
import json as j
import datetime

date_time = datetime.datetime.now()
pics = []
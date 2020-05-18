import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from time import sleep

def encode_face(image):
    face = fr.load_image_file(image)
    encoding = fr.face_encodings(face)[0]
    # print(list(encoding))
    return encoding

def resolve_image(image,all_encodings,all_id):
    cur_image_encoding = encode_face(image)
    matches = fr.compare_faces(all_encodings,cur_image_encoding)
    face_distances = fr.face_distance(all_encodings,cur_image_encoding)
    best_match_index = np.argmin(face_distances)
    id = None
    if matches[best_match_index]:
        id = all_id[best_match_index]
    return id




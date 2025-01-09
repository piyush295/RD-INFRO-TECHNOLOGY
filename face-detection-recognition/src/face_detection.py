from keras.models import load_model
import cv2
import numpy as np

class FaceDetector:
    def __init__(self, model_path):
        self.model = load_model(model_path)

    def detect_faces(self, frame):
        # Preprocess the frame for the model
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.model.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
        return faces

def draw_bounding_boxes(frame, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return frame
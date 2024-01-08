import cv2
import numpy
import time
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        print(f"Error reading frame from camera. Attempting to reconnect...")
        time.sleep(3)
        continue
    print("---------")
    print(type(frame))


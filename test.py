import os
import cv2
import threading
import time
from datetime import datetime

# RTSP stream URLs
rtsp_streams = [
    "rtsp://admin:ADMIN2022@81.149.241.73:1024/Streaming/Channels/101",
    "rtsp://admin:ADMIN2022@81.149.241.73:554/Streaming/Channels/101",
    # Add more stream URLs here as needed
]

# Function to capture video frames from the RTSP stream
class Camera():
    def __init__(self):
        self.rtsp_stream = rtsp_streams[0]
        cap = cv2.VideoCapture(self.rtsp_stream)
        self.flag_save = False
        self.flag_quit = False

        while True:
            ret, frame = cap.read()
            if not ret:
                print(f"Error reading frame from camera. Attempting to reconnect...")
                time.sleep(3)
                continue
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break        
        
            if not os.path.exists("frames"):
                os.mkdir("frames")
            # press 's' to break out of the loop
            if (cv2.waitKey(1) & 0xFF == ord('s')) | self.flag_save == True:
                cv2.imwrite(os.path.join("frames", f"Image_{time.time()}.png"), frame)
            if (cv2.waitKey(1) & 0xFF == ord('q')) | self.flag_quit == True:
                break

    def save_frames(self):
        self.flag_save = True
    def quit_frames(self):
        self.flag_quit = True
if __name__ == "__main__":
    camera = Camera()
    camera.save_frames()
    
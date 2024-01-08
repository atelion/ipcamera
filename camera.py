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

# Define the output file names for each camera
output_files = [
    "camera_1.avi",
    "camera_2.avi",
    # Add more output file names here as needed
]

frame_saving_reducer_factor = 3
frame_flag = [False for _ in range(len(rtsp_streams))]

# Function to capture video frames from the RTSP stream
def capture_frames(cap, index):
    # Video reader
    # cap = cv2.VideoCapture(rtsp_streams[index])

    while True:
        ret, frame = cap.read()
        if not ret:
            print(f"Error reading frame from camera {index}. Attempting to reconnect...")
            time.sleep(3)
            continue
        frames_buffer[index] = frame
        frame_flag[index] = True

# Function to save screenshot when 's' key is pressed
def save_screenshot(index):
    while True:
        if cv2.waitKey(1) & 0xFF == ord('s'):
            screenshot = frames_buffer[index]
            cv2.imshow(screenshot)
            if screenshot is not None:
                current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                screenshot_name = f"screenshot_{index}_{current_time}.png"
                cv2.imwrite(screenshot_name, screenshot)
                print(f"Screenshot saved: {screenshot_name}")

# Initialize frames buffer
frames_buffer = [None] * len(rtsp_streams)

# Create and start threads for capturing frames and saving screenshots
capture_threads = []
save_screenshot_threads = []

for i in range(len(rtsp_streams)):
    # Video reader
    cap = cv2.VideoCapture(rtsp_streams[i])

    # Get the video frame width and height
    frame_width = int(cap.get(3)) // frame_saving_reducer_factor
    frame_height = int(cap.get(4)) // frame_saving_reducer_factor

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    saving_video_name = output_files[i]

    # out = cv2.VideoWriter(saving_video_name, fourcc, 30.0, (frame_width, frame_height))

    capture_thread = threading.Thread(target=capture_frames, args=(cap, i))
    save_screenshot_thread = threading.Thread(target=save_screenshot, args=(i,))

    capture_threads.append(capture_thread)
    save_screenshot_threads.append(save_screenshot_thread)

    capture_thread.start()
    save_screenshot_thread.start()

# Wait for all threads to finish
for capture_thread, save_screenshot_thread in zip(capture_threads, save_screenshot_threads):
    capture_thread.join()
    save_screenshot_thread.join()

print("Video capture and screenshot saving completed for all cameras.")

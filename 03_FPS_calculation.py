import cv2
import time

def calculate_and_print_fps(frame_count, start_time):
    # Calculate and print FPS
    elapsed_time = time.time() - start_time
    fps = frame_count / elapsed_time
    print(f"FPS: {fps:.2f}")

    # Reset counters
    return 0, time.time()

# Open a video capture object (0 is the default camera)
cap = cv2.VideoCapture(0)

# Initialize variables for FPS calculation
frame_count = 0
start_time = time.time()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame.")
        break

    # Your image processing or face detection code goes here
    # For example, convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate and print FPS every 30 frames
    frame_count += 1
    if frame_count % 30 == 0:
        frame_count, start_time = calculate_and_print_fps(frame_count, start_time)

    # Display the frame
    cv2.imshow('Frame', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

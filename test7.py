import cv2
import tkinter as tk
from tkinter import Button
from threading import Thread
from datetime import datetime

# Global variables
recording = False
out = None
cap = None

def start_camera():
    """Initialize the webcam and start video capture."""
    global cap
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    def show_frames():
        global recording, out
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture video frame. Exiting...")
                break

            # Write the frame to the video file if recording
            if recording and out:
                out.write(frame)

            # Display the frame in a window
            cv2.imshow("Webcam Video", frame)

            # Exit if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                stop_camera()
                break

    # Start a thread for displaying video frames
    Thread(target=show_frames, daemon=True).start()

def toggle_recording():
    """Start or stop recording."""
    global recording, out
    if not recording:
        # Generate filename with date and time
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"recorded_{current_time}.avi"
        print(f"Recording started: {filename}")

        # Define codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))
        recording = True
    else:
        print("Recording stopped.")
        recording = False
        if out:
            out.release()
            out = None

def stop_camera():
    """Release resources and close all windows."""
    global cap, out, recording
    if cap:
        cap.release()
    if recording and out:
        out.release()
    cv2.destroyAllWindows()
    print("Camera stopped.")

# Create the GUI
root = tk.Tk()
root.title("Webcam Recorder with Timestamp")

# Start button
start_btn = Button(root, text="Start Camera", command=start_camera, width=20)
start_btn.pack(pady=10)

# Record button
record_btn = Button(root, text="Record/Stop Recording", command=toggle_recording, width=20)
record_btn.pack(pady=10)

# Stop button
stop_btn = Button(root, text="Stop Camera", command=stop_camera, width=20)
stop_btn.pack(pady=10)

# Run the GUI loop
root.mainloop()

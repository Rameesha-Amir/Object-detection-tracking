Real-Time Object Detection and Tracking

A real-time object detection and tracking system using Python, OpenCV, YOLOv8, and Deep SORT. Detects objects from a webcam or video and assigns each one a unique tracking ID.

Tech Stack

Python, OpenCV, YOLOv8, Deep SORT

How It Works
OpenCV captures video from the webcam or a video file, frame by frame.
Each frame is passed to the YOLOv8 model, which detects objects and draws bounding boxes around them.
Deep SORT takes these detections and tracks them across frames, giving each object a unique ID that stays the same as long as the object is visible.
The final output is displayed live, showing bounding boxes, object labels, and tracking IDs.
How to Run
Install dependencies: pip install -r requirements.txt
Go to src folder: cd src
Run: python main.py
Press 'q' to quit
Features
Real-time detection using YOLOv8
Object tracking with unique IDs using Deep SORT
Works with webcam or video file
Internship Task

This project was built as part of my internship task at CodeAlpha.

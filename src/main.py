import cv2
import time
from detector import ObjectDetector
from tracker import ObjectTracker
from utils import draw_box, draw_fps

def main():
    # Initialize detector and tracker
    detector = ObjectDetector(model_path="../models/yolov8n.pt", confidence_threshold=0.5)
    tracker = ObjectTracker(max_age=30)

    # Open webcam (0 = default camera). Change to a file path for a video file.
    video_source = "../videos/Video_Sample.mp4" # or "../videos/sample_video.mp4"
    cap = cv2.VideoCapture(video_source)

    if not cap.isOpened():
        print("Error: Could not open video source.")
        return

    prev_time = 0
    fail_count = 0
    max_fail_count = 30  # allow some bad frames before giving up

    while True:
        ret, frame = cap.read()

        if not ret:
            fail_count += 1
            if fail_count > max_fail_count:
                print("Camera stopped responding. Exiting.")
                break
            continue  # skip this frame and try again

        fail_count = 0  # reset once we get a good frame

        # Step 1: Detect objects in the current frame
        detections = detector.detect(frame)

        # Step 2: Track detected objects across frames
        tracked_objects = tracker.update(detections, frame)

        # Step 3: Draw boxes with labels and IDs
        for obj in tracked_objects:
            x1, y1, x2, y2 = obj["box"]
            draw_box(frame, x1, y1, x2, y2, obj["class_name"], obj["track_id"])

        # Step 4: Calculate and display FPS
        current_time = time.time()
        fps = 1 / (current_time - prev_time) if prev_time else 0
        prev_time = current_time
        draw_fps(frame, fps)

        # Step 5: Show the output frame
        cv2.imshow("Object Detection and Tracking", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
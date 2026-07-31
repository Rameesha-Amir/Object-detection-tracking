from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_path="models/yolov8n.pt", confidence_threshold=0.5):
        """
        Loads the YOLO model from the given path.
        """
        self.model = YOLO(model_path)
        self.confidence_threshold = confidence_threshold

    def detect(self, frame):
        """
        Runs detection on a single frame and returns a list of detections.
        Each detection is a dict: {box: [x1,y1,x2,y2], confidence, class_name}
        """
        results = self.model(frame, verbose=False)[0]
        detections = []

        for box in results.boxes:
            confidence = float(box.conf[0])

            if confidence < self.confidence_threshold:
                continue

            x1, y1, x2, y2 = box.xyxy[0].tolist()
            class_id = int(box.cls[0])
            class_name = self.model.names[class_id]

            detections.append({
                "box": [x1, y1, x2, y2],
                "confidence": confidence,
                "class_name": class_name
            })

        return detections
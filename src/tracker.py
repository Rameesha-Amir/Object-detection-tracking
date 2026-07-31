from deep_sort_realtime.deepsort_tracker import DeepSort

class ObjectTracker:
    def __init__(self, max_age=30):
        """
        Initializes the Deep SORT tracker.
        max_age = how many frames to keep a lost object before removing its ID.
        """
        self.tracker = DeepSort(max_age=max_age)

    def update(self, detections, frame):
        """
        Updates tracker with current frame's detections.
        Returns a list of tracked objects with IDs.
        """
        formatted_detections = []

        for det in detections:
            x1, y1, x2, y2 = det["box"]
            w, h = x2 - x1, y2 - y1
            # Deep SORT expects format: ([x1, y1, w, h], confidence, class_name)
            formatted_detections.append(([x1, y1, w, h], det["confidence"], det["class_name"]))

        tracks = self.tracker.update_tracks(formatted_detections, frame=frame)

        tracked_objects = []
        for track in tracks:
            if not track.is_confirmed():
                continue

            track_id = track.track_id
            x1, y1, x2, y2 = track.to_ltrb()
            class_name = track.get_det_class()

            tracked_objects.append({
                "box": [x1, y1, x2, y2],
                "track_id": track_id,
                "class_name": class_name
            })

        return tracked_objects
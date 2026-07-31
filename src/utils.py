import cv2

def draw_box(frame, x1, y1, x2, y2, label, track_id=None, color=(0, 255, 0)):
    """
    Draws a bounding box with a label and optional tracking ID on the frame.
    """
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    # Draw rectangle around the object
    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

    # Prepare text to display
    if track_id is not None:
        text = f"ID {track_id}: {label}"
    else:
        text = label

    # Draw background rectangle for text (for readability)
    (text_width, text_height), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
    cv2.rectangle(frame, (x1, y1 - text_height - 10), (x1 + text_width, y1), color, -1)

    # Put the text
    cv2.putText(frame, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (255, 255, 255), 2)

    return frame


def draw_fps(frame, fps):
    """
    Displays FPS (frames per second) on the top-left corner of the frame.
    """
    cv2.putText(frame, f"FPS: {int(fps)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
    return frame
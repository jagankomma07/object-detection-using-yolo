import os
import cv2
from ultralytics import YOLO

model = YOLO("./models/yolo11n.pt")

def detect_objects_in_video(video_path):
    """
    Detects objects in a video using YOLOv11 and saves the output video with bounding boxes.

    Args:
        video_path (str): Path to the input video file.

    Returns:
        str: Path to the output video file with detections.
    """
    # Ensure the input video file exists
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Input video file not found: {video_path}")

    os.makedirs("./output", exist_ok=True)

    video_file_name = os.path.splitext(os.path.basename(video_path))[0]
    output_path = os.path.join("./output", f"output_{video_file_name}.mp4")  

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Could not open video file: {video_path}")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) if cap.get(cv2.CAP_PROP_FRAME_WIDTH) > 0 else 640 
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) if cap.get(cv2.CAP_PROP_FRAME_HEIGHT) > 0 else 480
    fps = cap.get(cv2.CAP_PROP_FPS) if cap.get(cv2.CAP_PROP_FPS) > 0 else 30  

    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame)

            for result in results:
                if result.boxes:
                    for box in result.boxes:
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        cls = int(box.cls[0])
                        confidence = float(box.conf[0])
                        label = f"{model.names[cls]} {confidence:.2f}"

                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            out.write(frame)

    except Exception as e:
        print(f"An error occurred during video processing: {e}")
    finally:
        cap.release()
        out.release()

    return output_path
import cv2
import torch
from ultralytics import YOLO
import os

# Load YOLO model
model = YOLO("./models/yolo11n.pt")

def detect_objects_in_image(image_path):
    image = cv2.imread(image_path)
    results = model(image)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0])

            label = f"{model.names[cls]}"  # Updated label to include class name
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    image_file_name = os.path.basename(image_path).split('.')[0]
    output_path = f"./output/output-{image_file_name}.jpg"
    cv2.imwrite(output_path, image)
    return output_path

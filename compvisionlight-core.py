from ultralytics import YOLO
import cv2

# Model will download on start, if not, download with wget https://huggingface.co/ultralytics/yolov8/resolve/main/yolov8n.pt
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, imgsz=320)

    annotated_frame = results[0].plot()

    cv2.imshow("CompVision-Light", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

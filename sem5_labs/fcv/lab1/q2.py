import cv2 as cv
import cv2
video_path = '/home/Student/Desktop/220962049_aiml_a1/venv/lab1/q2-ezgif.com-gif-to-mp4-converter.mp4'
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Frame', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
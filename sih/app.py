from flask import Flask, render_template, Response
import cv2
import tempfile
import os
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
prev = None
app = Flask(__name__)

# Replace with the path to your video file
video_path = '/Users/janavbhasin/Desktop/crawling.mp4'
cap = cv2.VideoCapture(video_path)
def is_crawling(keypoints, prev):
    if prev is None:
        return False
    right_hip_x = keypoints[mp_pose.PoseLandmark.RIGHT_HIP.value].x
    prev_right_hip_x = prev[mp_pose.PoseLandmark.RIGHT_HIP.value].x
    
    right_shoulder_x = keypoints[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x
    prev_right_shoulder_x = prev[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x
    
    left_shoulder_x = keypoints[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x
    prev_left_shoulder_x = prev[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x
    
    left_hip_x = keypoints[mp_pose.PoseLandmark.LEFT_HIP.value].x
    prev_left_hip_x = prev[mp_pose.PoseLandmark.LEFT_HIP.value].x
    
    right_hip_y = keypoints[mp_pose.PoseLandmark.RIGHT_HIP.value].y
    right_shoulder_y = keypoints[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y

    left_hip_y = keypoints[mp_pose.PoseLandmark.LEFT_HIP.value].y
    left_shoulder_y = keypoints[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
    
    if(abs(right_shoulder_x - prev_right_shoulder_x) + abs(left_shoulder_x - prev_left_shoulder_x)+ abs(left_hip_x- prev_left_hip_x)+ abs(right_hip_x- prev_right_hip_x)>0.015):
         if (round(right_hip_y, 1) == round(right_shoulder_y, 1) or round(left_hip_y, 1) == round(left_shoulder_y, 1)):
            return 0
    if (round(right_hip_y, 1) == round(right_shoulder_y, 1) or round(left_hip_y, 1) == round(left_shoulder_y, 1)):
            return 1
    return -1

def is_running(keypoints, prev, fps, c):
    if prev is None:
        return False
    hip_y = keypoints[mp_pose.PoseLandmark.LEFT_HIP.value].y
    knee_y = keypoints[mp_pose.PoseLandmark.LEFT_KNEE.value].y
    prev_knee_y=prev[mp_pose.PoseLandmark.LEFT_KNEE.value].y
    knee_y_r=keypoints[mp_pose.PoseLandmark.RIGHT_KNEE.value].y
    prev_knee_x=prev[mp_pose.PoseLandmark.LEFT_KNEE.value].x
    knee_x=keypoints[mp_pose.PoseLandmark.LEFT_KNEE.value].x
    print(c)
    print(knee_x)
    knee_y_r=round(knee_y_r,1)
    knee_y=round(knee_y,1)
    speed=abs(prev_knee_x-knee_x)
    speed=speed/fps
    print(speed)
    if knee_y_r!=knee_y:
        return True
    if speed<1:
        if speed>0.003:
            return True
    return False

def process_frame(frame, count, c):
    global prev  # Declare prev as a global variable to modify and use it globally
    fps = 30.0  # Set a default FPS value, you can adjust this as needed
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_frame)
    c += 1
    if results.pose_landmarks:
        keypoints = results.pose_landmarks.landmark
        if is_crawling(keypoints, prev) == 0:
            status = "Crawling"
            count = count + 15
            cv2.putText(frame, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            print(status)
        elif is_crawling(keypoints, prev) == 1:
            status = "Lying"
            if (count > 0):
                status = "Crawling"
                count = count - 1
            cv2.putText(frame, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            print(status)
        elif is_running(keypoints, prev, fps, c):
            status = "Running"
            cv2.putText(frame, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            print(status)
        prev = keypoints  # Update the global prev variable
        for landmark in keypoints:
            x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
            cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
    return frame, count, c

def generate_frames():
    count = 0  # Initialize the count variable
    c = 0      # Initialize the c variable
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame, count, c = process_frame(frame, count, c)  # Pass all parameters to process_frame
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            break
        frame_data = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_data + b'\r\n')


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/garuda')
def garuda():
    return render_template('garuda.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)

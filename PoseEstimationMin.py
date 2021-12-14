import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture('Video/Vd_1.mp4')
pTime = 0

while True:

    cv2.namedWindow("Video Processing", cv2.WINDOW_NORMAL)#Create window with freedom of dimension
    success, vid = cap.read()
    vidRGB = cv2.cvtColor(vid, cv2.COLOR_BGR2RGB)
    results = pose.process(vidRGB)
    #print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(vid, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = vid.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(vid, (cx, cy), 10, (255, 0,0), cv2.FILLED)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(vid, str(int(fps)), (70,550), cv2.FONT_HERSHEY_PLAIN, 15, (255, 0, 0), 10)
    cv2.imshow("Video Processing", vid)
    cv2.waitKey(1)
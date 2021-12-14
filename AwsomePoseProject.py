import cv2
import time
import PoseModule as pm

cap = cv2.VideoCapture('Video/Vd_1.mp4')
pTime = 0
detector = pm.poseDetector()
while True:
    cv2.namedWindow("Video Processing", cv2.WINDOW_NORMAL)  # Create window with freedom of dimension
    success, vid = cap.read()
    vid = detector.findPose(vid)
    lmList = detector.getPosition(vid, draw=False)
    print(lmList[14])
    cv2.circle(vid, (lmList[14][1], lmList[14][2]), 10, (0, 0, 255), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(vid, str(int(fps)), (70, 550), cv2.FONT_HERSHEY_PLAIN, 15, (255, 0, 0), 10)
    cv2.imshow("Video Processing", vid)
    cv2.waitKey(1)

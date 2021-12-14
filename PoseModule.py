import cv2
import mediapipe as mp
import time



class poseDetector():
    def __init__(self, mode=False, model_complexity = 1, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5, enable_segmentation=False, smooth_segmentation=True):
        self.mode = mode
        self.model_complexity = model_complexity
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.enable_segmentation = enable_segmentation
        self.smooth_segmentation = smooth_segmentation
        self.pose = self.mpPose.Pose()

    def findPose(self, vid, draw=True):
        vidRGB = cv2.cvtColor(vid, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(vidRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(vid,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)

            return vid

    def getPosition(self, vid, draw=True):
            lmList = []
            if self.results.pose_landmarks:
                for id, lm in enumerate(self.results.pose_landmarks.landmark):
                    h, w, c = vid.shape
                    print(id, lm)
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                    if draw:
                        cv2.circle(vid, (cx, cy), 10, (255, 0,0), cv2.FILLED)
            return lmList

def main():
    cap = cv2.VideoCapture('Video/Vd_1.mp4')
    pTime = 0
    detector = poseDetector()
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



if __name__ == "__main__":
    main()
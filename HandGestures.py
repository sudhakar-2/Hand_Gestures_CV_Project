import cv2
import mediapipe as mp
import pyautogui

print("checking wheather the file is running or not asking this is developer B")

print(mp.__version__)

x1 = y1 = x2 = y2 =0
webcam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
my_hands = mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils

if webcam.isOpened():
    print("cam is opened")
else:
    print("cam is closed")

while True:
    ret, frame = webcam.read()
    
    frame_width,frame_height,_ = frame.shape

    if not ret:
        break
    
    frame=cv2.resize(frame,(500,500))
    rgb_image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=my_hands.process(rgb_image)
    hands=output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks=hand.landmark
            for id,landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)
                if id==8:
                    cv2.circle(frame,(x,y),radius=8,color=(0,255,255),thickness=3)
                    x1=x
                    y1=y
                if id==4:
                    cv2.circle(frame,(x,y),radius=8,color=(255,255,0),thickness=3)
                    x2=x
                    y2=y
                dist=((x2-x1)**2 + (y2-y1)**2)**(0.5)//4
                if dist >50:
                    pyautogui.press("volumeup")
                else:
                    pyautogui.press("volumedown")
                cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),3)
    cv2.imshow("webcam",frame)
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
webcam.release()
cv2.destroyAllWindows()
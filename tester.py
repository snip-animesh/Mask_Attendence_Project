import cv2 as cv
import warnings
from cvzone.FaceDetectionModule import FaceDetector
import arduinoController as ctn
import detect_mask

warnings.filterwarnings('ignore')

name,roll=" "," "
faceDetector = FaceDetector()

cap = cv.VideoCapture(0)
door_state=0
RGB=[0,0,0]
while True:
    success, img = cap.read()
    # if there is face or no face
    img, bbox = faceDetector.findFaces(img, draw=False)
    if not bbox:
        RGB = [0, 0, 1]
    elif bbox:
        RGB, door_state, name, roll = detect_mask.main(img)
    k = cv.waitKey(1)
    if k == ord('q'):
        break
    ctn.rgb(RGB)
    ctn.door(door_state)
    ctn.lcd(name.upper(),roll)
    # print(RGB)
    print(name,roll)
ctn.rgb([0,0,0])
ctn.door(0)
ctn.lcd(" "," ")
cap.release()
cv.destroyAllWindows()
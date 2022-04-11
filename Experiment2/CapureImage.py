import numpy as np
import cv2
   
cap = cv2.VideoCapture(0)

def settings(): 
    cap.set(3, 670.0)
    print("framewidth:" + str(cap.get(3)))
    cap.set(4, 420.0)
    print("frameheight:" + str(cap.get(4)))
    print("--------------------------------")
    cap.set(10, 140)
    print("brightness:" + str(cap.get(10)))
    cap.set(11, 36)
    print("contrast:" + str(cap.get(11)))
    cap.set(12, 0)
    print("saturation:" + str(cap.get(12)))
    print("--------------------------------")
    cap.set(14, 10)
    print("gain:" + str(cap.get(14)))
    cap.set(15, -2)
    print("exposure:" + str(cap.get(15)))
    print("--------------------------------")
    cap.set(17, 6000)
    print("whitebalance:" + str(cap.get(17)))
    
def shoot():
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("pic.png", frame)
            break;

def shoot10():
    for x in range(1, 20):
        ret, frame = cap.read()
        cv2.imwrite("pic" + str(x) + ".png", frame)
           
    cap.release()
    cv2.destroyAllWindows()

settings()
shoot()
shoot10()

cap.release()
cv2.destroyAllWindows()
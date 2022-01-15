import cv2
import random

def take_snapshot():
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    number=random.randint(1,100)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any storage device
        imageName="image"+str(number)+".jpg"
        cv2.imwrite(imageName,frame)
        result = False
    
    # releases the camera
    videoCaptureObject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()

take_snapshot()

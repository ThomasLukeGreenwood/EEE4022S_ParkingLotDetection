"""
This file connects to the ESP32 cam. It also allows control such as
* Changing resolution (r)
* Saving data that comes in as jpgs (s)
* Running predictions with YOLO (p) 
* Stopping streaming (esc)
Note for this to work properly, both the computer and esp32
must be connected to a mutal wifi source
current I have set that to be my iPhone hotspot
"""

import cv2
import numpy as np
from ultralytics import YOLO

import requests

'''
INFO SECTION
- if you want to monitor raw parameters of ESP32CAM, open the browser and go to http://192.168.x.x/status
- command can be sent through an HTTP get composed in the following way http://192.168.x.x/control?var=VARIABLE_NAME&val=VALUE (check varname and value in status)
'''

# ESP32 URL
URL = "http://192.168.4.1"
AWB = True

cap = cv2.VideoCapture(URL + ":81/stream") #/81stream

#importing the YOLO model
model = YOLO("largeYOLO.pt")  # pretrained YOLOv8s model
model.to("cuda")

# This allows us to set the resolution easily - index 10 is the best for me
def set_resolution(url: str, index: int=1, verbose: bool=False):
    try:
        if verbose:
            resolutions = "10: UXGA(1600x1200)\n9: SXGA(1280x1024)\n8: XGA(1024x768)\n7: SVGA(800x600)\n6: VGA(640x480)\n5: CIF(400x296)\n4: QVGA(320x240)\n3: HQVGA(240x176)\n0: QQVGA(160x120)"
            print("available resolutions\n{}".format(resolutions))

        if index in [10, 9, 8, 7, 6, 5, 4, 3, 0]:
            requests.get(url + "/control?var=framesize&val={}".format(index))
        else:
            print("Wrong index")
    except:
        print("SET_RESOLUTION: something went wrong")
# This allows quality, 10 is the best option for me
def set_quality(url: str, value: int=1, verbose: bool=False):
    try:
        if value >= 10 and value <=63:
            requests.get(url + "/control?var=quality&val={}".format(value))
    except:
        print("SET_QUALITY: something went wrong")

# Honestly don't know what this does but it doesn't work anyway
def set_awb(url: str, awb: int=1):
    try:
        awb = not awb
        requests.get(url + "/control?var=awb&val={}".format(1 if awb else 0))
    except:
        print("SET_QUALITY: something went wrong")
    return awb
 #activate saving data mode
def startSaving(dImg,dSaveData,dcnt):
    if(dSaveData):
        savePeriod = 10
        if(dcnt % savePeriod==0): 
            fileName = "image_"+str(int(dcnt/savePeriod))+".jpg" 
            cv2.imwrite(fileName, dImg)
        dcnt = dcnt + 1
    return dcnt # returning the number of images


if __name__ == '__main__':
    set_resolution(URL, index=8)
    saveData = False
    startPredicting = False
    cnt = 0
    while True:
        if cap.isOpened():
            ret, frame = cap.read()
            
            if(not(startPredicting)):
                cv2.imshow("frame", frame)
            else:
                results = model.predict(source = frame, show = True, show_labels = True, conf = 0.2, save = True)
            #Saving option
            cnt = startSaving(frame,saveData,cnt)
            # Modes to set quality, resolution, to start Saving data and quit
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.equalizeHist(gray)

            key = cv2.waitKey(1)

            if key == ord('r'):
                idx = int(input("Select resolution index: "))
                set_resolution(URL, index=idx, verbose=True)

            elif key == ord('q'):
                val = int(input("Set quality (10 - 63): "))
                set_quality(URL, value=val)

            elif key == ord('a'):
                AWB = set_awb(URL, AWB)
            
            elif key == ord('s'): #s
                print("Saving Images")  
                saveData = True
           
            elif key == ord('p'): #start predicting
                print("Starting predictions")  
                startPredicting = True

            elif key == 27: # press exit key to leave the window
                break

    cv2.destroyAllWindows()
    cap.release()
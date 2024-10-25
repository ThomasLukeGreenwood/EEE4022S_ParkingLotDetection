# This is just validating the results from FOMO
# Geting input from C/C++ file and draws the bounding boxes using cv2

import cv2
import numpy as np
from PIL import Image # for cropping image
# bounding boxes in form 
# From docs to draw boxes on frame, 
# frame = cv2.rectangle(frame, [start1, start2], [end 1, end2])
#originalImage
#image = cv2.imread("RawDataToCSV/parkinglotdetection-export/testing/photo_7_jpg.rf.04d0f92cc172fd91bba5796a680b984d.jpg.58mbm5kf.ingestion-8bdc99b6c-wk4p9.jpg")
filename = "RawDataToCSV/parkinglotdetection-export/testing/photo_51_jpg.rf.589e4411e1f741a9a592cee0676de898.jpg.58mbluvp.ingestion-8bdc99b6c-7m6vn.jpg"

image = cv2.imread(filename)

# Changing the image size as defined by FOMO docs
widthCrop = 80 #(640-480)/2 
image =image[widthCrop:(640-widthCrop),0:480] 
image = cv2.resize(image, (128,128))


#static bounding box declaration Can probs somewhat easily change this to read in from command line

#stringOfResults =   "occupied (0.980469) [ x: 0, y: 8, width: 8, height: 24 ] \nempty (0.937500) [ x: 56, y: 16, width: 72, height: 16 ] \noccupied (0.980469) [ x: 0, y: 40, width: 8, height: 16 ] \nempty (0.898438) [ x: 8, y: 40, width: 8, height: 8 ] \nempty (0.851562) [ x: 56, y: 48, width: 8, height: 8 ] \nempty (0.972656) [ x: 0, y: 56, width: 32, height: 16 ] \nempty (0.917969) [ x: 104, y: 64, width: 16, height: 8 ] \nempty (0.941406) [ x: 40, y: 80, width: 16, height: 16 ] \nempty (0.890625) [ x: 104, y: 80, width: 24, height: 8 ] \nempty (0.937500) [ x: 64, y: 88, width: 32, height: 16 ]"
stringOfResults = "empty (0.964844) [ x: 96, y: 24, width: 8, height: 24 ] \nempty (0.980469) [ x: 112, y: 24, width: 16, height: 16 ] \nempty (0.937500) [ x: 112, y: 56, width: 8, height: 8 ] \noccupied (0.917969) [ x: 120, y: 64, width: 8, height: 8 ]"
#print(stringOfResults)   
# Statically assigning the rectangles 

#This Section needs serious cleaning
nResults = len(stringOfResults.split("\n"))# correct or number of results
Lines = stringOfResults.split("\n")

# Drawing in the rectangles based off the results   
for i in range(nResults):
    color = (255,0,0) #switch back to red
    SepLines = Lines[i].split(" ")
    if SepLines[0] == "empty": # switch to green if the color is empty
        color = (0,255,0)
    
    #breaking down the values 
    x_1 = int(SepLines[4].strip(","))
    y_1 = int(SepLines[6].strip(","))
    x_2 = x_1+int(SepLines[8].strip(","))
    y_2 = y_1 +int(SepLines[10].strip(","))     
    print(x_1,y_1,x_2, y_2)
    image = cv2.rectangle(image, (x_1, y_1), (x_2,y_2), color,thickness = 2)
image = cv2.resize(image, (480,480))
while True: 
    cv2.imshow("FrameName",image)
    if cv2.waitKey(1) & 0xFF == ord("q"):
            break
"""
This file is to test a single image

"""

from ultralytics import YOLO
import numpy
import cv2

#resizing the image
# Other image optionst

#1-3 are the different parking lots from the test set 4 is from an untrained parking lot


#img = "Datasets/MergedParkingDataset.v1i.yolov8/test/images/photo_6_jpg.rf.38deb508061aee7638aa91b503c9f1b1.jpg" # Test data
#img = "Datasets/MergedParkingDataset.v1i.yolov8/test/images/4k-time-lapse-car-parking-lot-stock-video-download-video-clip-now-istock_TyROSAGZ_mp4-18_jpg.rf.29711c038857f37764e52a4f800a52eb.jpg"
#img = "UntrainedData/SP0.jpeg"
#img = "Datasets/MergedParkingDataset.v1i.yolov8/test/images/photo_42_jpg.rf.e27e6bc9bab5f5d312a155981c4482e8.jpg"

#img = "PythonCodeForYOLO/TestDataValidation/TestData/test/images/photo_1_jpg.rf.0d71ed04b80b30b50401e15be092e640.jpg" $# this one is very badW
#img = "C:/Users/tlgwo/Documents/UCT/4th Year/EEE4022/ESP32Connection/image_32.jpg"
img = "UntrainedData/FromWeb.jpg"

#img = "D:/photo_46.jpg"
#img = "C:/Users/tlgwo/Documents/UCT/4th Year/EEE4022/CollectedData/HandpickeTestData/photo_49.jpg"
#img = "C:/Users/tlgwo/Documents/UCT/4th Year/EEE4022/ESP32Connection/image_5.jpg"
#img = "D:/photo_2.jpg"
imgSx,imgSy,imgRBG = (cv2.imread(img)).shape
#folder ="C:/Users/tlgwo/Documents/UCT/4th Year/EEE4022/CollectedData/TestData3" # Test data
#folder = "C:/Users/tlgwo/Documents/UCT/4th Year/EEE4022/CollectedData/TestData2" #  Other test data
#folder ='C:/Users/tlgwo/Documents/UCT/4th Year/EEE4022_Final/PythonCodeForYOLO/TestDataValidation/TestData/test/images'
#folder = "C:/Users/tlgwo/Documents/UCT/4th Year/EEE4022/CollectedData/LabeledDataSet/ParkingLotDataset.v1i.yolov8/valid/images" # validation data
print("Width = ", imgSx)    
print("Height = ", imgSy)

imgRs =  cv2.resize(cv2.imread(img), (640,640))
# Load a model
modelName = "runs/detect/train_m/weights/best.pt"
#modelName = "C:/Users/tlgwo/Documents/UCT/retrainingYOLO/Models/yolo_n.pt"
model = YOLO(modelName)  # pretrained YOLOv8n model
model.to("cuda")

results = model.predict(source = imgRs, show = True, show_labels = True, conf = 0.2, save = False) # can add Visualise = true for useful data ,imgsz = (imgSx,imgSy),
print("\n",results)
while (True):
    if cv2.waitKey(25)& 0xFF == ord('q'): # Break out of loop when q is pressed
        break   
cv2.destroyAllWindows() # Stop displaying the frame 

# Note need to find a way how to do some low pass filtering specific to each box location
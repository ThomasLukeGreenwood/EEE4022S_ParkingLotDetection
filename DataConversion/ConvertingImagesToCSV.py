# This fully works -> It converts images to RBG888 format
# This format is correct for FOMO to read in
# I have tested it and it returns the expected results

from PIL import Image # for cropping image
import numpy as np # for creating numpy arrays
import binascii # for converting to hex
import cv2 
import numpy as np
# Reading in the file
#originalFileName
#filename = 'RawDataToCSV/parkinglotdetection-export/testing/photo_7_jpg.rf.04d0f92cc172fd91bba5796a680b984d.jpg.58mbm5kf.ingestion-8bdc99b6c-wk4p9.jpg'
#filename = "RawDataToCSV/parkinglotdetection-export/training/photo_0_jpg.rf.d3a8019c86af420252cbdbbb60146e03.jpg.58mbm1u0.ingestion-8bdc99b6c-2j7nr.jpg"
# resizing the image to 128x128
filename = "RawDataToCSV/parkinglotdetection-export/testing/photo_51_jpg.rf.589e4411e1f741a9a592cee0676de898.jpg.58mbluvp.ingestion-8bdc99b6c-7m6vn.jpg"
image = cv2.imread(filename)
#image = cv2.resize(image,(640, 480)) # for changing the aspect ratio

#print("Display image in hex /n")


# This is taking the numpy file from edge impulse and converting it to CSV

def convert_to_rgb888(image_path):
    # Open the image file
    img = Image.open(image_path) 
    # Convert the image to RGB mode
    # need to crop the longest 640 part into a square 480
    widthCrop = (640-480)/2 
    img = img.crop((widthCrop,0,(640-widthCrop),480))
    img.resize((128,128))
   # img = img.convert('RGB')
    #img.show()
    # Get the image data as a numpy array
    img_data = np.array(img)
    
    # Ensure the data is in the correct format (RGB888)
    img_data = img_data.astype(np.uint8)
    data = ""
    cnt = 0
    for y in range(128):
        for x in range(128):
            cnt = cnt+1
            if data == "": 
                R = str(hex(img_data[x][y][0]))
                G = str(hex(img_data[x][y][1]))
                G = G.replace("0x","") # get rid of the 0x in the middle
                B = str(hex(img_data[x][y][2])) 
                B = B.replace("0x","")
                data = R+G+B 
            else: 
                R = str(hex(img_data[x][y][0]))
                G = str(hex(img_data[x][y][1]))
                G = G.replace("0x","") # get rid of the 0x in the middle
                B = str(hex(img_data[x][y][2])) 
                B = B.replace("0x","")
                data = data +", "+  R+G+B
    
    #data = data.replace("',", ",")
    return data
    # Save the image data to a new file
    #print(binascii.hexlify(img_data))
  
# Example usage
#convert_to_rgb888(filename)


def FromNumpyFile(filename):
    data = np.load("RawDataToCSV/TestingData.npy")
    print(binascii.hexlify(data[0])) # This is image 1
    return data[0]
    
#dataOut = FromNumpyFile(filename)
dataOut =convert_to_rgb888(filename)
file2write = open("Testing.txt",'w') 
file2write.write(dataOut)
file2write.close()
print("Success")
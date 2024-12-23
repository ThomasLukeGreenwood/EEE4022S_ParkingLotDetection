# Parking Lot detection: The development of a vision based parking lot detector
<div align="center">

## Introduction  
This project compares various models and hardware to deploy the optimal parking lot detector on UCT's campus.

It compares FOMO and YOLOv8 running as edge and cloud based devices on ESP32-CAM, Raspberry Pi 4b and Laptop with 3050 GPU.

The link the the roboflow dataset is [here](https://app.roboflow.com/parkinglotdataset/mergedparkingdataset/16)

The link to the google drive containing the models is [here](https://drive.google.com/drive/folders/19S4D6c7Q1m6xjuM8bxjOBioV1oVX5XnU?usp=drive_link)
<div>



![Structure](https://github.com/user-attachments/assets/bbf294a9-e7f5-46d2-a8d2-d93d0a577348)
<div align="center">The Stucture of Cloud vs Edge Processing<div>


![AccuracyResults](https://github.com/user-attachments/assets/9faee921-4a49-4229-8ccd-dbde98d9c393)
<div align="center">The Accuracy on Different Models<div>


![Inference Time RPI](https://github.com/user-attachments/assets/e79fa0ae-4d54-4c87-892f-431203370a57)
<div align="center">The Inference Time of the Raspberry Pi<div>

![l](https://github.com/user-attachments/assets/c43a4e2d-06ab-4d24-8340-fb23fa2944c9)

<div align="center">Results From Test Set<div>

## Conclusion

The raspberry Pi 4 running YOLOv8n results in the best preformance in terms of balance of accuracy, power consumption, bandwidth use, and sever load.
With further development to the dataset and post processing on the server side, this device could be used in a network of sensors to find available parking accross the whole of UCT.



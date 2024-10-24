from ultralytics import YOLO
if __name__ == '__main__':
    # load a pretrained model (recommended for training)
    model = YOLO("yolov8m.pt")  
     # move the model to the GPU
    model.to("cuda")
    #For the other dataset
    dataLocation = #Insert Location of dataset
    # Location of the YOLOv8 dataset's yaml file
    results = model.train(
        data=dataLocation,
        epochs=50, 
        imgsz=640)
    print("Training Complete!!!")
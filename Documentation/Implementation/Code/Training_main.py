from ultralytics import YOLO
if __name__ == '__main__':
    # load a pretrained model (recommended for training)
    model = YOLO("yolov8m.pt")  
     # move the model to the GPU
    model.to("cuda")
    # Location of the YOLOv8 dataset's yaml file
    dataLocation =""#insert path here 
    #train model for 50 epochs
    #resize images to 640x640
    results = model.train(
        data=dataLocation,
        epochs=50, 
        imgsz=640)
    print("Training Complete!!!")
    
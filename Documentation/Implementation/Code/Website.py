def updatePrediction():
    #Load model
    model = YOLO("YOLOv8n.pt")
    #Capture the image
    cap = cv2.VideoCapture(0) 
    result, frame = cap.read()
    #Predict
    results = model(frame,
    conf = 0.07, 
    verbose = False)
    annotated_frame = results[0].plot()
    # Save The image
    cv2.imwrite(
        "Flask_app/static/images/predictions.jpg",
        annotated_frame)
    cap.release()
    #Render the webpage
    return render_template('prediction.html')
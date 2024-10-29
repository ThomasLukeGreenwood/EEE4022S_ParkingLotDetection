from flask import Flask, render_template,jsonify
from ultralytics import YOLO
import cv2
import requests


number = 0
app = Flask(__name__)
#director of the home route
def update_number():
    global number
    number = makePredictions()
    return jsonify(number=number)
@app.route('/')
def index():
    number = makePredictions()
    return render_template('index.html',number = number)
@app.route('/update_number')


#director of the predictions route
@app.route('/dynamic')
def dynamic():
    #Load model
    makePredictions()
    return render_template('dynamic.html')

def makePredictions():
    model = YOLO("best.pt")
    #Capture the image
    #cap = cv2.VideoCapture(0) # For edge based processors use own webcam
    URL = "http://192.168.4.1" # For cloud based connect to url and get the data from here
    cap = cv2.VideoCapture(URL + ":81/stream") #/81stream
    result, frame = cap.read()
    results = model(frame,
    conf = 0.15,
    iou = 0.8, 
    verbose = False,
    show_labels = False)
    annotated_frame = results[0].plot()
    cv2.imwrite(
        "Flask_app/static/images/dynamic_image.jpg",
        annotated_frame)
    cap.release()
    number = results[0].boxes.cls.tolist().count("empty")
    names = model.names
    empty_id = list(names)[list(names.values()).index('empty')]
    number = results[0].boxes.cls.tolist().count(empty_id)
    return number
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
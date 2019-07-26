#!/usr/bin/env python
from flask import Flask, render_template, Response
import cv2
import sys
import numpy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def get_frame():
    camera_port=0
    global camera
    camera=cv2.VideoCapture(camera_port) #this makes a web cam object
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter('./static/video.avi',fourcc, 20.0, (640,480))
    while True:
        retval, im = camera.read()
        init_record(im,out)
        imgencode=cv2.imencode('.jpg',im)[1]
        stringData=imgencode.tostring()    
        yield (b'--frame\r\n'
            b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')
    out.release()
    del(camera)
def hola():
    return 'hola mundo'
def init_record(img,out):
    
    out.write(img)        
    
    

@app.route('/calc')
def calc():
     return Response(get_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')



    

if __name__ == '__main__':
    app.run(host='localhost', debug=True, threaded=True)

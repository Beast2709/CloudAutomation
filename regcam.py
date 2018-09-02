#!/usr/bin/python36



from flask import Flask, render_template, Response
from camera import VideoCamera
import cv2
import numpy as np
import subprocess as sp
import webbrowser
from os import listdir
from os.path import isfile, join


app = Flask(__name__,template_folder='/var/www/html')

@app.route('/')
def index():
    return render_template('facelogin.html')

face_cascade=cv2.CascadeClassifier('/var/www/cgi-bin/haarcascade_frontalface_default.xml')
def faceextrator(img):
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=face_cascade.detectMultiScale(gray,1.3,5)
	if faces is ():
		return None
	for (x,y,w,h) in faces:
		cropped=img[y:y+h,x:x+w]
	return cropped


face_classifier = cv2.CascadeClassifier('/var/www/cgi-bin/haarcascade_frontalface_default.xml')
def face_detector(img, size=0.5):
	# Convert image to grayscale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_classifier.detectMultiScale(gray, 1.3, 5)
	if faces is ():
		return img,[]

	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
		roi = img[y:y + h, x:x + w]
		roi = cv2.resize(roi, (200, 200))
	return img, roi


def gen(camera):
	count =0 
	face_cascade=cv2.CascadeClassifier('/var/www/cgi-bin/haarcascade_frontalface_default.xml')
	while True:
		frame=camera.get_frame1()
		if faceextrator(frame) is not None:
			count+=1
			face=cv2.resize(faceextrator(frame),(200,200))
			face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
			filepath='/var/www/faces/user/nameimg'+str(count)+'.jpg'
			cv2.imwrite(filepath,face)
			cv2.putText(face,str(count),(5,5),cv2.FONT_HERSHEY_COMPLEX,12,255)
			ret, jpeg = cv2.imencode('.jpg', face)
			jpeg=jpeg.tobytes()
			yield (b'--frame\r\n'
            	   b'Content-Type: image/jpeg\r\n\r\n' + jpeg + b'\r\n\r\n')
		else:
			print('Finding face')
			pass
		if count==100:
			break
	print("Face Scan Complete")


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=1239)


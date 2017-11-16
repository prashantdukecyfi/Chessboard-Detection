import numpy as np
import cv2
import math

land_cascade = cv2.CascadeClassifier('cascade15.xml')

cap = cv2.VideoCapture(-1)

while (True):
	ret,img = cap.read()	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	land = land_cascade.detectMultiScale(gray, 10, 10)

	for (x,y,w,h) in land:
	    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),5)
	    roi_gray = gray[y:y+h, x:x+w]
	    roi_color = img[y:y+h, x:x+w]
	    print ("Platform detected") 	
	    a = int((x+x+w)/2)
	    b = int((y+y+h)/2)
	    cv2.circle(img,(a,b),10,(0,0,255),-1)			    
	    cv2.circle(img,(320,240),10,(0,0,0),-1)
	    distance_on_screen = math.sqrt((a-320)*(a-320)+(b-240)*(b-240))
	    print (distance_on_screen)
	    #To find distance on ground we will use height from the sensor and find the scaling factor and multiply it with distance_on_screen and thus by using unitary method we will find the corresponding distance on ground
	cv2.imshow('img',img)
	if cv2.waitKey(100) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()

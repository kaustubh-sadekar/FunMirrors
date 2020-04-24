import cv2
import numpy as np
import math
from vcam import vcam,meshGen
import sys


cap = cv2.VideoCapture(0)

ret, img = cap.read()

H,W = img.shape[:2]
fps = 30

# Creating the virtual camera object
c1 = vcam(H=H,W=W)

# Creating the surface object
plane = meshGen(H,W)

# Defining the plane by Z = F(X,Y) 
plane.Z += 20*np.exp(-0.5*((plane.X*1.0/plane.W)/0.1)**2)/(0.1*np.sqrt(2*np.pi))

# Extracting the generated 3D plane
pts3d = plane.getPlane()

# Projecting (Capturing) the plane in the virtual camera
pts2d = c1.project(pts3d)

# Deriving mapping functions for mesh based warping.
map_x,map_y = c1.getMaps(pts2d)

ret, img = cap.read()

while 1:
	ret, img = cap.read()
	if ret:
		output = cv2.remap(img,map_x,map_y,interpolation=cv2.INTER_LINEAR,borderMode=0)
		output = cv2.flip(output,1)
		out1 = np.hstack((img,output))
		out1 = cv2.resize(out1,(700,350))
		cv2.imshow("output",out1)
		if cv2.waitKey(1)&0xFF == 27:
			break
	else:
		break
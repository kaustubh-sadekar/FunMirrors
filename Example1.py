import cv2
import numpy as np
import math
from vcam import vcam,meshGen

# Reading the input image. Pass the path of image you would like to use as input image.
img = cv2.imread("chess.png")
H,W = img.shape[:2]

# Creating the virtual camera object
c1 = vcam(H=H,W=W)

# Creating the surface object
plane = meshGen(H,W)

# We generate a mirror where for each 3D point, its Z coordinate is defined as Z = 20*exp^((x/w)^2 / 2*0.1*sqrt(2*pi))

plane.Z += 20*np.exp(-0.5*((plane.X*1.0/plane.W)/0.1)**2)/(0.1*np.sqrt(2*np.pi))
pts3d = plane.getPlane()

pts2d = c1.project(pts3d)
map_x,map_y = c1.getMaps(pts2d)

output = cv2.remap(img,map_x,map_y,interpolation=cv2.INTER_LINEAR)

cv2.imshow("Funny Mirror",output)
cv2.imshow("Input and output",np.hstack((img,output)))
cv2.waitKey(0)

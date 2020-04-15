import cv2
import numpy as np
import math
from vcam import vcam,meshGen
import sys

def nothing(x):
    pass

arg = int(sys.argv[1])

# WINDOW_NAME = "output"
# cv2.namedWindow(WINDOW_NAME,cv2.WINDOW_NORMAL)
# cv2.resizeWindow(WINDOW_NAME,700,700)

cap = cv2.VideoCapture("Video3.mp4")
ret, img = cap.read()

# img = cv2.imread("chess.png")
# img = cv2.imread("pano2.jpg")

# cv2.imshow("output",img)
# cv2.waitKey(0)

H,W = img.shape[:2]
fps = 30
filename = "vids/Video_1a_%d.mp4"%arg

fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter(filename,fourcc,fps,(W,H))

c1 = vcam(H=H,W=W)
grid = meshGen(H,W)

if arg == 1:
	src = grid.getConvexMesh(0.3)
elif arg == 2:
	src = grid.getSimpleMesh()
elif arg == 3:
	src = grid.getMesh3(0.1,20,axis=0)
elif arg == 4:
	src = grid.getMesh4(0.1,10,axis=0)
elif arg == 5:
	src = grid.getMesh5(4,axis=0)
else :
	print("Wrong argument !!")
	exit(-1)

c1.set_tvec(0,0,1)

ret, img = cap.read()
c1.set_tvec(0,0,-c1.focus)

while 1:
	ret, img = cap.read()
	# output_mesh = c1.renderMesh(src)
	output = c1.applyMesh(img,src)
	# M = c1.RT
	output = cv2.flip(output,1)
	# out1 = np.hstack((img,output))
	cv2.imshow("output",output)
	# cv2.imshow("output_mesh",output_mesh)
	out.write(output)
	if cv2.waitKey(1)&0xFF == 27:
		break
import cv2
import numpy as np
import math
from vcam import vcam,meshGen


"""
# Uncomment for a different fun effect
class myMirror(meshGen):

	def __init__(self,H,W):
		super(myMirror, self).__init__(H,W)

	def defineMirror(self,epsilon,sigma,axis=0):

		if not axis:
			self.Z += epsilon*np.exp(-0.5*((self.X*1.0/self.W)/sigma)**2)/(sigma*np.sqrt(2*np.pi))
		elif axis == 1:
			self.Z += epsilon*np.exp(-0.5*((self.Y*1.0/self.H)/sigma)**2)/(sigma*np.sqrt(2*np.pi))
		else:
			print("Wrong axis")
			exit(-1)

	def getMirror(self,epsilon,sigma,axis=0):
		self.defineMirror(epsilon,sigma,axis)

		return self.getPlane()
"""

"""
# Uncomment for fun mirror effect
class myMirror(meshGen):

	def __init__(self,H,W):
		super(myMirror, self).__init__(H,W)

	def defineMirror(self,epsilon,sigma,axis=0):

		if not axis:
			self.Z -= epsilon*np.exp(-0.5*((self.X*1.0/self.W)/sigma)**2)/(sigma*np.sqrt(2*np.pi))
		elif axis == 1:
			self.Z -= epsilon*np.exp(-0.5*((self.Y*1.0/self.H)/sigma)**2)/(sigma*np.sqrt(2*np.pi))
		else:
			print("Wrong axis")
			exit(-1)

	def getMirror(self,epsilon,sigma,axis=0):
		self.defineMirror(epsilon,sigma,axis)

		return self.getPlane()
"""

# """
# Uncomment for sine wave type mirror
class myMirror(meshGen):

	def __init__(self,H,W):
		super(myMirror, self).__init__(H,W)

	def defineMirror(self,epsilon):

		self.Z += epsilon*np.sin((self.X/self.W)*2*np.pi*10)

	def getMirror(self,epsilon):
		self.defineMirror(epsilon)

		return self.getPlane()
# """


cap = cv2.VideoCapture("Video3.mp4")
ret, img = cap.read()

H,W = img.shape[:2]
fps = 30
filename = "sine.mp4"

fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter(filename,fourcc,fps,(W,H))

c1 = vcam(H=H,W=W)
mirror = myMirror(H,W)
src = mirror.getMirror(5)


ret, img = cap.read()

while 1:
	ret, img = cap.read()
	output = c1.applyMesh(img,src)
	output = cv2.flip(output,1)
	out1 = np.hstack((img,output))
	cv2.imshow("output",out1)
	out.write(out1)
	if cv2.waitKey(1)&0xFF == 27:
		break
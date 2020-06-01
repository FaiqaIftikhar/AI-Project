import numpy as np
import cv2
import os
from PIL import Image
import glob
def process():
	counter =0;

	for filename in glob.glob("../src/words/*.png"):
		img=Image.open(filename)
		#img=cv2.cvtColor(image,cv2.IMREAD_GRAYSCALE)
		# increase contrast
		pxmin = np.min(img)
		pxmax = np.max(img)
		temp=img-pxmin
		imgContrast = (img - pxmin) / (pxmax - pxmin) * 255

		# increase line width
		kernel = np.ones((3, 3), np.uint8)
		imgMorph = cv2.erode(imgContrast, kernel, iterations = 1)

		# write
		cv2.imwrite('../data/betterData/%d.png'%(counter), imgMorph)
		counter+=1

	

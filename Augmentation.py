import os
import sys
import cv2

# Open cv course : https://youtu.be/eDIj5LuIL4A?si=Pu5CgRFcmdzATe9s

# Pseudo code
# check given arg + join
# apply filter on image
# add extension name
# save image

def main(path):
	img = cv2.imread(path)
	cv2.imshow('Name', img)
	cv2.waitKey(0) # open cv will show the image until I press a key, ssinon si je mets 5000 ca rest 5 secondes

if __name__ == "__main__":
	if len(sys.argv) != 2:
		exit("Usage: Augmentation.py directory")
	main(sys.argv[1])
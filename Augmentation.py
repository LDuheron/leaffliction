import os
import sys
import cv2

# Open cv course : https://youtu.be/eDIj5LuIL4A?si=Pu5CgRFcmdzATe9s
# transformations methods : https://www.geeksforgeeks.org/image-transformations-using-opencv-in-python/

# Pseudo code
# check given arg + join
# in main :
# - loop over all images and aply ft augmentation
# in augmentation :
# - create a dictionary to store all modification
# - apply all modifs on image
# - add extension name
# - save image with extension 

# modification = { "filter1": "image with filter1", "filter2": "image with filter2"}
#

def augmentation(src, path):
	modification = {}

	modification["_Blur.JPG"] = cv2.GaussianBlur(src, (7, 7), 1)
	modification["_Contrast.JPG"] = cv2.convertScaleAbs(src, alpha=0.5)
	modification["_Flip.JPG"] = cv2.flip(src, 270)
	# modification["_Hue_Adjustment.JPG"] = cv2.cvtColor(src, cv2. COLOR_BGR2HSV)
	modification["_Illumination.JPG"] = cv2.convertScaleAbs(src, beta=50)
	modification["_Rotate.JPG"] = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
	modification["_Zoom.JPG"] = cv2.resize(src, None, fx=5, fy=5, interpolation=cv2.INTER_NEAREST)

	# save image 
	for key, value in modification.items():
		save_path = path.split(".JPG")[0] + key
		cv2.imwrite(save_path, value)


def main(path):
	join_path = os.path.join('.', path)
	try:
		img = cv2.imread(join_path)
		augmentation(img, path)
	except:
		print("Error")



if __name__ == "__main__":
	if len(sys.argv) != 2:
		exit("Usage: Augmentation.py directory")
	main(sys.argv[1])
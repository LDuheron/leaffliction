import os
import sys
import cv2

# Open cv course : https://youtu.be/eDIj5LuIL4A?si=Pu5CgRFcmdzATe9s

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

def augmentation(img, path):
	modification = {}

	modification["_Rotate.JPG"] = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

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
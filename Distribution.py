import os
import sys
import matplotlib.pyplot as plt

# https://java2blog.com/python-count-files-directory/

#  Pseudo code
# - check given arg
# - retrieve data from directory
# - store data
# - seperate function to plot
#-  seperate function to pie
# - show

def render(size, label):
	fig, (ax1, ax2) = plt.subplots(1, 2)
	fig.suptitle("Number of images per directory")

	ax1.pie(size, labels=label, autopct='%1.1f%%')

	ax2.bar(label, size)

	plt.show()


def main(path):
	dir_label = []
	count_file = []

	for root, dirs, files in os.walk(path):
		for dir in dirs:
			dir_label.append(dir)
			dir_path = os.path.join(root, dir)
			count_file.append(len(os.listdir(dir_path)))

	render(count_file, dir_label)


if __name__ == "__main__":
	if len(sys.argv) != 2:
		exit("Usage: ./Distribution.py directory")
	main(sys.argv[1])

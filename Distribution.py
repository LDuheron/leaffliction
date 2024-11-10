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

def pie(size, label):
	fig, ax = plt.subplots()
	ax.pie(size, labels=label, autopct='%1.1f%%')


def main(path):
	dir_label = []
	count_file = []

	for root, dirs, files in os.walk(path):
		for dir in dirs:
			dir_label.append(dir)
			dir_path = os.path.join(root, dir)
			count_file.append(len(os.listdir(dir_path)))

	# print(count_file)
	# print(dir_label)
	pie(count_file, dir_label)
	plt.bar(dir_label, count_file)
	plt.show()



if __name__ == "__main__":
	if len(sys.argv) != 2:
		exit("Usage: ./Distribution.py directory")
	main(sys.argv[1])


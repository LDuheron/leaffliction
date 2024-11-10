import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns

# https://java2blog.com/python-count-files-directory/

#  Pseudo code
# - check given arg
# - retrieve data from directory
# - store data
# - separate fruits
# - sort per fruit and per keys in list !
# - seperate function pie and bar
# - show

def render(fruit_type, label, size):
	fig, (ax1, ax2) = plt.subplots(1, 2)
	fig.suptitle(fruit_type + " class distribution")
	palette = sns.color_palette("Set3")

	ax1.pie(size, labels=label, colors= palette, autopct='%1.1f%%')

	plt.xticks(rotation=60)
	ax2.bar(label, size, color=palette)

	plt.tight_layout()

	plt.show()


def main(path):
	fruit_dictionary = {}

	for root, dirs, files in os.walk(path):
		for dir in sorted(dirs):
			if "_" in dir:
				dir_path = os.path.join(root, dir)
				files_in_dir = [item for item in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, item))]
			
				if files_in_dir:
					fruit = dir.split("_")[0]
					if fruit not in fruit_dictionary:
						fruit_dictionary[fruit] = {"label": [], "size": []}
					fruit_dictionary[fruit]["label"].append(dir)
					fruit_dictionary[fruit]["size"].append(len(files_in_dir))

	for fruit in sorted(fruit_dictionary):
		render(fruit, fruit_dictionary[fruit]["label"], fruit_dictionary[fruit]["size"])

if __name__ == "__main__":
	if len(sys.argv) != 2:
		exit("Usage: ./Distribution.py directory")
	main(sys.argv[1])

import os
import sys
import matplotlib.pyplot as plt 
import numpy as np

#  Pseudo code
# - check given arg
# - retrieve data from directory
# - store data
# - seperate function to plot
#-  seperate function to pie
# - show

def main(data_directory):



if __name__ == "__main__":
	if len(sys.argv) != 2:
		exit("Usage: ./Distribution.py directory")
	main(sys.argv[1])

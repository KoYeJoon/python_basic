#exer06-6_1.py
import os

def search(dirname):
	filenames = os.listdir(dirname)
	for filename in filenames :
		full_filename = os.path.join(dirname,filename)
		print(full_filename)

search("/Users/yejoonko/Study/Python/")

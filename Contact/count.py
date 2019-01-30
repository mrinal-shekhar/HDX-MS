import numpy as np
import glob 
import matplotlib.pyplot as plt
from collections import Counter
import csv
import pickle

###Write a file reader that saves the elements of the file in a single array###

filenames = sorted(glob.glob('contact.dat'))
arr=[]
for n in filenames:
	with open(n, 'r') as f:
    		data=[x.split() for x in f.readlines()]
	print(n)
	arr=arr+data
	


array=[] 	
for i in range(len(arr)):
	for k in range(len(arr[i])):
		array.append(int(arr[i][k]))
       
freq=Counter(array)

results = []
for m in range(479):
	results.append([m, freq[m]])
new_results = []
for line in results:
	if line[1] != 0:
		new_results.append(line)

		
np.savetxt('contacts_all.txt', new_results, delimiter=",")




import csv
import numpy as np 
import pandas as pd 
data = pd.DataFrame(data = pd.read_csv("candidate.csv"))
concepts = np.array(data.iloc[:,:-1])
targets = np.array(data.iloc[:,-1])
spec_h = concepts[0]
gen_h = [['?' for i in range(len(spec_h))] for i in range(len(spec_h))]
for i,j in enumerate(concepts):
	if targets[i].upper() == "YES":
		for k in range(len(spec_h)):
			if spec_h[k] != j[k]:
				spec_h[k] = '?'
				gen_h[k][k] = '?'
	if targets[i].upper() == 'NO':
		for x in range(len(spec_h)):
			if j[x] !=spec_h[x]:
				gen_h[x][x] = spec_h[x]
			else :
				gen_h[x][x] = '?'
indexes = [i for i,val in enumerate(gen_h) if val == [i for i in '?'*6]]
for i in indexes:
	gen_h.remove([i for i in '?'*6])
print('final solution is : ')
print(spec_h)
print(gen_h)



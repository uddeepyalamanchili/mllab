import numpy as nm
import pandas as pd
data = pd.read_csv('Data3.csv')
#print(data.to_string())
l = []
print(type(l))
print(type(data))
pdo = data.head()
print(data.columns[-1])
list1 = list(data[data.columns[-1]])
print(list1)
for i in data[data.columns[-1]]:
	print(i)
print()
s = list(data.loc[data[data.columns[-1]] == 'Y'])
attrib = 'Humidity'
val = 'High'
#print(data.axis)
print(list(data.loc[data[attrib] == val].drop(attrib,axis = 1)))
#print(s)
rule = ''
print(rule[:-2])

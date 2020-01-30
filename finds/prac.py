import csv
hypo = [i for i in '%'*6]
print(hypo)
with open('trainingexamples.csv') as csv_file:
	read_csv = csv.reader(csv_file,delimiter = ',')
	data =[]
	for row in read_csv:
		if row[-1].upper() == 'YES':
			data.append(row)
print('psositive examples :',data)
list1= []
print('the steps in find - s :')
print(hypo)
hypo = data[0][:-1]
for i in range(len(data)):
	for j in range(len(hypo)):
		if hypo[j]!=data[i][j]:
			hypo[j] = '?'
	print(hypo)
print('the maximally specific hypothesis is :')
print(hypo)

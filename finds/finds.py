import csv
hypo = ["%","%","%","%","%","%"]
with open("trainingexamples.csv") as csv_file:
	readcsv = csv.reader(csv_file,delimiter = ",")
print(readcsv)
data = []
print("\n the given training example")
for row in readcsv:
	print(row)
if row[len(row)-1].upper()=="yes":
	data.append(row)
print("\nthe positive examples are :")
for x in data:
	print(x)
print("\n")
totalexamples = len(data)
i=0
j=0
k=0
print("the steps of the finds algorithm are \n",hypo)
list = []
p=0
d=len(data[p])-1
for j in range(d):
	list.append(data[i][j])
hypo = list
i=1
for i in range(totalexamples):
	for k in range(d):
		if hypo[k] != data[i][k]:
			hypo[k] = "?"
			k = k+1
		else :
			hypo[k]
	print(hypo)
	i=i+1
print("\n the maximally specific finds hypothesis for the given training examples is")
list = []
for i in range(d):
	list.append(hypo[i])
print(list)


import csv
hypo=['%','%','%','%','%','%'];
with open ("trainingexamples.csv")as csv_file:
	readcsv=csv.reader(csv_file,delimiter=',')
	print(readcsv)
	data=[]
	print("\n the given training examples are")
	for row in readcsv:
		print(row)
		if row[-1].upper()=="YES":
			data.append(row)
print("\n the positive examples are");
for x in data:
	print(x);
print("\n");
TotalExamples=len(data);
'''i=0;
j=0;
k=0;'''
print("the steps of the find-s algorithm are\n",hypo);
list=[];
p=0;
hypo = data[0][:-1]
d=len(data[p])-1;
'''for j in range(d):
	list.append(data[i][j]);
	hypo=list;
print("list :",list,"\n")'''
i=1;
for i in range(TotalExamples):
	for k in range(d):
		if hypo[k]!=data[i][k]:
			hypo[k]='?';
			'''k=k+1;
		else:
			hypo[k];'''
	print(hypo);
	i=i+1;
print("\n the maximally specific find-s hypothesis for the given traning examples is");
list=[];
for i in range(d):
	list.append(hypo[i]);
print(list);
print(hypo)

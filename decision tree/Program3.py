import pandas as pd
import numpy as np
import math
# create a node with label and branches.
class Node:
	def __init__(self,l):
		self.label=l
		self.branches = {}
###Calculate the entropy of a dataset.
    ##The only parameter of this function is the target_col parameter which specifies the target column	
def entropy(data):
	total_ex = len(data)
	positive_ex = len(data.loc[data["Play Tennis"] == 'Y'])
	negative_ex = len(data.loc[data["Play Tennis"] == 'N'])
	entropy = 0
	if(positive_ex > 0):
		entropy = (-1)*(positive_ex/float(total_ex))*(math.log(positive_ex,2)-math.log(total_ex,2))
	if(negative_ex > 0):
		entropy += (-1)*(negative_ex/float(total_ex))*(math.log(negative_ex,2)-math.log(total_ex,2))
	return entropy
#calculate gain of all attributes
def gain(s,data,attrib):
	values = set(data[attrib])
	print(values)
	gain = s
	for val in values:
		gain -= len(data.loc[data[attrib] == val])/float(len(data))*entropy(data.loc[data[attrib] == val])
	return gain
# return attribute with maximum gain
def get_attrib(data):
	entropy_s = entropy(data)
	attribute =""
	max_gain = 0
	for attr in data.columns[:len(data.columns)-1]:
		print("attribute : ",attr)
		g = gain(entropy_s,data,attr)

		if g > max_gain:
			max_gain = g
			attribute = attr

	return attribute
#create a decision tree
def decision_tree(data):
	
	root = Node("NULL")

	if(entropy(data) == 0):
		if(len(data.loc[data[data.columns[-1]] == 'Y']) == len(data)):
			root.label = "Y"
			return root
		else:
			root.label = "N"
			return root

	if(len(data.columns) == 1):
		return
	else:
		attrib = get_attrib(data)
		root.label = attrib
		values = set(data[attrib])
	
		for val in values:
			root.branches[val] = decision_tree(data.loc[data[attrib] == val].drop(attrib,axis = 1))
		return root	

def get_rules(root,rule,rules):
	if not root.branches:
		rules.append(rule[:-2]+" => "+root.label)
		return rules

	for i in root.branches:
		get_rules(root.branches[i],rule+root.label+"="+i+" ^ ",rules)
	return rules

def test(tree,test_str):
	if not tree.branches:
		return tree.label
	return test(tree.branches[test_str[tree.label]],test_str)


data = pd.read_csv('Data3.csv')
entropy_s = entropy(data) #calculating the entropy of the root 
attrib_count = 0
cols = len(data.columns)-1
tree = decision_tree(data)
rules = get_rules(tree,"",[])
print(rules)
test_str = {}
print("Enter test case input")
for i in data.columns[:-1]:
	test_str[i] = input(i+": ")
print(test_str)
print(test(tree,test_str))


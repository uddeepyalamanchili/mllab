from sklearn.datasets from from sklearn.datasets import fetch_20newsgroups
twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
print("lenth of the twenty_train--------->", len(twenty_train))
#print(twenty_train.target_names)  #prints all the categories

print("***First Line of the First Data File***")
#print("\n".join(twenty_train.data[0].split("\n")[:5]))#prints first line of the first data file

#2 Extracting features from text files
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
print('dim=',X_train_counts.shape)
 from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(X_train_tfidf_Shape)
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf,twenty_train.target)
from sklearn.pipeline import Pipeline
text_clf = Pipeline([('vect',countVectorizer()),('tfidf',TfidfTransformer()),('clf',MultinomialNB())])
text_clf = text_clf.fit(twenty_train.data,twenty_train.target)
import numpy as np
twenty_test = fetch_20newsgroup(subset = 'test',shuffle=True)
predicted = text_clf.predicted(twenty_test_data)
accuracy = np.mean(predicted==twenty_test.target)
print("Predicted Accuracy = ",accuracy)
from sklearn import metrics
print("Accuracy = ",metrics.accuracy_score())

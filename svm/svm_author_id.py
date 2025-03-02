#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
clf = SVC(kernel='rbf', C=10000, gamma=1)

#taking only 1% of the test data
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

#print ('The accuracy is: %f' % (accuracy_score(labels_test, pred)))

chris = []
for item in pred:
	if pred[item] == 1:
		chris.append(item)
	

print len(chris)
#########################################################



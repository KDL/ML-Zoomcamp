#Ensure that the script is installed via requirements
#!pip install -r requirements.txt


#libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score, roc_curve, f1_score
from sklearn.tree import DecisionTreeClassifier
import os
import pickle

#dictionary
dv = DictVectorizer(sparse=False) #import encoder



#----------------------------- Check the database exists, then clean it
if not os.path.isfile("data/healthcare-dataset-stroke-data.csv"):
    #TODO: implement the downloaders
    print("File data/healthcare-dataset-stroke-data.csv doesn't exist, aborting file")
    exit()

#load file into dataframe
df = pd.read_csv("data/healthcare-dataset-stroke-data.csv")

# map hypertension & heartdisease
df.hypertension = df.hypertension.map({0:'No',1:'Yes'})
df.heart_disease = df.heart_disease.map({0:'No',1:'Yes'})

#change columns to lower case
df = df.rename(columns={'Residence_type':'residence_type'})


#Correcting the 201 missing values from BMI
df=df.fillna(0)



#-------------------------split according to random state = 1
df_trainval, df_test = train_test_split(df, test_size=0.2, random_state=1) #split train+val [80%], test [20%]
df_train, df_val = train_test_split(df_trainval, test_size=0.25, random_state=1) #split train[60%] val [20%]

#reset, drop index
df_train = df_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)

#use stroke as output
y_test = df_test["stroke"].values
y_train = df_train["stroke"].values
y_val = df_val["stroke"].values

del df_test["stroke"]
del df_train["stroke"]
del df_val["stroke"]

#drop id as it doesn't have any meaning
del df_test["id"]
del df_train["id"]
del df_val["id"]



#----------------------- prepare for training (Serialize data)
# Serialize non-numerical data using DictVectorizer (aka One-Hot Encoding)
train_dict = df_train.to_dict(orient='records') # get categorial variables from train db, sort them by x and put them into dictionary 
X_train = dv.fit_transform(train_dict) #one-hot encoding 
val_dict = df_val.to_dict(orient='records') #apply same 
X_val = dv.transform(val_dict)

#---------------------- Classification test function
# input: classifier, prediction function, X_train, y_train, X_val, y_val
# output: Classification Accuracy, Validation Accuracy, AUC, F1
def test_classifier(clf,predictFcn,X_train,y_train,X_val,y_val):
    clf.fit(X_train,y_train)
    y_predict = predictFcn(X_val)
    fpr, tpr, thresholds = roc_curve(y_val, y_predict)
    #roc_data = (fpr,tpr,thresholds)
    return (np.mean(predictFcn(X_train) == y_train),np.mean(predictFcn(X_val) == y_val),roc_auc_score(y_val,y_predict),f1_score(y_val,y_predict))

#---------------------- train using decision tree max_depth = 6
dt = DecisionTreeClassifier(max_depth=6)
v=test_classifier(dt,dt.predict,X_train,y_train,X_val,y_val)
pd.DataFrame(v,index=['Classification Accuracy','Validation Accuracy','AUC','F1'],columns=['D.T. max_depth = 1'])
print('Classification Accuracy:\t %2.5f\nValidation Accuracy:\t\t %2.5f\nAUC:\t\t\t\t %2.5f\nF1:\t\t\t\t %2.5f\n' %(v[0],v[1],v[2],v[3]))


#-------------------- export model into a pickle
# output file: model.bin for the model, and dv.bin for the hot one encoder
dt = DecisionTreeClassifier(max_depth=6)
v=test_classifier(dt,dt.predict,X_train,y_train,X_val,y_val)
with open("model.bin", 'wb') as f:  pickle.dump(dt,f)
with open("dv.bin", 'wb') as f: pickle.dump(dv,f)
print("Pickle file is exported to model.bin, dv.bin")
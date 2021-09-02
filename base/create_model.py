import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pickle

def create():
    train = pd.read_csv('datasets/loan-train.csv')
    test = pd.read_csv('datasets/loan-train.csv')

    train['source']='train'
    test['source']='test'

    dataset = pd.concat([train,test], ignore_index = True)

    ds = dataset.isnull().sum()

    for index, value in ds.items():
        if value > 0:
            if dataset[f"{index}"].dtypes == float:
                dataset[f"{index}"].fillna(dataset[f"{index}"].median(), inplace=True)
            elif dataset[f"{index}"].dtypes == int:
                dataset[f"{index}"].fillna(dataset[f"{index}"].median(), inplace=True)
            elif dataset[f"{index}"].dtypes == object:
                dataset[f"{index}"].fillna(dataset[f"{index}"].mode()[0], inplace=True)
                
    if dataset.isnull().sum().sum() != 0:
        print(ds)
        raise ValueError("you still still have some unfilled spaces")

    #Divide into test and train:
    train = dataset.loc[dataset['source']=="train"]
    test = dataset.loc[dataset['source']=="test"]
    #Drop unnecessary columns:
    test.drop(['source'],axis=1,inplace=True)
    train.drop(['source'],axis=1,inplace=True)

    X=train.drop(["Loan_Status",'Loan_ID'],axis=1)
    y=train["Loan_Status"]

    X = pd.get_dummies(X,drop_first=True)

    X = test.drop(["Loan_Status","Loan_ID"],axis=1)
    categorical_d = {'Male': 1, 'Female': 0}
    X['Gender'] = X['Gender'].map(categorical_d)

    categorical_d = {'Yes': 1, 'No': 0}
    X['Married'] = X['Married'].map(categorical_d)
    X['Self_Employed'] = X['Self_Employed'].map(categorical_d)

    categorical_d = {'Graduate': 1, 'Not Graduate': 0}
    X['Education'] = X['Education'].map(categorical_d)

    le = LabelEncoder()

    X['Property_Area'] = le.fit_transform(X['Property_Area'])
    X['Dependents'] = le.fit_transform(X['Dependents'])


    x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=0)
    
    LR_Model = LogisticRegression(max_iter=1000,random_state=0)
    LR_Model.fit(x_train,y_train)

    Pkl_Filename = "Pickle_RL_Model.pkl"  

    with open(Pkl_Filename, 'wb') as file:  
        pickle.dump(LR_Model, file)


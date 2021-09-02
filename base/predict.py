import pickle
import pandas as pd

Pkl_Filename = "Pickle_RL_Model.pkl" 


def loanpredictfunc(data):
    with open(Pkl_Filename, 'rb') as file:  
            Pickled_LR_Model = pickle.load(file)
            Pickled_LR_Model

    v_data = [data,]
    df = pd.DataFrame.from_dict(v_data)
    df.drop(['Loan_ID'],axis=1)

    categorical_d = {'Male': 1, 'Female': 0}
    df['Gender'] = df['Gender'].map(categorical_d)

    categorical_d = {'Yes': 1, 'No': 0}
    df['Married'] = df['Married'].map(categorical_d)
    df['Self_Employed'] = df['Self_Employed'].map(categorical_d)

    categorical_d = {'Graduate': 1, 'Not Graduate': 0}
    df['Education'] = df['Education'].map(categorical_d)


    df.drop(['Loan_ID'],axis=1, inplace=True)
    
    loan_status_predict = Pickled_LR_Model.predict(df)
    print(loan_status_predict)  

    return({'loan_id': data['Loan_ID'], 'loan_status':loan_status_predict[0]})
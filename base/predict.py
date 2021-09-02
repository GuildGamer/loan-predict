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
    
    loan_status_predict = Pickled_LR_Model.predict(df)  

    return({'loan_id': data['Loan_ID'], 'loan_status':loan_status_predict})
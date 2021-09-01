import pickle

Pkl_Filename = "Pickle_RL_Model.pkl" 


def loanpredictfunc(data):
    with open(Pkl_Filename, 'rb') as file:  
            Pickled_LR_Model = pickle.load(file)
            Pickled_LR_Model
    # Predict the Labels using the reloaded Model
    loan_status_predict = Pickled_LR_Model.predict(data)  

    return({'loan_id': data['loan_id'], 'loan_status':loan_status_predict})
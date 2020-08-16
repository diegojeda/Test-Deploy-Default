import numpy as np
import joblib

# prediction function 
def ValuePredictor(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, 12) 
    loaded_model = joblib.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict) 
    return result


def nueva():


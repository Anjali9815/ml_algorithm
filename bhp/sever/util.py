import json, pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore")


__location = None
__data_column = None
__model = None



def get_estimated_price(sqft, bath, bhk, location):

    try:
        loc_index = __data_column.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_column))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def get_location_name():
    return __location

def load_saved_artifact():
    print("loading saved artifacts...start")
    global __data_column
    global __location
    global __model
    with open("D:/Workspace/ML_ALGO/bhp/sever/artifacts/columns.json", "r") as f:
        __data_column = json.load(f)['data_col']
        __location = __data_column[3:]

    with open("D:/Workspace/ML_ALGO/bhp/sever/artifacts/banglore_price_pred_model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("loading saved artifacts..done")

if __name__ == "__main__":
    load_saved_artifact()
    print(get_location_name())
    print(get_estimated_price(1000, 2, 3, '8th phase jp nagar'))
    print(get_estimated_price(1500, 2, 2, '8th phase jp nagar'))
    print(get_estimated_price(1800, 2, 3, '2nd phase judicial layout'))
    print(get_estimated_price(850, 1, 1, 'akshaya nagar'))

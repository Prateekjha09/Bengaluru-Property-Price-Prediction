import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath): # returning the estimated price which takes few arguments and returns price for given features sent as parameters
    # noinspection PyBroadException
    try:
           loc_index = __data_columns.index(location.lower()) # converted to lower as every column value in json is in lowercase
    except:
        loc_index = -1 # if unable to find the index

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2) # prices in lakhs


def load_saved_artifacts(): # columns and prices are stored here..
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("columns.json", "r") as f: # loading json file dictionary into data columns variable..
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk and 4 one has location details..

    global __model
    if __model is None:
        with open('banglore_home_prices_model.pickle', 'rb') as f: # model is loaded here
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    #print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    #print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    #print(get_estimated_price('Kalhalli', 1000, 2, 2))  # other location
    #print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location

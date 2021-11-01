
# import libraries
from flask import Flask
from flask import request
from flask import jsonify

import numpy as np
import pandas as pd
import pickle 

#load models
with open("model.bin", 'rb') as f: dt = pickle.load(f)
with open("dv.bin", 'rb') as f: dv = pickle.load(f)

#config app Flask
app = Flask('stroke')

@app.route('/predict', methods=['POST']) #/predict as gateway
def predict():
    data = request.get_json() #get json data as dict
    print(data) #print them (comment me)

    X = dv.transform(data) #Serialize data using one-hot encode (loaded file)
    y_pred = dt.predict(X) #predict using the DT/maxdep=6 (loaded file)
    
    result = {
        'stroke_predict': int(y_pred)
    } #only one result, as we are using decision tree

    return jsonify(result) #convert dict to json string and serve them


if __name__ == "__main__":    app.run(debug=True, host='0.0.0.0', port=9696) #serve in local host via port 9696, with verbose output
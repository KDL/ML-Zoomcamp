import numpy as np
import pandas as pd
import pickle 

#import sklearn
#sklearn_version = sklearn.__version__
#print(sklearn_version)

with open("dv.bin", 'rb') as f: dv = pickle.load(f)
with open("model1.bin", 'rb') as f: model = pickle.load(f)

c = { "contract": "two_year", "tenure": 12, "monthlycharges": 19.7} #customer, updated according to features
X = dv.transform([c])
prob = model.predict_proba(X)[:,1]
print("Probability that customer A is churning is %.3f" % prob)


import requests
url = "http://127.0.0.1:8001/predict"
customer = {"contract": "two_year", "tenure": 1, "monthlycharges": 10}
results = requests.post(url, json=customer).json()
print("Probability that a user is churning: %2.3f" % results["churn_probability"])
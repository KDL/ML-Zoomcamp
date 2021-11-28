import requests
#import json
#url="http://localhost:8080/"
url='http://localhost:8080/2015-03-31/functions/function/invocations'
data = {'url': 'https://upload.wikimedia.org/wikipedia/commons/1/18/Vombatus_ursinus_-Maria_Island_National_Park.jpg'}
res = requests.post(url,json=data).json()
print(res)


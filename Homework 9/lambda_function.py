#import libs
#import tensorflow as tf
#from tensorflow import keras
import numpy as np


#import tensorflow.lite as tflite
import tflite_runtime.interpreter as tflite
interpreter = tflite.Interpreter(model_path = 'cats-dogs-v2.tflite')
interpreter.allocate_tensors()

#interpreter.get_input_details()
iindex = interpreter.get_input_details()[0]['index']
oindex = interpreter.get_output_details()[0]['index']
print("Input index: %d | Output index: %d" % (iindex,oindex))


from io import BytesIO
from urllib import request

from PIL import Image

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img


def predict(url):
    img = download_image(url)
    img = prepare_image(img, (150,150)) #format according to last homework RGB 150x150
    

    #preprocess img
    x = np.array(img);
    X = np.array([x*1.0/255],dtype=np.float32)
    
   

    interpreter.set_tensor(iindex, X)
    interpreter.invoke()
    return  {'res': interpreter.get_tensor(oindex)[0].tolist()}
   


def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result


#load img




FROM agrigorev/zoomcamp-cats-dogs-lambda:v2


RUN pip install keras-image-helper

RUN pip install --upgrade pip

RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp38-cp38-linux_x86_64.whl

COPY ["requirements.txt", "lambda_function.py", "./"]
#COPY ["requirements.txt", "lambda_function.py", "predict.py", "./"]

RUN pip install -r requirements.txt


CMD ["lambda_function.lambda_handler"]
#CMD ["predict"]


FROM agrigorev/zoomcamp-cats-dogs-lambda:v2


WORKDIR .

RUN pip install --upgrade pip

COPY ["requirements.txt", "predict.py", "./"]

RUN pip install -r requirements.txt

RUN python predict.py

ENTRYPOINT ["python", "predict.py"]


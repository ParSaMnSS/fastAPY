# uvicorn main:app --reload
from fastapi import FastAPI
from enum import Enum

class Modelname(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

app = FastAPI()

# get is to read, and post is to create data; put is to update and delete is to... delete


@app.get("/models/{model_name}")
async def getmodel(model_name: Modelname):
    if model_name is Modelname.alexnet:
        return {"use jinja2 for render template, model_name:": model_name, 'message':'SOLJABOI'}
    if model_name.value == 'lenet':
        return {'model_name': model_name, 'message':'LeCNN all images'}
    return {'model_name':model_name, 'message':'Have some residentials'}

@app.get('/files/{file_path:path}')
async def read_file(file_path:str):
    return {'file_path': file_path}


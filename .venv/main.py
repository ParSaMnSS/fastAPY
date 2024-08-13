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

# QUERIES: 
# function parameters that are not part of the path parameters

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]



@app.get("/items1/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# By not defining a default value "| None = None", You make the parameter required 

@app.get("/item/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item 


@app.get('/items2/{item_id}')
async def read_user_item(
    item_id : str,  needy: str, skip: int = 0, limit: int | None = None
):
    item = {'item_id': item_id, 'needy': needy, 'skip': skip, 'limit': limit}
    return item
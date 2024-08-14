from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get('/items/')
async def read_items(q: Annotated[str | None, Query(max_length=50)]=None):
    result = {'items' : [{'item_id':'Foo'}, {'item_id':'Bar'}]}
    if q:
        result.update({'q':q})
    return result

# "q: str | None = Query(default=None)" the same as " q: str | None = None"
# ...makes the parameter optional


# More validation

@app.get('/items/something')
async def read_the_items(q: Annotated[str, Query(min_length=3, max_length=50, pattern='^fixedquery@email.com$')] = None):
    results = {'items':[{'item_id':'Foo'}, {'item_id':'Bar'}]}
    if q: 
        results.update({'q':q})
    return results

# Query parameter list / multiple values

@app.get('/itemss/')
async def read_itemss(q: Annotated[list[str] | None, Query()] = None):
# async def read_items(q: Annotated[list, Query()] = []):
# async def read_itemss(q: Annotated[list[str] | None, Query()] = ['foo', 'bar']):  NOTE: fixed parameters
    query_items = {'q':q}
    return query_items


# More metadata
# You can add a "title" and a "description" 
# alias is what will be used to find the parameter value

@app.get('/something/')
async def read_items(q:Annotated[str | None, Query(
    alias='item-query',
    title='Wake yo ahh up cuz its time to go beast mode',
    description='something something long someone out',
    min_length=3, 
    max_length=50, 
    pattern='^fixedquery$',
    deprecated=True
    )] = None):
    results = {'items': [{'item_id':'Foo'}, {'item_id':'Bar'}]}
    if q: 
        results.update({'q':q})
    return results
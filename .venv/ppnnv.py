from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()

@app.get('/items/{item_id}')
async def read_items(
    item_id: Annotated[int, Path(title="The id of the item to get")],
    q: Annotated[str | None, Query(alias='item-query')] = None
):
    results = {'item_id': item_id}
    if q: 
        results.update({'q':q})
    return results
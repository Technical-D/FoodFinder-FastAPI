from fastapi import FastAPI, HTTPException
from auth import get_access_token
import requests

app = FastAPI()

FOOD_SEARCH_URL = "https://platform.fatsecret.com/rest/server.api"

@app.get("/search")
def search_food(query:str, page_number:int=0, max_results:int=10):
    token = get_access_token()
    params = {
        "method": "foods.search.v3",
        "format": "json",
        "search_expression": query,
        "page_number": page_number,
        "max_results": max_results
    }

    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(FOOD_SEARCH_URL, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data")
    

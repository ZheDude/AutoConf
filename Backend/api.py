from dotenv import load_dotenv
from fastapi import FastAPI, Request
import uvicorn
import os

app = FastAPI()

def process_data(data: dict):
    print("Processing data:", data)
    return {"processed_data": data}


@app.post("/configuration/")
async def receive_json(request: Request):
    json_data = await request.json()
    result = process_data(json_data)
    return result


if __name__ == "__main__":
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)

import json

# from dotenv import load_dotenv
from fastapi import FastAPI, Request
import uvicorn
import os

from config_processor import get_list_of_konfigurations

app = FastAPI()

def process_data(data: dict):
    # print("Processing data:", data)
    print("HELLO THIS IS WHERE DAFUQ I AM :LSDKJF:SLDKFJS:DLKFJS:DLKFJS:DLKFJSD:LKFJSD:LFKJSD:LFKJSD")
    json_string = json.dumps(data)
    print(json_string)

    konfig_liste = get_list_of_konfigurations(json_string)

    for element in konfig_liste:
        print(element)
    return konfig_liste


@app.post("/configuration/")
async def receive_json(request: Request):
    json_data = await request.json()
    result = process_data(json_data)
    return result


if __name__ == "__main__":
    # load_dotenv()
    # API_KEY = os.getenv("API_KEY")
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
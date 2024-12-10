import json
import os

import uvicorn
from fastapi import FastAPI, Request, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware

from config_processor import get_list_of_konfigurations


SECRET_TOKEN = os.getenv("SECRET_TOKEN", "your-secure-token")
SECRET_TOKEN = "CHICKEN"
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://specific-origin1.com",],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],

)


def process_data(data: dict):
    # print("Processing data:", data)
    print("HELLO THIS IS WHERE DAFUQ I AM :LSDKJF:SLDKFJS:DLKFJS:DLKFJS:DLKFJSD:LKFJSD:LFKJSD:LFKJSD")
    json_string = json.dumps(data)
    print(json_string)

    configuration_processer_tuple = get_list_of_konfigurations(json_string)
    konfig_liste = configuration_processer_tuple[1]
    ssh_ip = configuration_processer_tuple[0]
    # TODO MEHMET SWITCH SACHEN LAUFEN LASSEN
    print(ssh_ip, " HELLO THIS IS THE IP ")
    print(konfig_liste)

    for element in konfig_liste:
        print(element)
    if len(konfig_liste) == 0:
        raise HTTPException(status_code=404, detail="No Valid Configuration")
    return konfig_liste


@app.post("/configuration/")
async def receive_json(
    request: Request,
    authorization: str = Header(None)  # Expect the token in the Authorization header
):
    '''
    origin = request.headers.get("Origin")
    if origin not in ALLOWED_ORIGINS:
        raise HTTPException(status_code=403, detail="Origin not allowed")
    '''

    # Enforce the secret token
    if authorization != f"Bearer {SECRET_TOKEN}":
        raise HTTPException(status_code=403, detail="Invalid or missing token")

    # Enforce Content-Type header
    if request.headers.get("Content-Type") != "application/json":
        raise HTTPException(
            status_code=400, detail="Content-Type must be application/json"
        )

    json_data = await request.json()
    result = process_data(json_data)
    return result


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True,
                ssl_certfile=r"C:\\Users\Sai\Documents\GitHub\AutoConf\Backend\server.crt",
                ssl_keyfile=r"C:\\Users\Sai\Documents\GitHub\AutoConf\Backend\server.key")

    # uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)


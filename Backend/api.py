import json
import logging
import os
import sys

import uvicorn
#from dotenv import load_dotenv
# from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from config_processor import get_list_of_konfigurations

app = FastAPI()
#load_dotenv()
#SECRET_TOKEN = os.getenv("SECRET_TOKEN", "default-token-chicken")
#SSL_CERTFILE = os.getenv("SSL_CERTFILE")
#SSL_KEYFILE = os.getenv("SSL_KEYFILE")
app = FastAPI()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"
)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)


def process_data(data: dict):
    """
    Processes incoming configuration data and returns the result.

    :param data: Input JSON data
    :return: List of configurations
    """
    json_string = json.dumps(data)
    logger.info("Received Data: %s", json_string)

    configuration_processer_tuple = get_list_of_konfigurations(json_string)
    konfig_liste = configuration_processer_tuple[1]
    ssh_ip = configuration_processer_tuple[0]
    logger.info("SSH IP: %s", ssh_ip)
    logger.info("Configurations: %s", konfig_liste)

    if ssh_ip:
        from connections import SSHConnection
        #dev1 = SSHConnection(ssh_ip, "cisco", "cisco")
        #result = dev1.send_command_imprvd("configure terminal\n    ")
        #print(result)
        #result = dev1.send_command_imprvd("do-exec show running\n    ")
        #print(result)
        for element in konfig_liste:
            #result = dev1.send_command_imprvd(element)
            print(element)
        print("Configurations applied successfully.")
    else:
        print("No SSH data found.")
        for element in konfig_liste:
            print(element)

    if len(konfig_liste) == 0:
        raise HTTPException(status_code=404, detail="No Valid Configuration")
    return konfig_liste

def process_data_testing(data: dict):
    json_string = json.dumps(data)

    configuration_processer_tuple = get_list_of_konfigurations(json_string)
    ssh_ip = configuration_processer_tuple[0]
    
    if ssh_ip:
        from connections import SSHConnection
        print("Configurations applied successfully.")
    else:
        print("No SSH data found.")

    if len(ssh_ip) == 0:
        raise HTTPException(status_code=404, detail="No Valid Configuration")
    return None

@app.post("/configuration/")
async def receive_json(request: Request):
    if request.headers.get("Content-Type") != "application/json":
        raise HTTPException(
            status_code=400, detail="Content-Type must be application/json"
        )
    json_data = await request.json()
    result = process_data(json_data)
    return result

@app.post("/configuration/")
async def receive_json(
        request: Request,
        authorization: str = Header(None)

):
    """
    Receives JSON configuration via POST request with Authorization Header.

    :param request: Incoming request object
    :param authorization: Bearer token for authentication
    :return: Processed configurations
    """

    """
    print(authorization, "this is the authorization header")
    if authorization != f"Bearer {SECRET_TOKEN}":
        logger.warning("Unauthorized access attempt")
        raise HTTPException(status_code=403, detail="Invalid or missing token")

    """

    if request.headers.get("Content-Type") != "application/json":
        logger.warning("Invalid Content-Type in request")
        raise HTTPException(
            status_code=400, detail="Content-Type must be application/json"
        )

    json_data = await request.json()
    result = process_data(json_data)
    return result

@app.get("/metadata/switch")
async def get_metadata_switch():
    import switch_meta_vars as swmv
    try:
        switch = swmv.switch_meta_vars("172.16.2.127", "cisco", "cisco")
    except Exception as e:
        return {"error": str(e)}
    return {"Interfaces": switch.extract_interfaces(), "Neighbors": switch.extract_neighbors()}

@app.get("/metadata/router")
async def get_metadata_router():
    return {"Top Secret! This is a government project. Authorized users only!": "https://www.youtube.com/watch?v=k85mRPqvMbE"}



if __name__ == "__main__":
    # load_dotenv()
    # API_KEY = os.getenv("API_KEY")
    uvicorn.run(
        "api:app",
        host="127.0.0.1",
        port=8000,
        reload=True
        #,
        #ssl_certfile=SSL_CERTFILE,
        #ssl_keyfile=SSL_KEYFILE
    )


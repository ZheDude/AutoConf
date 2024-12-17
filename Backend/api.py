import json
import logging
import os
import sys

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware

from config_processor import get_list_of_konfigurations

load_dotenv()
SECRET_TOKEN = os.getenv("SECRET_TOKEN", "default-token-chicken")
SSL_CERTFILE = os.getenv("SSL_CERTFILE")
SSL_KEYFILE = os.getenv("SSL_KEYFILE")
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
    allow_origins=["https://specific-origin1.com", ],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],

)


def process_data(data: dict):
    """
    Processes incoming configuration data and returns the result.

    :param data: Input JSON data
    :return: List of configurations
    """
    # print("Processing data:", data)
    json_string = json.dumps(data)
    logger.info("Received Data: %s", json_string)

    configuration_processer_tuple = get_list_of_konfigurations(json_string)
    konfig_liste = configuration_processer_tuple[1]
    ssh_ip = configuration_processer_tuple[0]
    logger.info("SSH IP: %s", ssh_ip)
    logger.info("Configurations: %s", konfig_liste)

    for element in konfig_liste:
        print(element)
    if len(konfig_liste) == 0:
        raise HTTPException(status_code=404, detail="No Valid Configuration")
    return konfig_liste


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

    # Enforce the secret token
    if authorization != f"Bearer {SECRET_TOKEN}":
        logger.warning("Unauthorized access attempt")
        raise HTTPException(status_code=403, detail="Invalid or missing token")

    # Enforce Content-Type header
    if request.headers.get("Content-Type") != "application/json":
        logger.warning("Invalid Content-Type in request")
        raise HTTPException(
            status_code=400, detail="Content-Type must be application/json"
        )

    json_data = await request.json()
    result = process_data(json_data)
    return result


if __name__ == "__main__":
    uvicorn.run(
        "api:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        ssl_certfile=SSL_CERTFILE,
        ssl_keyfile=SSL_KEYFILE
    )

    # uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)

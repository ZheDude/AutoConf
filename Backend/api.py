import json

import uvicorn
# from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from config_processor import get_list_of_konfigurations

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)


def process_data(data: dict):
    # print("Processing data:", data)
    #print("HELLO THIS IS WHERE DAFUQ I AM :LSDKJF:SLDKFJS:DLKFJS:DLKFJS:DLKFJSD:LKFJSD:LFKJSD:LFKJSD")
    json_string = json.dumps(data)
    #print(json_string)

    configuration_processer_tuple = get_list_of_konfigurations(json_string)
    konfig_liste = configuration_processer_tuple[1]
    ssh_ip = configuration_processer_tuple[0]
    # TODO MEHMET SWITCH SACHEN LAUFEN LASSEN
    #print(ssh_ip, " HELLO THIS IS THE IP ")
    #print(konfig_liste)

    #for element in konfig_liste:
    #    print(element)
    
    if ssh_ip:
        from connections import SSHConnection
        dev1 = SSHConnection(ssh_ip, "cisco", "cisco")
        result = dev1.send_command_imprvd("configure terminal\n    ")
        print(result)
        result = dev1.send_command_imprvd("do-exec show running\n    ")
        print(result)
        print("Configurations applied successfully.")
    else:
        print("No SSH data found.")

    if len(konfig_liste) == 0:
        raise HTTPException(status_code=404, detail="No Valid Configuration")
    return konfig_liste


@app.post("/configuration/")
async def receive_json(request: Request):
    if request.headers.get("Content-Type") != "application/json":
        raise HTTPException(
            status_code=400, detail="Content-Type must be application/json"
        )
    json_data = await request.json()
    result = process_data(json_data)
    return result


if __name__ == "__main__":
    # load_dotenv()
    # API_KEY = os.getenv("API_KEY")
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)

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
    json_string = json.dumps(data)

    configuration_processer_tuple = get_list_of_konfigurations(json_string)
    konfig_liste = configuration_processer_tuple[1]
    ssh_ip = configuration_processer_tuple[0]
    
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

@app.post("/configuration/deviceip")
async def receive_json(request: Request):
    if request.headers.get("Content-Type") != "application/json":
        raise HTTPException(
            status_code=400, detail="Content-Type must be application/json"
        )
    json_data = await request.json()
    result = process_data_testing(json_data)
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
    return {"metadata": "This is the metadata"}



if __name__ == "__main__":
    # load_dotenv()
    # API_KEY = os.getenv("API_KEY")
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)


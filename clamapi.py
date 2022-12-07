import clamd
import os
from fastapi import FastAPI,File, UploadFile
import random
import string

app = FastAPI()

clamav = clamd.ClamdNetworkSocket()
print(clamav.ping())
print(clamav.version())

@app.get("/healthcheck")
def healthcheck(ping=None):
    if ping == None:
        return {"healthy"}
    return {ping}


@app.get("/clamav-ping")
def clamav_ping():
    return {clamav.ping()} 

@app.get("/clamav-version")
def clamav_version():
    return {clamav.version()} 

@app.post("/scan-file")
def hello(file: UploadFile = File(...)):
    temp_filename = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits , k=15))
    save_file = r"C:\\temp\\" + temp_filename
    try:
        contents = file.file.read()

        os.makedirs(os.path.dirname(save_file), exist_ok=True)
        with open(save_file, 'wb') as f:
            f.write(contents)
        scan_results = clamav.scan(save_file)
        clean_result = scan_results.values()

    except Exception as e:
        print(e)
        return {"message": "There was an error scanning the file " + e }
    finally:
        file.file.close()
        os.remove(save_file)
    return {"result": clean_result}

'''
clamav = clamd.ClamdNetworkSocket()
print(clamav.ping())
print(clamav.version())
print(clamav.scan(r"C:\\Users\\lab_e\\Desktop\\repos\\clamav-api\\clamapi.py"))
'''
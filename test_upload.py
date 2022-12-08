import requests
import time

url = 'http://127.0.0.1:8000/scan-file'
for x in range(1):
    with open(r"eicar.txt", 'r') as file:
        file = {'file': file}
        resp = requests.post(url=url, files=file) 
        print(resp.json())
        print(x)

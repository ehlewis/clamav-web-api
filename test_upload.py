import requests
import time

url = 'http://127.0.0.1:5000/scan-file'
for x in range(10):
    with open(r"testfiles\\Docker.exe", 'rb') as file:
        file = {'file': file}
        resp = requests.post(url=url, files=file) 
        print(resp.json())
        print(x)

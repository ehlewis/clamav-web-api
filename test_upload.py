import requests

url = 'http://127.0.0.1:8000/scan-file'
#file = open(r'C:\\Users\\lab_e\\Desktop\\test.txt', 'r')
file = open(r"C:\\Users\\lab_e\\Desktop\\repos\\clamav-api\\eicar.txt", 'r')

file = {'file': file}
resp = requests.post(url=url, files=file) 
print(resp.json())
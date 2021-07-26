import urllib.request
import requests
import numpy as np

ipwebcap_url="http://192.168.1.108:8080/shot.jpg"
fastapi_post_url = "http://3.26.64.174/predict/"
# fastapi_post_url ="http://127.0.0.1/predict/"

while True:
 imgResp=urllib.request.urlopen(ipwebcap_url)
 imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
 print(imgNp)
 
 try:
     r = requests.post(fastapi_post_url, files={'file':imgNp})
     print(r.status_code)
     num_ppl=r.json()['num_ppl']
 except Exception as e:
     pass
     print('Error: ',e)
     num_ppl=-999
 print( f'Number of people in the frame is {num_ppl}')

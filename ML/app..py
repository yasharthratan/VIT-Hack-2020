import requests
filename='D:/IP-App-Price-Tracker/src/invoice_recognition/reciept_image_dataset/1204-receipt.jpg'
url = 'http://127.0.0.1:5000/'  #I've used this for testing purpose

files={"file":(open(filename,"rb"))}
headers={'authorisation' : "Bearer {token}"}
response = requests.request('POST', url, files=files, headers=headers)
print(response.text)

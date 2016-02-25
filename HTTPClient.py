import requests
url = 'http://128.199.160.37:12055'
files = {'file': open('testImage.jpg', 'rb')}
r = requests.post(url, files=files)
print r.status_code
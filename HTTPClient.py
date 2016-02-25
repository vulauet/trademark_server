import requests
url = 'http://128.199.160.37:12055/trademark'
files = {'file': open('trademark.jpg', 'rb')}
r = requests.post(url, files=files)
print r.status_code
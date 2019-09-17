import requests
print("1+1=")
r = requests.get("http://127.0.0.1:5000/compute/sum?parma=1&parmb=1")
assert r.status_code == 200
print(r.text)

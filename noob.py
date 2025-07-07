from flask import Flask
import requests

app = Flask(__name__)

HASH_VALUE = "f972eecea9030dbe6efe"
POST_API = "https://mdproxyvpn.com/v1/json/update"
FAKE_DATA = "eLw3EV0c5sOmv1h20Ci3VNI8MNXMAg+g6rtrtrt"

@app.route('/')
def home():
    payload = {
        "hash": HASH_VALUE,
        "code": FAKE_DATA
    }
    try:
        response = requests.post(POST_API, data=payload)
        return "Upload Success: " + response.text
    except Exception as e:
        return "Exception: " + str(e)

if __name__ == '__main__':
    app.run()

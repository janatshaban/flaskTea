import os
from flask import Flask
import requests

app = Flask(__name__)

HASH_VALUE = os.getenv("HASH_VALUE")
POST_API = os.getenv("POST_API")
FAKE_DATA = os.getenv("FAKE_DATA")

@app.route('/')
def home():
    if not all([HASH_VALUE, POST_API, FAKE_DATA]):
        return "Error: Missing configuration."

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

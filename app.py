from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    azure_secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

    return "Hello from Defender Scan test image!"



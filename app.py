from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    aws_access_key_id = "AKIAIOSFODNN7EXAMPLE"
    aws_secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

    return "Hello from Defender Scan test image!"



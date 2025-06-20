from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Defender Scan test image!"

# Dummy GitHub token: ghp_FAKE1234567890EXAMPLETOKEN
# Dummy Azure secret: DefaultEndpointsProtocol=https;AccountName=fake;AccountKey=abc123==
# Dummy password: password=MySecret123!

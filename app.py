from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "RootBound Demo Running"

@app.route("/data")
def get_data():
    # File access
    with open("data.txt", "r") as f:
        file_data = f.read()

    # Network call
    response = requests.get("https://api.github.com")

    return jsonify({
        "file": file_data,
        "status_code": response.status_code
    })

if __name__ == "__main__":
    app.run(port=5000)
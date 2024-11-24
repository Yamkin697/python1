from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello, World! This is running in Docker!")

@app.route("/status")
def status():
    return jsonify(status="OK", uptime="24 hours")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

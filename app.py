 # Flask app# Files to ignore in Docker build
from flask import Flask, jsonify
app =Flask(__name__)
print("APP is running using Docker and jenkins-------")
@app.route("/")
def home():
    return jsonify({"message": "APP is running using Docker and jenkins"}),200

@app.route("/status")
def status():
    return jsonify({"status": "ok-app is running ","version": "1.0.0"})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 5009, debug=False)
# testing ci/cd again
# another cicd flow test
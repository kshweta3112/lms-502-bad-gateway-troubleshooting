from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "LMS Backend is running"

@app.route("/actuator/health")
def health():
    return jsonify(status="UP")

@app.route("/api/courses")
def courses():
    return jsonify([
        {"id": 1, "name": "Python"},
        {"id": 2, "name": "AWS"},
        {"id": 3, "name": "Docker"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

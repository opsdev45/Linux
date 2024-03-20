from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, from my Flask app in a Docker container!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)  # Expose app on all interfaces, port 8000
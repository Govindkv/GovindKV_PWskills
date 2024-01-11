from flask import Flask

app = Flask(__name__)

@app.route("/govind")
def home_page():
    return "This is my homepage"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000

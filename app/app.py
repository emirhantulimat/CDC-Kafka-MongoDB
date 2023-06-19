from flask import Flask, render_template, request
from pymongo import MongoClient
import socket

myip = socket.gethostbyname(socket.gethostname())
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        client = MongoClient("mongodb://mongo:27017/")
        db = client["mydatabase"]
        collection = db["mycollection"]
        key = request.form.get("key")
        value = request.form.get("value")
        data = {"key": key, "value": value}
        collection.insert_one(data)
        client.close()

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

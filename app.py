from flask import Flask, request


app = Flask(__name__)


@app.route("/localhost:80", methods=["GET"])
def method_name():
    two = 1 + 1
    print(two)

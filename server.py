from flask import Flask, Response
import random
import time

print(__name__)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/weights")
def stream():
    def eventStream():
        while True:
            time.sleep(1)
            print("about to yield")
            yield "data: hello \n\n"
    return Response(eventStream(), mimetype="text/event-stream")
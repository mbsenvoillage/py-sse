from flask import Flask, Response
import time

app = Flask(__name__)
@app.route("/weights")
def stream():
    def eventStream():
        while True:
            time.sleep(1)
            print("about to yield")
            yield "data: hello \n\n"
    return Response(eventStream(), mimetype="text/event-stream")
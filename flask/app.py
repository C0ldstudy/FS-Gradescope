"""
Author: c0ldstudy
2022-03-23 13:44:32
"""

import flask
from flask import Flask
from os.path import join
import argparse

app = flask.Flask(__name__)
app.config["DEBUG"] = False

def server_run(IP_ADDR, PORT, DEBUG):
    print(IP_ADDR, PORT, DEBUG)
    @app.route("/", methods=["GET"])
    def home():
        return "<h1>The File Receiving Server</p>"

    @app.route('/save_files', methods=['POST'])
    def save_files():
        print("save files")
        student_name = request.form["student_name"]
        task = request.form["task"]
        path = "submission/" + str(task) + "/" + str(task) + "-" + str(student_name) + "-" + time.strftime("%Y%m%d_%H%M%S") + "/"
        if not os.path.exists(path):
            os.makedirs(path)
        for name, file in request.files.items():
            file.save(os.path.join(path, name))
        return {"feedback": "Server received the files successfully!"}

    print("File receiving server is running...")
    app.run(host=IP_ADDR, port=PORT, debug=DEBUG)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Receing Server")
    parser.add_argument('--ip_addr', type=str, default='127.0.0.1', help='Set to 0.0.0.0 if the server needs to receive outside requests.')
    parser.add_argument('--port', type=str, default='5000', help='Set to 443 if it is needed.')
    parser.add_argument('--debug', type=bool, default=False)

    args = parser.parse_args()
    server_run(IP_ADDR=args.ip_addr, PORT=args.port, DEBUG=args.debug)

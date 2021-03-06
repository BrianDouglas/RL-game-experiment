import os
from datetime import datetime
import json
import pymongo
import os
import bd_config

from flask import Flask, session, render_template, request, jsonify
#from flask_socketio import SocketIO, emit

from GameEnv import GameEnv
from ModelBuilder import *

bd_config.init()
LOAD_DB = True

app = Flask(__name__)
#app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
#socketio = SocketIO(app)

#landing page
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/machine")
def machine():
    return render_template("machine.html")

@app.route("/game_data", methods=['POST'])
def game_data():
    data = request.get_json()
    if (LOAD_DB):
        connectTo = 'final_project'
        client = pymongo.MongoClient(f"mongodb+srv://{bd_config.USERNAME}:{bd_config.PASSWORD}@bricluster.yskth.mongodb.net/{connectTo}?retryWrites=true&w=majority")
        db = client.final_project
        collection = db.state_action
        collection.insert_many(data)
        client.close()
    else:
        print(data)
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)
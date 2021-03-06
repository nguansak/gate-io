from flask import (
    Flask, 
    render_template,
    request,
    jsonify,
    send_from_directory,
)
from gate_service import *
import sqlite3
import json
from db import *
from datetime import datetime
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

today = datetime.today().strftime('%Y-%m-%d')
path = "data/" + today
try:
    os.mkdir(path)
except:
    print("exist path")

app = Flask(__name__, template_folder="public")
#app.config["DEBUG"] = True
service = GateService(60) 
db = Db(path+"/data.db")
db.initDb()

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('./public/js', path)

@app.route('/gate/<string:gateCode>', methods=['GET', 'POST'])
def gate(gateCode):
    if request.method == 'GET':
        info = service.gateInfo(gateCode)
        return jsonify(info)

@app.route('/gate/<string:gateCode>/raw', methods=['GET', 'POST'])
def gateRaw(gateCode):
    if request.method == 'POST':
        data = request.data.decode("utf-8")
        if gateCode == "test":
            service.handleGateRaw(gateCode, data)
        return jsonify({})


@app.route('/gate/<string:gateCode>/json', methods=['GET', 'POST'])
def gateJson(gateCode):
    if request.method == 'POST':
        data = request.json
        service.handleGateJson(gateCode, data)
        return jsonify({})


@app.route('/gate/<string:gateCode>/counter', methods=['GET', 'POST'])
def gateCounter(gateCode):
    if request.method == 'POST':
        data = request.json
        service.handleGateCounter(gateCode, data)
        return jsonify({})


@app.route('/total', methods=['GET'])
def total():
    total = service.getTotal()
    return jsonify(total)

#app.run(debug=True, host='0.0.0.0', port=5000)
app.run(host='0.0.0.0', port=5000)

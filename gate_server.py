from flask import (
    Flask, 
    render_template,
    request,
    jsonify,
)
from gate_service import *
import sqlite3
import json

app = Flask(__name__, template_folder="publics")
#app.config["DEBUG"] = True
service = GateService() 

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

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

#app.run(debug=True, host='0.0.0.0', port=5000)
app.run(host='0.0.0.0', port=5000)

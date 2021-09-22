import flask
import json
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

x = '{ "name":"John", "age":30, "city":"New York"}'

@app.route('/', methods=['GET'])
def home():
    return "You have 2 functions: getX and getAge"

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/getX', methods=['GET'])
def getx():
    return jsonify(x)

@app.route('/api/v1/getAge', methods=['GET'])
def getName():
    return jsonify(json.loads(x)["age"])

#app.run(host="localhost", port=8080, debug=True,ssl_context=('cert.pem', 'key.pem'))
app.run(host="127.0.0.1", port=8080, debug=False,threaded=True)
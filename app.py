import math

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/sqrt', methods=['GET'])
def add_message():
    if 'value' not in request.args:
        return 'No value in request', 400
    response = {'result': math.sqrt(float(request.args['value']))}
    return jsonify(response)


@app.route('/sum', methods=['GET'])
def add_message_of_sum():
    if 'value' not in request.args:
        return 'No value in request', 400
    total = sum([int(x) for x in request.args['value'].split('_')])
    response = {'result': total, 'Message': 'Evthg is fuckin awesome'}
    return jsonify(response)


if __name__ == '__main__':
    app.run()

import math

from flask import Flask, request, jsonify
from time import sleep

app = Flask(__name__)


@app.route('/')
def hello_world():
    sleep(60)
    return 'Hello World!'


@app.route('/summa', methods=['GET'])
def add_message():
    if 'value' not in request.args:
        return 'No value in request', 400
    newer = request.args['value'].split('_')
    summa = 0
    for i in newer:
        summa += int(i)
    response = {'result': summa, 'Message': 'Evthg is fuckin awesome'}
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

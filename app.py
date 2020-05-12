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
    print(request.args)
    if 'value' not in request.args:
        return 'No value in request', 400
    newer = request.args['value'].split('_')
    summa = 0
    for i in newer:
        summa += int(i)
    response = {'result': summa, 'Message': 'Evthg is fuckin awesome'}
    return jsonify(response)


if __name__ == '__main__':
    app.run()

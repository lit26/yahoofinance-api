import flask
from flask import request, jsonify, abort
from yahoofinanceapi.ticker import Ticker

app = flask.Flask(__name__)
app.config["DEBUG"] = True

ticker = Ticker()
@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to yafoo finance api</h1>"

@app.route('/api/v1/history', methods=['GET'])
def history():
    if 'symbol' not in request.args or \
        'start_day' not in request.args or \
        'end_day' not in request.args:
        return abort(400)

    results = {'metadata':{'symbol':request.args['symbol']}}
    if 'interval' not in request.args:
        results['metadata']['interval'] = request.args['interval']
        data = ticker.history_data(request.args['symbol'],
                                    request.args['start_day'],
                                    request.args['end_day'],
                                    'history')
        results['data'] = data
    else:
        results['metadata']['interval'] = request.args['interval']
        data = ticker.get_data(request.args['symbol'],
                                request.args['start_day'],
                                request.args['end_day'],
                                'history',
                                interval=request.args['interval'])
        results['data'] = data
    return jsonify(results)

@app.route('/api/v1/intraday', methods=['GET'])
def intraday():
    if 'symbol' not in request.args or \
        'start_day' not in request.args or \
        'end_day' not in request.args:
        return abort(400)

    results = {'metadata':{'symbol':request.args['symbol']}}
    if 'interval' not in request.args:
        results['metadata']['interval'] = request.args['interval']
        data = ticker.history_data(request.args['symbol'],
                                request.args['start_day'],
                                request.args['end_day'],
                                'intraday')
        results['data'] = data
    else:
        results['metadata']['interval'] = request.args['interval']
        data = ticker.get_data(request.args['symbol'],
                                request.args['start_day'],
                                request.args['end_day'],
                                'intraday',
                                interval=request.args['interval'])
        results['data'] = data
    return jsonify(results)

@app.route('/api/v2/history', methods=['GET'])
def history_v2():
    if 'symbol' not in request.args or \
        'start_day' not in request.args or \
        'end_day' not in request.args:
        return abort(400)

    results = {'metadata':{'symbol':request.args['symbol']}}
    if 'interval' not in request.args:
        results['metadata']['interval'] = request.args['interval']
        data = ticker.history_data(request.args['symbol'],
                                    request.args['start_day'],
                                    request.args['end_day'],
                                    'history',
                                    version='v2')
        results['data'] = data
    else:
        results['metadata']['interval'] = request.args['interval']
        data = ticker.get_data(request.args['symbol'],
                                request.args['start_day'],
                                request.args['end_day'],
                                'history',
                                interval=request.args['interval'],
                                version='v2')
        results['data'] = data
    return jsonify(results)

@app.route('/api/v2/intraday', methods=['GET'])
def intraday_v2():
    if 'symbol' not in request.args or \
        'start_day' not in request.args or \
        'end_day' not in request.args:
        return abort(400)

    results = {'metadata':{'symbol':request.args['symbol']}}
    if 'interval' not in request.args:
        results['metadata']['interval'] = request.args['interval']
        data = ticker.history_data(request.args['symbol'],
                                request.args['start_day'],
                                request.args['end_day'],
                                'intraday',
                                version='v2')
        results['data'] = data
    else:
        results['metadata']['interval'] = request.args['interval']
        data = ticker.get_data(request.args['symbol'],
                                request.args['start_day'],
                                request.args['end_day'],
                                'intraday',
                                interval=request.args['interval'],
                                version='v2')
        results['data'] = data
    return jsonify(results)
app.run()
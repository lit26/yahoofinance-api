import flask
from flask import request, jsonify, abort
from yafoofinanceapi.ticker import Ticker

app = flask.Flask(__name__)
app.config["DEBUG"] = True

ticker = Ticker()
@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to yafoo finance api</h1>"

@app.route('/api/v1/history', methods=['GET'])
def api_id():
    if 'symbol' not in request.args or \
        'start_day' not in request.args or \
        'end_day' not in request.args:
        return abort(400)

    results = {'metadata':{'symbol':request.args['symbol']}}
    if 'interval' not in request.args:
        results['metadata']['interval'] = request.args['interval']
        data = ticker.history_data(request.args['symbol'],
                               start_day=request.args['start_day'],
                               end_day=request.args['end_day'])
        results['data'] = data
    else:
        results['metadata']['interval'] = request.args['interval']
        data = ticker.get_data(request.args['symbol'],
                               start_day=request.args['start_day'],
                               end_day=request.args['end_day'],
                               interval=request.args['interval'])
        results['data'] = data
    return jsonify(results)
app.run()
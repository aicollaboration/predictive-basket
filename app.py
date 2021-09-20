import datetime

import pandas as pd
from flask import Flask, Response, json, jsonify, request
from flask.wrappers import Response
from flask_cors import CORS, cross_origin
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder

app = Flask(__name__)
cors = CORS(app)

API_V1 = '/api/1.0'

####


class InputValidator:
    def validate(self, input):
        return True if input else False


input_validator = InputValidator()

####


@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "status": "it works"
    })


@app.route(API_V1 + '/ping', methods=['GET'])
def ping():
    return "pong"


@app.route(API_V1 + '/info', methods=['GET'])
def info():
    return jsonify({
        'version': API_V1,
        'project': 'aicollaboration',
        'service': 'predictive-basket',
        'language': 'python',
        'type': 'api',
        'date': str(datetime.datetime.now()),
    })


@app.route(API_V1 + '/predict', methods=['POST', 'OPTIONS'])
@cross_origin(origin='localhost')
def predict():
    dataset = request.json

    if not input_validator.validate(dataset):
        return "error"

    transaction_encoder = TransactionEncoder()
    data = transaction_encoder.fit(dataset).transform(dataset)
    df = pd.DataFrame(data, columns=transaction_encoder.columns_)

    result = apriori(df, min_support=0.6, use_colnames=True)
    result['length'] = result['itemsets'].apply(lambda x: len(x))

    print(result)

    return result.to_json()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
    print('Service is running on port 5000')
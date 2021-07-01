import datetime
import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

app = Flask(__name__)
cors = CORS(app)

API_V1 = '/api/1.0'


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
        'service': 'apriori',
        'language': 'python',
        'type': 'api',
        'date': str(datetime.datetime.now()),
    })


@app.route(API_V1 + '/predict', methods=['POST', 'OPTIONS'])
@cross_origin(origin='localhost')
def predict():
    data = request.json

    dataset = [
        ['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
        ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
        ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
        ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
        ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']
    ]

    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)
    df = pd.DataFrame(te_ary, columns=te.columns_)

    result = apriori(df, min_support=0.6, use_colnames=True)
    result['length'] = result['itemsets'].apply(lambda x: len(x))

    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)

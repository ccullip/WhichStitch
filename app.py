from flask import Flask, request, jsonify, render_template, json, redirect, url_for
from flask_cors import CORS
from serve import get_model_api
from flask.json import jsonify

app = Flask(__name__)
CORS(app) # needed for cross-domain requests, allow everything by default
model_api = get_model_api()

# default route
@app.route('/')
def main():
    return render_template('simple_client.html')

# HTTP Errors handlers
@app.errorhandler(404)
def url_error(e):
    return """
    Wrong URL!
    <pre>{}</pre>""".format(e), 404

@app.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

@app.route('/output')
def output():
    print('redirected')
    return render_template('output.html')

@app.route('/error')
def error():
    print('redirected error')
    return render_template('output.html')

# API route
@app.route('/api', methods=['POST'])
def api():
    args = request.args.to_dict()
    if request.method == 'POST':
        request_data = request.get_json()
        input_data = request_data['image']
        pred1, pred2 = model_api(input_data)
        return jsonify({'pred1': pred1, 'pred2': pred2})


if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)
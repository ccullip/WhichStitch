from flask import Flask, request, jsonify, render_template, json
from flask_cors import CORS
from serve import get_model_api

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

# API route
@app.route('/api', methods=['POST'])
def api():
    try:
        input_data = request.form['image']
        output_data = model_api(input_data)
        response = jsonify(output_data)
        return json.dumps({'status':'OK?', 'response':response})
    except Exception as e:
        print(repr(e))
    return json.dumps({'status':'OK!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
from flask import Flask, request, jsonify, render_template, json
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

# API route
@app.route('/api')
def api():
    #print(request)
    args = request.args.to_dict()
    #print(args['output'])
    try:
        input_data = args['output']
        print("data:")
        output_data = model_api(input_data)
        #print(output_data)
        #response = jsonify(output_data)
        print('success')
        return jsonify({'status':'OK?'})
    except Exception as e:
        #str = repr(e)
        #print(str)
        return json.dumps({'status':'OK!'})

if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)
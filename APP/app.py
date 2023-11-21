from flask import Flask, request, jsonify
from Compiler.adapscriptyaccv2 import *
from Compiler.adapscriptlexer import tokens
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

compiler = Compiler()

@app.route('/execute', methods=['POST'])
def execute_code():
    data = request.get_json()
    code = data['code']

    result, error = compiler.execute(code)

    if error:
        return jsonify({'error': error})
    else:
        return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='10.0.2.2', port=5000, debug=True)

from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'message': 'Vulnerable API - AppSec Academy',
        'endpoints': {
            '/list': 'GET - Lists folder contents (vulnerable to command injection)',
            'usage': '/list?folder=folder_name'
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

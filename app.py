from flask import Flask, request, jsonify
import os


app = Flask(__name__)

@app.route('/list', methods=['GET'])
def list_directory():
    """
    Endpoint vulnerable to command injection.
    Receives a query param 'folder' with the folder name and lists its contents.
    VULNERABLE: Does not sanitize user input before executing system commands.
    """
    folder = request.args.get('folder', '.')
    
    result = os.popen(f'ls -la {folder}').read()
    
    return jsonify({
        'folder': folder,
        'output': result
    })

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

from flask import Flask
from flask import send_file
import os
import json
from flask import Response
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/routes/<path:file_name>')
def route_chunks(filename):

    res = {'data':os.listdir('split/{}'.format(file_name))}
    return Response(json.dumps(res),  mimetype='application/json')

@app.route('/download/<path:file_name>')
def download_complete(file_name):
    uploads = os.path.join(app.root_path, 'join',file_name)
    print(uploads)
    return send_file(uploads, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')
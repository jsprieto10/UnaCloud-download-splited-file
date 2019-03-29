from flask import Flask
from flask import send_file
import os
import json
from flask import Response
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/routes/<file_name>')
def route_chunks(file_name):

    res = {'data':os.listdir(file_name.replace('-','/'))}
    return Response(json.dumps(res),  mimetype='application/json')

@app.route('/download/<file_name>')
def download_complete(file_name):
    uploads = os.path.join(app.root_path,file_name.replace('-','/'))
    print(uploads)
    return send_file(uploads, as_attachment=True)



if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')
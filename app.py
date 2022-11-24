from flask import Flask, request

app = Flask(__name__)

@app.get('/')
def index():
    return 'Rekruto! Давай дружить!'


@app.get('/url_name')
def hello():
    name = request.args.get('name')
    message = request.args.get('message')
    return 'Hello {}! {}!'.format(name, message)
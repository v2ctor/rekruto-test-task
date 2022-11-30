from flask import Flask, request

app = Flask(__name__)

@app.get('/')
def index():
    name = request.args.get('name')
    message = request.args.get('message')
    if name and message:
        return 'Hello {}! {}!'.format(name, message)
    else:
        return 'Rekruto! Давай дружить!'
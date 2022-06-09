# Ao abrir o Gitpod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template

app = Flask(__name__)

lugares = [
    {"local": 'Fatec', "cidade": 'São José do Rio Preto', "pais": 'Brasil'},   
    {"local": 'Torre Eifel', "cidade": 'Paris', "pais": 'França'},   
]

@app.route('/')
def index():
    return render_template('index.html', lugares=lugares)

@app.route('/create')
def create():
    return render_template('create.html')

app.run(debug=True)
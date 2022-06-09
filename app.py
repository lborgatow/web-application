# Ao abrir o Gitpod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template, request
from uuid import uuid4

app = Flask(__name__)

lugares = [
    {"id": 1, "local": 'Fatec', "cidade": 'São José do Rio Preto', "pais": 'Brasil'},   
]

@app.route('/')
def index():
    return render_template('index.html', lugares=lugares)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    local = request.form['local']     # <input name="..." ...
    cidade = request.form['cidade']   # Sempre será uma string!
    pais = request.form['pais']
    lugares.append({"id": uuid4(), "local": local, "cidade": cidade, "pais": pais})
    return render_template('index.html', lugares=lugares)

def delete():
    pass

def update():
    pass

app.run(debug=True)
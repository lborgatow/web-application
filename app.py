# Ao abrir o Gitpod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template, request
from uuid import uuid4
import csv

app = Flask(__name__)

f_in = open('lugares.csv')
leitor = csv.DictReader(f_in, ['id', 'local', 'cidade', 'pais'])
lugares = [linha for linha in leitor]

@app.route('/')
def index():
    return render_template('index.html', lugares=lugares)

@app.route('/create')
def create():
    return render_template('create.html')

def save_file():
    with open('lugares.csv', 'w') as f_out:
        escritor = csv.DictWriter(f_out, ['id', 'local', 'cidade', 'pais'])
        escritor.writerows(lugares)

@app.route('/save', methods=['POST'])
def save():
    local = request.form['local']     # <input name="..." ...
    cidade = request.form['cidade']   # Sempre será uma string!
    pais = request.form['pais']
    lugares.append({"id": uuid4(), "local": local, "cidade": cidade, "pais": pais})

    save_file()

    return render_template('index.html', lugares=lugares)

@app.route('/delete/<id>')
def delete(id):     
    for lugar in lugares:
        if lugar['id'] == id:
            lugares.remove(lugar)

    save_file()

    return render_template('index.html', lugares=lugares)

def update():
    pass

app.run(debug=True)
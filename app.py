# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template, request, redirect
from uuid import uuid4
import csv

app = Flask(__name__)


lugares = []

with open('lugares.csv', 'r') as file_in:
    leitor = csv.DictReader(file_in)
    for lugar in leitor:
        lugares.append(dict(lugar))


def save_file():
    with open('lugares.csv', 'w') as file_out:
        escritor = csv.DictWriter(file_out, ['id', 'Local', 'Cidade', 'País'])
        escritor.writeheader()
        escritor.writerows(lugares)

@app.route('/')
def index():
    save_file()
    return render_template('index.html', lugares=lugares) 

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    local = request.form['Local']
    cidade = request.form['Cidade']
    pais = request.form['País']
   
    lugares.append({'id': uuid4(), 'Local': local, 'Cidade': cidade, 'País': pais})
    
    return redirect('/')

@app.route('/edit/<id>')
def edit(id):
    for lugar in lugares:
        id_string = str(lugar['id'])
        if id_string == id: 
            return render_template('edit.html', lugar=lugar)

@app.route('/update/<id>', methods=['POST'])
def update(id):
    for lugar in lugares:
        id_string = str(lugar['id'])
        if id_string == id:
            lugar['Local'] = request.form['Local']
            lugar['Cidade'] = request.form['Cidade']
            lugar['País'] = request.form['País']
    
    return redirect('/')

@app.route('/delete/<id>')
def delete(id):
    for lugar in lugares:
        id_string = str(lugar['id'])
        if id_string == id:
            del lugares[lugares.index(lugar)]
            return render_template('deleted.html')


app.run(debug=True)
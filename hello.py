from flask import Flask
app =Flask(__name__)

#decorador
@app.route('/')
def funcion_principal():
    return 'Hola, mundo'

@app.route('/adios')
def bye():
    return 'Adios, mundo cruel'
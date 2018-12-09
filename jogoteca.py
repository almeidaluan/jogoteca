from flask import Flask,render_template

app = Flask(__name__)

@app.route("/inicio")
def hello():
    return render_template('lista.html',titulo='Lista de Jogos')

app.run() #host='0.0.0.0',port=8080

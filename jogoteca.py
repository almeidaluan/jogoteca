from flask import Flask,render_template

app = Flask(__name__)

@app.route("/inicio")
def hello():
    lista_jogos = ['Mortal Combat','Mario Cart','Top Gear']
    return render_template('lista.html',titulo='Lista de Jogos',jogos=lista_jogos)

app.run(port=8080) #host='0.0.0.0',port=8080

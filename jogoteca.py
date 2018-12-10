from flask import Flask,render_template

app = Flask(__name__)

class Jogo:
    def __init__(self,nome,categoria,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


@app.route("/inicio")
def hello():
    jogo01 = Jogo('Super Mario','Acao','SNES')
    jogo02 = Jogo('Pokemon Gold','RPG','GBA')
    lista_jogos = [jogo01,jogo02]
    return render_template('lista.html',titulo='Lista de Jogos',jogos=lista_jogos)

app.run(port=8081) #host='0.0.0.0',port=8080

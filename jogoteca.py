from flask import Flask,render_template,request,redirect

app = Flask(__name__)


class Jogo:
    def __init__(self,nome,categoria,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

#Lista global que ja vem com 2 jogos por default
jogo01 = Jogo('Super Mario','Acao','SNES')
jogo02 = Jogo('Pokemon Gold','RPG','GBA')
lista = [jogo01,jogo02]

@app.route("/")
def listaJogos():
    jogo01 = Jogo('Super Mario','Acao','SNES')
    jogo02 = Jogo('Pokemon Gold','RPG','GBA')
    lista_jogos = [jogo01,jogo02]
    return render_template('lista.html',titulo='Lista de Jogos',jogos=lista_jogos)

@app.route("/novo")
def novoJogo():
    return render_template('novo.html',titulo="Novo Jogo")

@app.route("/criar",methods=['POST',])
def criarJogo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista.append(jogo)
    return redirect('/')

app.run(port=8081) #host='0.0.0.0',port=8080

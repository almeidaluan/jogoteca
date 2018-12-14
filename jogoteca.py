from flask import Flask,render_template,request,redirect,session,flash

app = Flask(__name__)
app.secret_key = 'caelum'

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
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima-page=novo')
    return render_template('novo.html',titulo="Novo Jogo")

@app.route("/criar",methods=['POST',])
def criarJogo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista.append(jogo)
    return redirect('/')

@app.route("/login")
def login():
    proxima = request.args.get('proxima-page')
    return render_template('login.html', proxima=proxima)

@app.route("/autenticar",methods=['POST',])
def autenticar():
    if 'mestra' == request.form['senha']:
         session['usuario_logado'] = request.form['usuario']
         flash(request.form['usuario'] + 'logado com sucesso')
         proxima_page = request.form['proxima']
         return redirect("/{}".format(proxima_page))
    else:
         flash('Nao foi possivel se logar no sistema,tente novamente ou aguarde alguns minutos')
         return redirect("/login")


@app.route('/logout')
def deslogar():
    session['usuario_logado'] = None
    flash('Usuario Deslogado')
    return redirect('/')

app.run(port=8081) #host='0.0.0.0',port=8080

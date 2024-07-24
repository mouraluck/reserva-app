from Flask import flask, render_template, request

app = Flask (__name__)

#define dicionario de logins
login_dict = [

]

def pegar_login_armazenado():
    #sldaps
    print('pegando dados')
    #login_dict.append(exemplo)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/',methods=['post'])
def home():
    return render_template('reservas.html')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


#pega os dados do método post no html do template
@app.route('/cadastro', methods=['post'])
def cadastro():
    nome = request.form['nome'] 
    email = request.form['email']
    senha = request.form['senha']
    cad = {
        'nome':nome ,
        'email':email,
        'senha':senha
    }
    login_dict.append(cad)
    return render_template(cad)

@app.route('/cadastrar-sala')
def cadastrar_sala(): 
    return render_template('cadastrar-sala.html')

@app.route('/reservas')
def reservas():
    return render_template('reservas.html')

@app.route('/reservar-sala')
def reservar_sala():
    return render_template('reservar-sala.html')

@app.route('/listar-salas')
def listar_salas():
    return render_template('listar-salas.html')
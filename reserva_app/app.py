from flask import Flask, render_template, request

app = Flask(__name__)

# Define dicionário de logins
login_dict = []


def pegar_login_armazenado():
    # sldaps
    print('Pegando dados')
    # login_dict.append(exemplo)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/reservas', methods=['POST'])
def reservas():
    return render_template('reservas.html')

# @app.route('/cadastro')
# def cadastro():
#     return render_template('cadastro.html')

# Pega os dados do método POST no HTML do template
@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form['nome'] 
    email = request.form['email']
    senha = request.form['senha']
    cad = {
        'nome': nome,
        'email': email,
        'senha': senha
    }
    login_dict.append(cad)
    return render_template('cadastro.html', cad=cad)  # Passa 'cad' para o template

@app.route('/cadastrar-sala')
def cadastrar_sala(): 
    return render_template('cadastrar-sala.html')

@app.route('/reservar-sala')
def reservar_sala():
    return render_template('reservar-sala.html')

@app.route('/listar-salas')
def listar_salas():
    return render_template('listar-salas.html')

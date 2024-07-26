from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Define dicionário de logins
login_dict = []


def pegar_login_armazpopenado():
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
#         return render_template('cadastro.html')

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


@app.route('/cadastrar-sala', methods=['GET', 'POST'])
def cadastrar_sala():
    if request.method == 'POST':  # se o forms for enviado
        # Obter dados do formulário
        tipo = request.form['tipo']
        capacidade = request.form['capacidade']
        descricao = request.form['descricao']
        
        # Salvar a sala no arquivo CSV
        with open('salas.csv', 'a', newline='') as arquivo_salas:
            writer = csv.writer(arquivo_salas)
            writer.writerow([tipo, capacidade, descricao])
        
        # Redirecionar para a lista de salas após o cadastro
        return render_template('listar-sala')
    
    # Se o método for GET, exibir o formulário
    return render_template('cadastrar-sala.html')



@app.route('/reservar-sala')
def reservar_sala():
    return render_template('reservar-sala.html')

@app.route('/listar-salas')
def listar_salas():
    return render_template('listar-salas.html')


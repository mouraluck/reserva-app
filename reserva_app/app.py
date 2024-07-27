from flask import Flask, render_template, request, redirect, url_for 
import csv

#passando .csv para acessivel á python
cadastro_csv = 'cad_usuarios.csv'

app = Flask(__name__)

# Define dicionário de logins
login_dict = []

# pagina inicial
@app.route('/')
def login():
    return render_template('login.html')

# pagina de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        salvar_cadastro(nome, email, senha)
        cad = {
            'nome': nome,
            'email': email,
            'senha': senha
        }
        # Adiciona o login ao dicionário de logins
        login_dict.append(cad)
        return redirect(url_for('reservas'))
    return render_template('cadastro.html')

# salvar dados digitados pelo usuario no csv
def salvar_cadastro(nome, email, senha):
    with open(cadastro_csv, 'a', newline='') as arquivo_cadastros:
        writer = csv.writer(arquivo_cadastros)
        writer.writerow([nome, email, senha])
        #verificando função 
        print(f"dados salvos: {nome}, {email},{senha}")


@app.route('/', methods=['POST'])
# Função para verificar se o usuário está registrado no CSV
def logar(email, senha):
    try: 
        with open (cadastro_csv, 'r') as arquivo_cadastros:
            leitor_csv = csv.reader(arquivo_cadastros)
            for linha in leitor_csv:
                # linha 1 - email || linha 2
                if linha[1] == email and linha[2] == senha:
                    return redirect(url_for('reservas'))

    except FileNotFoundError:
        return render_template('login.html', error='Email ou senha incorretos.')

@app.route('/cadastrar-sala', methods=['GET', 'POST'])
def cadastrar_sala():
    if request.method == 'POST':
        tipo = request.form['tipo']
        capacidade = request.form['capacidade']
        descricao = request.form['descricao']
        
        # Salvar a sala no arquivo CSV
        with open('salas.csv', 'a', newline='') as arquivo_salas:
            writer = csv.writer(arquivo_salas)
            writer.writerow([tipo, capacidade, descricao])
        
        # Redirecionar para a lista de salas após o cadastro
        return redirect(url_for('listar_salas'))
    
    return render_template('cadastrar-sala.html')


# VER QUAL DAS DUAS RESERVAS ESTÃO FUNCIONANDO E SENDO UTEIS
@app.route('/reservas', methods=['GET', 'POST'])
def reservas():
    return render_template('reservas.html')

@app.route('/reservas')
def salas_reservadas ():
    return render_template('reservas.html')

# verificar se salas estao reservadas
@app.route('/reservar-sala')
def reservar_sala():
    return render_template('reservar-sala.html')

# listar salas reservadas
@app.route('/listar-salas')
def listar_salas():
    return render_template('listar-salas.html')

if __name__ == '__main__':
    app.run(debug=True)

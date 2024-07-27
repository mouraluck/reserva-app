from flask import Flask, render_template, request, redirect, url_for 
import csv

#passando .csv para acessivel á python
cadastro_csv = 'cad_usuarios.csv'
cadastro_sala_csv = 'cad_sala.csv'

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

# logica de cadastrar sala no csv sendo construida
@app.route('/cadastrar-sala', methods=['GET', 'POST'])
def cadastrar_sala(nome, email, senha):
    with open(cadastro_csv, 'a', newline='') as arquivo_salas:
        writer = csv.writer(arquivo_salas)
        writer.writerow([tipo, capacidade, descricao])
        #verificando função 
        print(f"dados salvos: {tipo}, {capacidade},{descricao}")


# VER QUAL DAS DUAS RESERVAS ESTÃO FUNCIONANDO E SENDO UTEIS
@app.route('/reservas', methods=['GET', 'POST'])
def reservas():
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

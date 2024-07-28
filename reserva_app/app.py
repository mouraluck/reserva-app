from flask import Flask, render_template, request, redirect, url_for 
import csv

#passando .csv para acessivel á python
cadastro_csv = 'cad_usuarios.csv'
cadastro_sala_csv = 'cad_sala.csv'

app = Flask(__name__)

# FUNÇÕES

# salvar dados digitados pelo usuario no csv
def salvar_cadastro(nome, email, senha):
    with open(cadastro_csv, 'a', newline='') as arquivo_cadastros:
        writer = csv.writer(arquivo_cadastros)
        writer.writerow([nome, email, senha])
        #verificando função 
        print(f"dados salvos: {nome}, {email},{senha}")


# pagina de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        salvar_cadastro(nome, email, senha)
        return redirect(url_for('reservas'))
    return render_template('cadastro.html')

# salvar sala digitada pelo usuario no csv 
def salvar_sala(tipo, capacidade, descricao):
    with open(cadastro_sala_csv, 'a', newline = '') as salas_cadastros:
        writer = csv.writer(salas_cadastros)
        writer.writerow([tipo, capacidade, descricao])

        print(f"dados salvos: {tipo}, {capacidade}, {descricao}")


@app.route('/detalhe', methods=['GET', 'POST'])
def detalhe_sala():
    if request.method == 'POST':
        tipo = request.form['tipo']
        capacidade = request.form['capacidade'] 
        descricao = request.form['descricao']
        salvar_sala(tipo, capacidade, descricao)
        #nao sei oq to fazendo
        return redirect(url_for('descricao-sala'))
    return render_template ()





@app.route('/descricao-sala', methods = ['GET', 'POST'])

# 
@app.route('/detalhe-reserva', methods = ['GET', 'POST'])

#verificação de login
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


# ROTAS "VAZIAS"
@app.route('/cadastrar-sala', methods=['GET', 'POST'])


# pagina inicial
@app.route('/')
def login():
    return render_template('login.html')


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
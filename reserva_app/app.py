from flask import Flask, render_template, request, redirect, url_for 
import csv

#csv acessivel a python
cadastro_csv = 'cad_usuarios.csv'
cadastro_sala_csv = 'cad_sala.csv'

app = Flask(__name__)


# salvar dados digitados pelo usuario no csv
def salvar_cadastro(nome, email, senha):
    with open(cadastro_csv, 'a', newline='') as arquivo_cadastros:
        writer = csv.writer(arquivo_cadastros)
        writer.writerow([nome, email, senha])
        #verificando função 
        print(f"dados salvos: {nome}, {email},{senha}")


# rota /cadastro
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_post():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        salvar_cadastro(nome, email, senha)
        return render_template('reservas.html')


@app.route('/logar', methods=['GET','POST'])
# Função para verificar se o usuário está registrado no CSV
def logar():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form ['senha']

        with open (cadastro_csv, mode ='r') as arquivo_cadastros:
            leitor = csv.leitor(arquivo_cadastros)

            for linha in leitor:
                if linha['email'] == email and linha['senha'] == senha:
                    return redirect(url_for('sucess'))
            return "invalido", 401
    return render_template('cadastrar-sala.html')


@app.route('/sucess')
def sucess():
    return "LOGIN DEU CERTO!!!!"

# salvar sala digitada pelo usuario no csv 
def salvar_sala(tipo, capacidade, descricao):
    with open(cadastro_sala_csv, 'a', newline = '') as salas_cadastros:
        writer = csv.writer(salas_cadastros)
        writer.writerow([tipo, capacidade, descricao])

        print(f"dados salvos: {tipo}, {capacidade}, {descricao}")

# ta errado, detalhe da reserva mostra os dados da sala reservada, horario inicial, final,
@app.route('/detalhe-reserva', methods=['GET', 'POST'])
def detalhe_sala():
    if request.method == 'POST':
        tipo = request.form['tipo']
        capacidade = request.form['capacidade'] 
        descricao = request.form['descricao']
        
        if tipo == '' or capacidade == '' or descricao == '':
            return render_template ('cadastrar-sala.html')
        salvar_sala(tipo, capacidade, descricao)
        return render_template('listar-sala.html')



@app.route('/descricao-sala', methods = ['GET', 'POST'])


#botao de logout vai pra rota /login  mas nao vai pra nenhum lugar essa rota

# pagina inicial
#@app.route('/')
#def login():
#    return render_template('login.html')

#verificação de login

# ROTAS "VAZIAS"
@app.route('/cadastrar-sala', methods=['GET', 'POST'])

@app.route('/cadastrar-sala')
def cadastrar_sala():
    return render_template('cadastrar-sala.html')





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
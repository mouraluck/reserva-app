from flask import Flask, render_template, request, redirect, url_for 
import csv

#csv acessivel a python
users = 'cad_usuarios.csv'
cadastro_sala_csv = 'cad_sala.csv'
reserva_csv = 'res_sala.csv'  



app = Flask(__name__)

salas_dic = []


# salvar dados digitados pelo usuario no csv ✔️
def salvar_cadastro(nome, email, senha):
    with open(users, 'a', newline='') as arquivo_cadastros:
        writer = csv.writer(arquivo_cadastros)
        writer.writerow([nome, email, senha])
        #verificando função 
        print(f"dados salvos: {nome}, {email},{senha}")


# rota /cadastro ✔️
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


# salvar sala digitada pelo usuario no csv ✔️
def salvar_sala(tipo, capacidade, descricao):
    with open(cadastro_sala_csv, 'a', newline = '') as salas_cadastros:
        writer = csv.writer(salas_cadastros)
        writer.writerow([tipo, capacidade, descricao])
        print(f"dados salvos: {tipo}, {capacidade}, {descricao}")

# ta dando certo ✔️, mas tem problema da rota
# detalhe da reserva mostra os dados da sala reservada, horario inicial, final,
@app.route('/detalhe-reserva', methods=['POST'])
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


@app.route('/cadastrar-sala', methods=['GET', 'POST'])
def cadastrar_sala():
    return render_template('cadastrar-sala.html')


# verificar se salas estao reservadas
@app.route('/reservar-sala')
def reservar_sala():
    return render_template('reservar-sala.html')

#salva a reserva no csv
def salvar_reserva(sala, inicio, fim):
    with open(reserva_csv, 'a', newline='') as arquivo_reservas:
        writer = csv.writer(arquivo_reservas)
        writer.writerow([sala, inicio, fim])
        print(f"Reserva salva: Sala {sala}, Início {inicio}, Fim {fim}")

#mostra os detalhes da reserva
@app.route('/detalhe-reserva', methods=['GET', 'POST'])
def detalhe_reserva():
    if request.method == 'POST':
        sala = request.form['sala']
        inicio = request.form['inicial']
        fim = request.form['final']
        
        if sala == '' or inicio == '' or fim == '':
            return render_template('reservar-sala.html', error="Por favor, preencha todos os campos.")
        
        salvar_reserva(sala, inicio, fim)
        return render_template('detalhe-reserva.html') 
    


@app.route('/reservas', methods=['GET', 'POST'])
def reservas():
    return render_template('reservas.html')




# listar salas 
@app.route('/listar-salas')
def listar_salas():
    with open(cadastro_sala_csv, 'r') as arquivo_salas:
        salas_dic = [] 
        count = 0
        next(arquivo_salas)
        for linha in arquivo_salas: 
            
            tipo = ''
            count= count+1
            if linha[0] == '1':
                tipo = 'Sala 1'
            elif linha[0] == '2':
                tipo = 'Sala 2'
            elif linha[0] == '3':
                tipo = 'Sala 3'
            # Cria um novo dicionário para cada item da linha
            sala = {
                'count': count,
                'tipo': tipo,
                'capacidade': linha[1],
                'descricao': linha[2]
            }
            
            salas_dic.append(sala)  # Adiciona o novo dicionário à lista
            

    return render_template('listar-salas.html', salas=salas_dic)


#  PARA FAZER:

# criar rota / e pegar codigo do latorre e deixar igual✔️
# desabilitar botão de logout - dá erro✔️
# no html de cadastrar sala: jogar mensagem "preencha todos os campos" ao inves de recarregar a pagina 
# terminar a rota que salva as reservas no csv

# ROTAS:

# / - não está referenciando nada (tem que referenciar a tela de login, mesmo que nao tenha login)❌
# /cadastro - ✔️
# /logar - rota comentada, não deu certo ✔️ 
# /sucess - rota comentada, era caso o login desse certo ❌
# /detalhe-reserva - erro ❌
# /descricao-sala - não faz sentido, vai para Cadastrar sala (html) ❌
# /cadastrar-sala - vai para Cadastrar sala (html) ✔️
# /reservas - indo para reservas ✔️ (não precisa implementar)
# /reservar-sala - indo para reservar sala ✔️ salvando no csv ❌
# /listar-salas - indo para listagem das salas ✔️ conectada ao csv a partir da reserva ❌
# /login - botao de logout vai pra essa rota mas a rota não existe ✔️


# NÃO ESTÁ DANDO CERTO, VOU COMENTAR:

@app.route('/', methods=['POST'])
def logar():
    valid = False
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        

        with open(users, 'r', newline='' ) as arquivo_cadastros:
            leitor = csv.DictReader(arquivo_cadastros, fieldnames=['email', 'senha']) 

            for linha in leitor:  # leitor já retorna um dicionário em cada iteração
                if linha['email'] == email and linha['senha'] == senha:
                    print(leitor.reader['email', 'senha'])  # Imprime o email encontrado (opcional)
                    valid = True
    if valid==True:
        return render_template('sucess.html')
    else:
        return render_template('login.html')




#teste se Login deu certo:
@app.route('/sucess')
def sucess():
   return render_template('sucess.html')


#pagina inicial
@app.route('/')
def login():
   return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
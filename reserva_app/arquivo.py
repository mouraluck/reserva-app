import csv

def salvar_sala(tipo, capacidade, descricao):
    with open('salas.csv', 'a', newline='') as arquivo_salas:
        writer = csv.writer(arquivo_salas)
        writer.writerow([tipo, capacidade, descricao])

def obter_salas():
    salas = []
    with open('salas.csv', 'r') as arquivo_salas:
        reader = csv.reader(arquivo_salas)
        for row in reader:
            sala = {
                'tipo': row[0],
                'capacidade': row[1],
                'descricao': row[2]
            }
            salas.append(sala)
    return salas
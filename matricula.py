class Matricula():
    def __init__(self,nome,cpf,endereco,idade,nome_da_mae,nome_do_pai):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.idade = idade
        self.nome_da_mae = nome_da_mae
        self.nome_do_pai = nome_do_pai

    def matricular():
        alunos = {}
        nome = str(input('Informe seu nome: '))
        alunos['nome'] = nome
        cpf = str(input('Informe seu CPF: '))
        alunos['cpf'] = cpf
        idade = int(input('Informe sua idade: '))
        alunos['idade'] =idade
        endereco = str(input('Informe seu endereço completo: '))
        alunos['endereço']= endereco
        nomeM = str(input('Informe o nome da mãe: '))
        alunos['Nome da mãe'] = nomeM
        nomeP = str(input('Informe o nome do seu pai: '))
        alunos['Nome do pai'] = nomeP

        return alunos

a = Matricula.matricular()
for dados,valores in a.items():
    print(f'{dados}: {valores}')
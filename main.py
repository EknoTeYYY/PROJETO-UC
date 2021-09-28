#importar (all)
senha_adm = 28092021
senha_alunos = 123456789
ask = int(input('Voce é aluno ou administrador ? \n1. ADM \n2. ALUNOS \n'))
if ask == 1:
    senha = int(input('Informe sua senha: '))
    if senha == senha_adm:
        print('acertou mizeravi')
    else:
        print('SENHA INVALIDA!')
elif ask == 2:
    senha = int(input('Informe sua senha: '))
    if senha == senha_alunos:
        print('acertou mizeravi')
    else:
        print('SENHA INVALIDA!')
else:
        print('OPÇÃO INVALIDA')

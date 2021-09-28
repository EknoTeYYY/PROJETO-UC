import datetime
class Desempenho():
    def __init__ (self,media,presenca):
        self.media = media
        self.presenca = presenca

    def calcular():
        aluno = str(input('Informe o nome do aluno: '))
        turma =str(input('Informe o número da turma desse aluno: '))

        n1 = float (input("Informe a prova 1: "))
        if n1 < 6:
            rn1 = float (input("Informe a recuperação da prova 1: "))
            if rn1 > n1:
                n1 = rn1
        n2 = float (input("Informe a prova 2: "))
        if n2 < 6:
            rn2 = float (input("Informe a recuperação da prova 2: "))
            if rn2 > n2:
                    n2 = rn2
        n3 = float (input("Informe a prova 3: "))
        if n3 < 6:
            rn3 = float (input("Informe a recuperação da prova 3: "))
            if rn3 > n3:
                    n3 = rn3
        t1 = float (input("Informe a nota do trabalho 1: "))
        t2 = float (input("Informe a nota do trabalho 2: "))
        t3 = float (input("Informe a nota do trabalho 3: "))

        retorno = int(input('Deseja confirmar ? \n1.SIM \n2.NÃO \n'))
        if retorno == 1:
            pass
        else:
             return Desempenho.calcular()

        media = (n1 + n2 + n3 + ((t1 + t2 + t3) /3) )/4

        if media >= 9:
            print('Conceito A')
            print(aluno ,turma,'Aprovado')
        elif media >= 7.5 and media < 9:
            print('Conceito B')
            print(aluno ,turma,'Aprovado')
        elif media >= 6.0 and media < 7.5:
            print('Conceito C')
            print(aluno ,turma,'Aprovado')
        elif media >= 4.0 and media < 6.0:
            print('Conceito D')
            print(aluno ,turma,'Reprovado')
        elif media < 4.0:
            print('Conceito E')
            print(aluno ,turma,'Reprovado')
        
        return media
        
    def presenca():
            dia =(datetime.date.today().day,datetime.date.today().month,datetime.date.today().year)
            chamada = 0
            pres = int(input('Aluno presente ? \n1.SIM \n2.NÃO \n'))
            if pres ==1:
                chamada += 1
            else:
                pass
            
            return chamada

a = Desempenho.calcular()
print(a)
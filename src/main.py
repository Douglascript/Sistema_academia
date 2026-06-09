#Sistema para gerenciamento de alunos de uma academia
from uteis import alunos, interacao
from time import sleep

while True:
    interacao.titulo('Sistema de Alunos')
    escolha = interacao.menu()
    if escolha == 1:
        nome = input('Nome do aluno(a): ')
        idade = int(input(f'Idade do(a) {nome}: '))
        peso = float(input('Peso atual: '))
        altura = float(input('Altura atual: '))
        alunos.cadastrar(nome, idade, peso, altura)
        sleep(3)
        continue
    elif escolha == 2:
        alunos.listar()
        sleep(3)
        continue
    elif escolha == 3:
        nome = input('Nome do aluno que deseja procurar: ')
        alunos.busca(nome)
        sleep(3)
        continue
    elif escolha == 4:
        nome = input('Quem deve ser deletado?: ')
        alunos.remover(nome)
        sleep(3)
        continue
    elif escolha == 5:
        alunos.sair()
        break
    else:
        continue
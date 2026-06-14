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
    elif escolha == 6:
        print('-' * 60)
        peso = float(input('Informe o peso em kg: '))
        altura = float(input('Informe a altura da pessoa: '))
        m = alunos.imc(peso, altura)
        if m < 18.5:
            print(f'O IMC dessa pessoa é {m:.2f}, está abaixo do peso. ')
        elif m >= 18.5 and m < 25.0:
            print(f'O IMC dessa pessoa é {m:.2f}, está normal. ')
        elif m >= 25.0 and m < 30:
            print(f'O IMC dessa pessoa é {m:.2f}, está no sobrepeso. ')
        elif m >= 30.0 and m < 35.0:
            print(f'O IMC dessa pessoa é {m:.2f}, Obesidade de grau I. ')
        elif m >= 35.0 and m < 40:
            print(f'O IMC dessa pessoa é {m:.2f}, Obesidade de grau II. ')
        else:
            print(f'O IMC dessa pessoa é {m:.2f}, Obesidade de grau III. ')
        t = input('Aperte qualquer tecla para continuar...')
    elif escolha == 7:
        print('-' * 60)
        lista = alunos.atualizar()
        for aluno in lista:
            for chave, valor in aluno.items():
                print(f'{chave}: {valor} ', end='')
            print('')
        print('')

        nome = input('Aluno desejado: ').strip().lower()
        for aluno in lista:
            if aluno['nome'].lower() == nome:
                while True:
                    dado = input('Dado que será atualizado ex:(idade): ').strip().lower()
                    if dado == 'nome':
                        novo_n = input('Novo nome: ').strip().lower()
                        aluno['nome'] = novo_n
                        break
                    elif dado == 'idade':
                        nova_i = input('Nova idade: ').strip().lower()
                        aluno['idade'] = nova_i
                        break
                    elif dado == 'peso':
                        novo_p = input('Novo peso: ').strip().lower()
                        aluno['peso'] = novo_p
                        break
                    elif dado == 'altura':
                        nova_a = input('Novo altura: ').strip().lower()
                        aluno['altura'] = nova_a
                        break
                    else:
                        print('\n!Opção inválida!\n')
                        continue
        alunos.salvar(lista)
        r = input('Pronto! Aperte qualquer tecla para continuar...')
    elif escolha == 8:
        print('')
        print(alunos.estatistica())
        print('')
        sleep(2)
        r = input('Pronto! Aperte qualquer tecla para continuar...')
    else:
        continue
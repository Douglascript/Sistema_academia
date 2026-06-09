def cadastrar(nome = '', idade = 0, peso = 0.0, altura = 0.0):
    '''Função que recebe atributos de uma pessoa e escreve em um arquivo txt'''
    import os

    print('-'*60)
    print(f'{"Cadastro de Alunos".center(60)}')
    print('-'*60)
    arquivo = open('controle.txt', 'a')
    arquivo.write(f'Nome: {nome}, idade: {idade}, peso: {peso} e altura: {altura}\n')
    arquivo.close
    print(f'ALUNO REGISTRADO > Nome: {nome}, idade: {idade}, peso: {peso} e altura: {altura}\n')

def listar():
    print('-'*60)
    print(f'{"Lista de Alunos".center(60)}')
    print('-'*60)
    arquivo = open('controle.txt', 'r')
    alunos = arquivo.readlines()
    arquivo.close()
    for aluno in alunos:
        print(aluno.strip())

def buscar(nome = ''):
    arquivo = open('controle.txt', 'r')
    conteudo = arquivo.readlines()
    arquivo.close()
    for aluno in conteudo:
        if f"Nome: {nome}" in aluno:
            print(f'Aluno encontrado: {aluno}')

def busca(nome = ''):
    arquivo = open('controle.txt', 'r')
    alunos = arquivo.readlines()
    arquivo.close()
    for aluno in alunos:
        dado = aluno.split(',')
        if dado[0].lower() == f'nome: {nome}'.lower():
            print(f'Aluno encontrado: {aluno}')

def remover(nome = ''):
    arquivo = open('controle.txt', 'r')
    alunos = arquivo.readlines()
    arquivo.close()

    arquivo = open('controle.txt', 'w')
    for aluno in alunos:
        if nome.lower() not in aluno.lower():
            arquivo.write(aluno)
    arquivo.close()
    print('Apagado com sucesso.')

def sair():
    from time import sleep
    
    print('Saindo', end='')
    for _ in range(3):
        print('.', end='', flush=True)
        sleep(1)
def cadastrar(nome = '', idade = 0, peso = 0.0, altura = 0.0):
    '''Função que recebe atributos de uma pessoa e escreve em um arquivo txt'''
    import os

    print('-'*60)
    print(f'{"Cadastro de Alunos".center(60)}')
    print('-'*60)
    arquivo = open('controle.txt', 'a')
    arquivo.write(f'nome: {nome}, idade: {idade}, peso: {peso}, altura: {altura}\n')
    arquivo.close()
    print(f'ALUNO REGISTRADO > Nome: {nome}, idade: {idade}, peso: {peso}, altura: {altura}\n')

def listar():
    '''Função que lista linhas de um arquivo txt'''
    print('-'*60)
    print(f'{"Lista de Alunos".center(60)}')
    print('-'*60)
    arquivo = open('controle.txt', 'r')
    alunos = arquivo.readlines()
    arquivo.close()
    for aluno in alunos:
        print(aluno.strip())

def buscar(nome = ''):
    '''Função que recebe um nome e diz se existe no arquivo txt'''
    arquivo = open('controle.txt', 'r')
    conteudo = arquivo.readlines()
    arquivo.close()
    for aluno in conteudo:
        if f"Nome: {nome}" in aluno:
            print(f'Aluno encontrado: {aluno}')

def busca(nome = ''):
    '''Função que recebe um nome e diz se existe no arquivo txt V2'''
    arquivo = open('controle.txt', 'r')
    alunos = arquivo.readlines()
    arquivo.close()
    for aluno in alunos:
        dado = aluno.split(',')
        if dado[0].lower() == f'nome: {nome}'.lower():
            print(f'Aluno encontrado: {aluno}')

def remover(nome = ''):
    '''Função que recebe um nome e apaga a linha aonde ele se encontra'''
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
    '''Função para encerramento de menu'''
    from time import sleep
    
    print('Saindo', end='')
    for _ in range(3):
        print('.', end='', flush=True)
        sleep(1)

def imc(peso = 0, altura = 0):
    '''Função que recebe o peso e altura de uma pessoa e retorna o IMC'''
    imc = peso / (altura * altura)
    return imc

def atualizar():
    '''Função que devolve uma lista de dicionários para cada item no arquivo txt  '''
    alunos = []
    arquivo = open('controle.txt', 'r')
    conteudo = arquivo.readlines()
    arquivo.close()

    for linha in conteudo:
        dados = {}

        campos = linha.strip().split(',')
        for campo in campos:
            chave, valor = campo.split(':')
            dados[chave.strip()] = valor.strip()

        alunos.append(dados)
    
    return alunos

def salvar(lista):
    '''Recebe uma lista de dicionários e atualiza o arquivo TXT'''
    
    with open('controle.txt', 'w') as arquivo:
        for aluno in lista:
            arquivo.write(
                f"nome: {aluno['nome']}, "
                f"idade: {aluno['idade']}, "
                f"peso: {aluno['peso']}, "
                f"altura: {aluno['altura']}\n"
            )


def estatistica():
    ''' '''
    lista = atualizar()

    total_alunos = len(lista)

    pesos = []
    imcs = []

    for aluno in lista:
        peso = float(aluno['peso'])
        altura = float(aluno['altura'])

        pesos.append(peso)
        imcs.append(peso / (altura ** 2))

    imc_medio = sum(imcs) / len(imcs)
    maior_peso = max(pesos)
    menor_peso = min(pesos)

    return (
        f'Total de alunos: {total_alunos}\n'
        f'IMC médio: {imc_medio:.1f}\n'
        f'Maior peso: {maior_peso:.1f}kg\n'
        f'Menor peso: {menor_peso:.1f}kg'
    )
    print()
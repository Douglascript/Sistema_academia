def titulo(txt = ''):
    '''Função que recebe uma string e já exibe um título formatado com a string'''
    print('-' * 60)
    print(txt.center(60))
    print('-' * 60)

def menu():
    '''Função para exibir um Menu'''
    print('[1] - Cadastrar aluno\n[2] - Listar alunos\n[3] - Buscar aluno\n[4] - Remover aluno\n[5] - Sair\n[6] - Calcular IMC\n[7] - Atualizar Aluno\n[8] - Mostrar Estatísticas')
    n = int(input('Sua opção: '))
    return n
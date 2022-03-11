import shutil

def escrever_arquivo(texto):
    arquivo = open('C:/local/local2/teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'x')
    aluno_nota = arquivo.read()
    print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    for x in aluno_nota:
        lista_notas = x.split(',')
        print(lista_notas)
        aluno = lista_notas[0]
        print(aluno)  # imprimir todos os nomes dos alunos
        media = lambda notas: sum([int(i) for i in notas]) / 4  # vai passar nos strings e converter pra int

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Local/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Local/')

if __name__ == '__main__':
    copia_arquivo('notas.txt')
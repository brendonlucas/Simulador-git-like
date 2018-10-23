from modelos import *
from serviso import *


def main():
    git_controle = ControleGit()
    repo_atual = False
    while True:
        menu = "☆☆ COMANDOS GIT ☆☆ \n\
        1 - Criar Repositorio: \n\
        2 - selecionar Repositorio: \n\
        3 - Criar arquivo: \n\
        4 - Remover arquivo: \n\
        5 - Editar arquivo: \n\
        6 - Adiconar arquivo ao HEAD: \n\
        7 - Commit <Mensagem>: \n\
        8 - Enviar todos os commits: \n\
        9 - Carregar arquivos do repositorio remoto: \n\
        10 - Git status \n\
        11 - Git log \n\
        ->"

        comando = int(input(menu))

        if comando == 1:
            nome_repositorio = input("Digite o nome do repositorio que deseja criar:")
            git_controle.criar_repositorio(nome_repositorio)

        if comando == 2:
            repo_solicitado = input("Escolha um repositorio: -> ")
            repo_atual = git_controle.seleciona_repositorio(repo_solicitado)
        if repo_atual != False:
            if comando == 3:
                nome_arquivo = input("Digite o nome do arquivo: -> ")
                git_controle.criar_arquivo(nome_arquivo, repo_atual)

        if comando == 4:
            nome_arquivo = input("Digite o arquivo para apagar: -> ")
            git_controle.remover_arquivo(nome_arquivo, repo_atual)

        if comando == 5:
            tipo = int(input("Deseja sobrescrever ou apenas adiconar (1- sobrescrever/ 2 - adicionar -> )"))
            nome_arquivo = input("Digite o nome do arquivo -> ")
            texto = input()
            git_controle.editar_arquivo(nome_arquivo, repo_atual, texto, tipo)

        if comando == 6:
            nome = input("Digite o nome do arquivo ->")
            git_controle.add(repo_atual, nome)

        if repo_atual != False:
            if comando == 7:
                git_status = git_controle.retorna_stage_area()
                monitorados = git_status
                for i in range(len(monitorados)):
                    comentario = input("mensagem -> ")
                    git_controle.commit(monitorados[i], comentario)

        if comando == 8:
            git_controle.push()

        if comando == 9:
            git_controle.pull()

        if comando == 10:
            if repo_atual != False:
                git_status = git_controle.git_status(repo_atual)
                monitorados = git_status[0]
                nao = git_status[1]
                print("Monitorados")
                for i in range(len(monitorados)):
                    if monitorados[i][1] == False:
                        print(monitorados[i][0])
                print(" \nNao monitorados:")
                for j in range(len(nao)):
                    print(nao[j][0])
        if comando == 11:
            log = git_controle.git_log()
            for i in range(len(log)):
                print(log[i][0][0], "->", log[i][1])


if __name__ == '__main__':
    main()

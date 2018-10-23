class Arquivo:
    def __init__(self):
        self.nome = ""
		self.comentario =""
    def criar_arquivo(self, repo_atual, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        repo_atual.append([nome_arquivo, "", False, False])
        return True

    def remover(self, nome_arquivo, repo_atual):
        self.nome_arquivo = nome_arquivo
        for i in range(1, len(repo_atual)):
            if repo_atual[i][0] == self.nome_arquivo:
                del repo_atual[i]
                return True
        return False

    def editar(self, nome_arquivo, repo_atual, texto, tipo):
        if tipo == 1:
            for i in range(1, len(repo_atual)):
                if repo_atual[i][0] == nome_arquivo:
                    repo_atual[i][1] = texto
        if tipo == 2:
            for i in range(1, len(repo_atual)):
                if repo_atual[i][0] == nome_arquivo:
                    repo_atual[i][1] += texto


class RepositorioLocal:
    def __init__(self):
        self.nome = "nome"

    def criar_repositorio(self, nome, repositorio_local):
        self.nome = nome
        repositorio_local.append([self.nome])

    def add(self, repo_atual, nome_arquivo, area_commit):
        self.nome = "i"
        for i in range(1, len(repo_atual)):
            if repo_atual[i][0] == nome_arquivo:
                repo_atual[i][2] = True
                area_commit.append(repo_atual[i])

    def commit(self, arquivo, comentario, area_commits):
        self.comentario = comentario
        arquivo[3] = True
        area_commits.append([arquivo, comentario])

    def push(self, strenger_area):
        pass


class RepositorioRemoto:
    def __init__(self):
        self.repositorio_remoto = []

    def recebe_push(self, arquivo, repo_remoto):
        self.repo_remoto = repo_remoto
        for i in range(len(repo_remoto)):
            if repo_remoto[i][0] == arquivo[0]:
                repo_remoto[i] = arquivo
                break
        self.repo_remoto.append(arquivo)

    def manda(self):
        return self.repositorio_remoto

    def mostra_repo_remoto(self):
        print(self.repositorio_remoto)

    def poll(self, repo_remoto, repo_local, strenger_area):
        for i in range(len(repo_local)):
            dire = repo_local[i]
            for j in range(len(dire)):
                arquivo_atual = dire[j]
                for k in range(len(repo_remoto)):
                    if arquivo_atual[0] == repo_remoto[k][0]:
                        arquivo_atual = repo_remoto[k]
                        arquivo_atual[3] = False
                        strenger_area.append(arquivo_atual)

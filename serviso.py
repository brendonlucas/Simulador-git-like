from modelos import *


class ControleGit:
    def __init__(self):
        self.repositorios_local = []
        self.repo_remoto = [['null']]
        self.repositorio = RepositorioLocal()
        self.arquivo = Arquivo()
        self.repositorio_remoto = RepositorioRemoto()
        self.stage_area = []
        self.commits = []
        self.monitorado = []
        self.nao_monitorado = []

    def criar_repositorio(self, nome):
        self.repositorio.criar_repositorio(nome, self.repositorios_local)

    def seleciona_repositorio(self, repo_solicitado):
        for i in range(len(self.repositorios_local)):
            if self.repositorios_local[i][0] == repo_solicitado:
                return self.repositorios_local[i]
        return False

    def criar_arquivo(self, nome_arquivo, repo_atual):
        criar = self.arquivo.criar_arquivo(repo_atual, nome_arquivo)
        if criar:
            return True

    def git_status(self, repo_atual):
        self.monitorado = []
        self.nao_monitorado = []
        for i in range(1, len(repo_atual)):
            if repo_atual[i][2] == True:
                self.monitorado.append([repo_atual[i][0], repo_atual[i][3]])
            else:
                self.nao_monitorado.append([repo_atual[i][0], repo_atual[i][3]])
        return self.monitorado, self.nao_monitorado

    def remover_arquivo(self, nome_arquivo, repo_atual):
        self.arquivo.remover(nome_arquivo, repo_atual)

    def editar_arquivo(self, nome_arquivo, repo_atual, texto, tipo):
        self.arquivo.editar(nome_arquivo, repo_atual, texto, tipo)

    def add(self, repo_atual, nome_arquivo):
        self.repositorio.add(repo_atual, nome_arquivo, self.stage_area)

    def commit(self, arquivo, comentario):
        self.repositorio.commit(arquivo, comentario, self.commits)

    def retorna_stage_area(self):
        return self.stage_area

    def push(self):
        for i in range(len(self.stage_area)):
            self.repositorio_remoto.recebe_push(self.stage_area[i], self.repo_remoto)
        self.stage_area = []

    def pull(self):
        self.repositorio_remoto.pull(self.repo_remoto, self.repositorios_local, self.stage_area)

    def git_log(self):
        return self.commits

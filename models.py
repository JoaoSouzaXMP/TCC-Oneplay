from config import CURSOR
from helpers import SQL_QUERYS
import base64

class Jogo:
    def __init__(self, CategoriaID=None, ExibirHome=None, Ordem=None, Nome=None):
        """Inicializa a classe Jogo."""
        self.categoriaid = CategoriaID
        self.exibirhome = ExibirHome
        self.ordem = Ordem
        self.nome = Nome

    def __repr__(self):
        """Representação da classe Jogo."""
        return f"Jogo(CategoriaID='{self.categoriaid}', ExibirHome='{self.exibirhome}', Ordem='{self.ordem}', Nome='{self.nome}')"

    @staticmethod
    def _executar(query, *params):
        """Executa uma consulta SQL."""
        return CURSOR.execute(SQL_QUERYS[query], *params)

    @classmethod
    def _exibir(cls, query):
        """Função auxiliar para exibir jogos."""
        consulta = cls._executar(query).fetchall()
        return [(jogo[:6] + (base64.b64encode(jogo[6]).decode('utf-8'),) if jogo[6] else jogo) for jogo in consulta]

    @classmethod
    def exibir(cls):
        """Exibe todos os jogos."""
        return cls._exibir('SelectJogosAll')

    @classmethod
    def exibiradm(cls):
        """Exibe todos os jogos para o administrador."""
        return cls._exibir('SelectJogosAllAdm')

    @classmethod
    def consultarid(cls, id):
        """Consulta jogo por id."""
        return cls._executar('SelectJogoId', id).fetchone()

    @classmethod
    def consultarpagina(cls, id):
        """Consulta página por id."""
        row = cls._executar('SelectPagina', id).fetchone()
        if not row:
            cls._executar('InserttblPaginaJogos', id)
            row = cls._executar('SelectPagina', id).fetchone()
        return row

    @classmethod
    def consultartutorial(cls, id):
        """Consulta tutorial por id."""
        return cls._executar('SelectTutorial', id).fetchall()

    @classmethod
    def consultarimagens(cls, id):
        """Consulta imagens por ID e decodifica em base64."""
        dados_imagem = cls._executar('SelectImagens', id).fetchone()
        if dados_imagem:
            dados_imagem = tuple(base64.b64encode(img).decode('utf-8') if img else None for img in dados_imagem)
        return dados_imagem

    @staticmethod
    def adicionar():
        """Adiciona um novo jogo."""
        Jogo._executar('InsertJogoDefault')

    @staticmethod
    def atualizarjogo(id, nome, arquivo=None):
        """Atualiza um jogo existente."""
        Jogo._executar('UpdateJogo', nome, id)
        if arquivo:
            img_bytes = arquivo.read()
            if Jogo._executar('SelectImagens', id).fetchone() is None:
                Jogo._executar('InserttblImagensJogos', id)
            Jogo._executar('UpdateImgIndex', img_bytes, id)

    @staticmethod
    def atualizarpagina(*args):
        """Atualiza um jogo existente e salva os dados binarios das imagens."""
        Jogo._executar('UpdatePaginaJogos', *args[0:13])
        if Jogo._executar('SelectImagens', args[12]).fetchone() is None:
            Jogo._executar('InserttblImagensJogos', args[12])
        for i, arquivo in enumerate(args[15:], start=1):
            if arquivo:
                arquivo.seek(0)
                img_bytes = arquivo.read()
                if i == 1:
                    Jogo._executar('UpdateImgPaginaJogo', img_bytes, args[12])
                elif i == 2:
                    Jogo._executar('UpdateImgNoticia1', img_bytes, args[12])
                elif i == 3:
                    Jogo._executar('UpdateImgNoticia2', img_bytes, args[12])

    @staticmethod
    def deletar(id):
        """Deleta um jogo existente."""
        Jogo._executar('DeleteJogo', id)

    @staticmethod
    def exibirjogo(id):
        """Alterna a exibição de um jogo. ~TRUE ~FALSE"""
        Jogo._executar('UpdateJogoExibir', id)

    @staticmethod
    def exibirtodos():
        """Exibe todos os jogo. ALL -> TRUE"""
        Jogo._executar('UpdateExibirTodos')

    @staticmethod
    def ocultartodos():
        """Oculta todos os jogo. ALL -> FALSE"""
        Jogo._executar('UpdateOcultarTodos')

    @staticmethod
    def adicionarpasso(id):
        """Adicionar um novo passo no tutorial."""
        Jogo._executar('InsertTutorialJogos', id)

    @staticmethod
    def atualizarpasso(*args):
        """Atualiza um dos passos do tutorial."""
        Jogo._executar('UpdateTutorialJogos', args[0:4])

    @staticmethod
    def deletarpasso(id):
        """Deletar um dos passos do tutorial."""
        Jogo._executar('DeleteTutorialJogos', id)

class Usuario:
    def __init__(self, nome, senha):
        """Inicializa a classe Usuario."""
        self.nome = nome
        self.senha = senha

    def __repr__(self):
        """Representação da classe Usuario."""
        return f"Usuario(nome='{self.nome}', senha='{self.senha}')"

    @staticmethod
    def _executar(query, *params):
        """Executa uma consulta SQL."""
        return CURSOR.execute(SQL_QUERYS[query], params)

    def adicionar(self):
        """Adiciona um novo usuário."""
        self._executar('InsertUsuario', self.nome, self.senha)

    @staticmethod
    def consultarnome(Nome):
        """Consulta usuário por nome."""
        return Jogo._executar('SelectUsuarioNome', Nome).fetchone()

    def consultarsenha(self):
        """Consulta senha do usuário."""
        return self._executar('SelectUsuarioNome', self.nome, self.senha).fetchone()

    def redefinirsenha(self):
        """Redefine a senha do usuário."""
        self._executar('UpdateSenhaUsuario', self.senha, self.nome)
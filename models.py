from config import CURSOR
from helpers import SQL_QUERYS
import base64

class Jogo:
    def __init__(self, CategoriaID, ExibirHome, Ordem, Nome):
        """Inicializa a classe Jogo."""
        self._categoriaid = CategoriaID
        self._exibirhome = ExibirHome
        self._ordem = Ordem
        self._nome = Nome

    def __repr__(self):
        """Representação da classe Jogo."""
        return f"'{self._categoriaid}','{self._exibirhome}','{self._ordem}','{self._nome}'"

    @staticmethod
    def _executar(query, *params):
        """Executa uma consulta SQL."""
        return CURSOR.execute(SQL_QUERYS[query], *params)

    @classmethod
    def _exibir(cls, query):
        """Função auxiliar para exibir jogos."""
        consulta = cls._executar(query).fetchall()
        for jogo in consulta:
            if jogo[6] is not None:
                jogo[6] = base64.b64encode(jogo[6]).decode('utf-8')
        return consulta

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
            for indice in range(3):
                if dados_imagem[indice] is not None:
                    dados_imagem[indice] = base64.b64encode(dados_imagem[indice]).decode('utf-8')
        return dados_imagem

    @staticmethod
    def adicionar():
        """Adiciona um novo jogo."""
        Jogo._executar('InsertJogoDefault')

    @staticmethod
    def atualizarjogo(id, nome, arquivo):
        """Atualiza um jogo existente."""
        Jogo._executar('UpdateJogo', nome, id)
        if arquivo:
            img_bytes = arquivo.read()
            Jogo._executar('InserttblImagensJogos', id) if Jogo._executar('SelectImagens', id).fetchone() is None else None
            Jogo._executar('UpdateImgIndex', img_bytes, id)

    @staticmethod
    def atualizarpagina(*args):
        """Atualiza um jogo existente e salva os dados binarios das imagens."""
        Jogo._executar('UpdatePaginaJogos', *args[0:13])
        Jogo._executar('InserttblImagensJogos', args[12]) if Jogo._executar('SelectImagens', args[12]).fetchone() is None else None
        for i, arquivo in enumerate(args[15:], start=1):
            if arquivo:
                arquivo.seek(0)
                img_bytes = arquivo.read()
                match i:
                    case 1:
                        Jogo._executar('UpdateImgPaginaJogo', img_bytes, args[12])
                    case 2:
                        Jogo._executar('UpdateImgNoticia1', img_bytes, args[12])
                    case 3:
                        Jogo._executar('UpdateImgNoticia2', img_bytes, args[12])

    @staticmethod
    def deletar(id):
        """Deleta um jogo existente."""
        Jogo._executar('DeleteJogo', id)

    @staticmethod
    def exibirjogo(id):
        """Alterna a exibição de um jogo. ~TRUE ~FALSE"""
        Jogo._executar('UpdateJogoExibir',id)

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
        Jogo._executar('InsertTutorialJogos',id)

    @staticmethod
    def atualizarpasso(*args):
        """Atualiza um dos passos do tutorial."""
        print(*args[0:4])
        Jogo._executar('UpdateTutorialJogos', args[0:4])

    @staticmethod
    def deletarpasso(id):
        """Deletar um dos passos do tutorial."""
        Jogo._executar('DeleteTutorialJogos',id)

class Usuario:
    def __init__(self, nome, senha):
        """Inicializa a classe Usuario."""
        self._nome = nome
        self._senha = senha

    def __repr__(self):
        """Representação da classe Usuario."""
        return f"Usuario(nome='{self._nome}', senha='{self._senha}')"

    def _executar(self, query, *params):
        """Executa uma consulta SQL."""
        return CURSOR.execute(SQL_QUERYS[query], params)

    def adicionar(self):
        """Adiciona um novo usuário."""
        self._executar('InsertUsuario', self._nome, self._senha)

    @staticmethod
    def consultarnome(Nome):
        """Consulta usuário por nome."""
        return Jogo._executar('SelectUsuarioNome', Nome).fetchone()

    def consultarsenha(self):
        """Consulta senha do usuário."""
        return self._executar('SelectUsuarioNome', self._nome, self._senha).fetchone()

    def redefinirsenha(self):
        """Redefine a senha do usuário."""
        self._executar('UpdateSenhaUsuario', self._senha, self._nome)
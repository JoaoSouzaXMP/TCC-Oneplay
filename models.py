from config import CURSOR
from helpers import SQL_QUERYS
import base64

class Jogo:
    def __init__(self,CategoriaID,ExibirHome,Ordem,Nome):
        self._categoriaid = CategoriaID
        self._exibirhome = ExibirHome
        self._ordem = Ordem
        self._nome = Nome
    def __repr__(self):
        return f"'{self._categoriaid}','{self._exibirhome}','{self._ordem}','{self._nome}'"
    @classmethod
    def exibir(cls):
        consulta = CURSOR.execute(SQL_QUERYS['SelectJogosAll']).fetchall()
        jogos_decodificados = []
        for jogo in consulta:
            jogo_copia = list(jogo)
            if jogo_copia[6] is not None:
                jogo_copia[6] = base64.b64encode(jogo_copia[6]).decode('utf-8')
            jogos_decodificados.append(jogo_copia)
        return jogos_decodificados
    def consultarid(id):
        return CURSOR.execute(SQL_QUERYS['SelectJogoId'],id).fetchone()
    def consultarpagina(id):
        return CURSOR.execute(SQL_QUERYS['SelectPagina'],id).fetchone()
    def consultartutorial(id):
        return CURSOR.execute(SQL_QUERYS['SelectTutorial'],id).fetchall()
    def consultarimagens(id):
        imagens = CURSOR.execute(SQL_QUERYS['SelectImagens'],id).fetchone()
        if imagens:
            for i in (0,2):
                if imagens[i] is not None:
                    imagens[i] = base64.b64encode(imagens[i]).decode('utf-8')
        return imagens
    def adicionar(self):
        CURSOR.execute(SQL_QUERYS['InsertJogo'],self._nome,self._categoria,self._console)
    def atualizar(id,nome,arquivo):
        CURSOR.execute(SQL_QUERYS['UpdateJogo'],nome,id)
        row = CURSOR.execute(SQL_QUERYS['SelectImagens'],id).fetchone()
        if row:
            img_bytes = arquivo.read()
            CURSOR.execute(SQL_QUERYS['UpdateImagem'],img_bytes,id)
        else:
            img_bytes = arquivo.read()
            CURSOR.execute(SQL_QUERYS['InsertImagem'],id,img_bytes)
    def deletar(id):
        CURSOR.execute(SQL_QUERYS['DeleteJogo'],id)

class Usuario:
    def __init__(self,nome,senha):
        self._nome = nome
        self._senha = senha
    def __repr__(self):
        return f"'{self._nome}','{self._senha}'"
    def adicionar(self):
        CURSOR.execute(SQL_QUERYS['InsertUsuario'],self._nome,self._senha)
    def consultarnome(Nome):
        return CURSOR.execute(SQL_QUERYS['SelectUsuarioNome'],Nome).fetchone()
    def consultarsenha(self):
        return CURSOR.execute(SQL_QUERYS['SelectUsuarioNome'],self._nome,self._senha).fetchone()
    def redefinirsenha(self):
        CURSOR.execute(SQL_QUERYS['UpdateSenhaUsuario'],self._senha,self._nome)
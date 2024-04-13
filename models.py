from config import CURSOR
from helpers import SQL_QUERYS
import base64

class Jogo:
    def __init__(self,CategoriaID,ExibirHome,Ordem,Nome,Frase,Descricao,Download):
        self._categoriaid = CategoriaID
        self._exibirhome = ExibirHome
        self._ordem = Ordem
        self._nome = Nome
        self._frase = Frase
        self._descricao = Descricao
        self._download = Download

    def __repr__(self):
        return f"'{self._categoriaid}','{self._exibirhome}','{self._ordem}','{self._nome}','{self._frase}','{self._descricao}','{self._download}'"
    
    @classmethod
    def exibir(cls):
        consulta = CURSOR.execute(SQL_QUERYS['SelectJogosAll']).fetchall()
        jogos_decodificados = []
        for jogo in consulta:
            jogo_copia = list(jogo)
            if jogo_copia[3] is not None:
                jogo_copia[3] = base64.b64encode(jogo_copia[3]).decode('utf-8')
            jogos_decodificados.append(jogo_copia)
        return jogos_decodificados
    
    def consultarnome(self):
        return CURSOR.execute(SQL_QUERYS['SelectJogoNome'],self._nome).fetchone()
    
    def consultarid(id):
        consulta = CURSOR.execute(SQL_QUERYS['SelectJogoId'],id).fetchone()
        jogo_decodificado = []
        jogo_copia = list(consulta)
        if jogo_copia[6] is not None:
            jogo_copia[6] = base64.b64encode(jogo_copia[6]).decode('utf-8')
        if jogo_copia[7] is not None:
            jogo_copia[7] = base64.b64encode(jogo_copia[7]).decode('utf-8')
        if jogo_copia[10] is not None:
            jogo_copia[10] = base64.b64encode(jogo_copia[10]).decode('utf-8')
        jogo_decodificado.append(jogo_copia)
        return jogo_decodificado
    
    def tutorial(id):
        lista = CURSOR.execute('select * from tblTutoriais where JogoID = ?',id).fetchall()
        return lista
    
    def videos(id):
        lista = CURSOR.execute('select * from tblVideos where JogoID = ?',id).fetchall()
        return lista
    
    def adicionar(self):
        CURSOR.execute(SQL_QUERYS['InsertJogo'],self._nome,self._categoria,self._console)

    def atualizar(id,nome,categoria,console):
        CURSOR.execute(SQL_QUERYS['UpdateJogo'],nome,categoria,console,id)

    def deletar(id):
        Imagem.excluir(id)
        CURSOR.execute(SQL_QUERYS['DeleteJogo'],id)

class Imagem:
    def exibirhomes():
        img_data = CURSOR.execute(SQL_QUERYS['SelectImagemHomes'],id).fetchone()
        if img_data:
            img_base64 = base64.b64encode(img_data[0]).decode('utf-8')
            return img_base64
        return False
    def salvar(id,arquivo):
        img_bytes = arquivo.read()
        arquivo.seek(0)
        CURSOR.execute(SQL_QUERYS['InsertImagem'],id,img_bytes)
    def editar(id,arquivo):
        row = CURSOR.execute(SQL_QUERYS['SelectImagem'],id).fetchone()
        if row:
            img_bytes = arquivo.read()
            arquivo.seek(0)
            CURSOR.execute(SQL_QUERYS['UpdateImagem'],img_bytes,id)
        else:
            Imagem.salvar(id,arquivo)
    def excluir(id):
        CURSOR.execute(SQL_QUERYS['DeleteImagem'],id)

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
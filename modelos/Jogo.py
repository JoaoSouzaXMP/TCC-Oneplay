from main import db
from modelos.ImagemJogo import ImagemJogo
import base64

class Jogo(db.Model):
    __tablename__ = 'tblJogos'
    JogoID = db.Column(db.INTEGER, primary_key=True)
    CategoriaID = db.Column(db.INTEGER)
    ExibirHome = db.Column(db.BOOLEAN)
    Ordem = db.Column(db.INTEGER)
    Nome = db.Column(db.VARCHAR)
    
    def __repr__(self) -> str:
        return str((
            self.JogoID,
            self.CategoriaID,
            self.ExibirHome,
            self.Ordem,
            self.Nome,
        ))
    
    @classmethod    
    def get_jogos_boolean(cls, exibir_home: bool = None) -> list:
        query = db.session.query(Jogo,ImagemJogo.ImgIndex).outerjoin(ImagemJogo, Jogo.JogoID == ImagemJogo.JogoID)

        if exibir_home is not None:
            query = query.filter(Jogo.ExibirHome == exibir_home)
        
        results = query.all()

        jogos = []
        for jogo, img_index in results:
            jogo_list = (
                jogo.JogoID,
                jogo.CategoriaID,
                jogo.ExibirHome,
                jogo.Ordem,
                jogo.Nome,
                base64.b64encode(img_index).decode('utf-8') if img_index else None,
            )
            jogos.append(jogo_list)

        return jogos
    
    @classmethod
    def get_jogo_by_jogoid(cls, jogo_id):
        # Consulta para buscar um único jogo pelo JogoID
        jogo = db.session.query(Jogo).filter(Jogo.JogoID == jogo_id).first()
        if jogo:
            return jogo
        else:   
            return None
    
    @staticmethod
    def adicionar():
        # Adiciona um novo jogo
        novo_jogo = Jogo()
        db.session.add(novo_jogo)
        db.session.commit()

    @staticmethod
    def exibir_by_jogoid(id):
        # Alterna a exibição de apenas um jogo. ~TRUE ~FALSE
        jogo = Jogo.query.filter_by(JogoID=id).first()
        jogo.ExibirHome = not jogo.ExibirHome
        db.session.commit()

    @staticmethod
    def alterar_exibicao_todos_boolean(valor):
        # Altera a exibição de todos os jogos para o valor especificado. TRUE or FALSE
        Jogo.query.update({Jogo.ExibirHome: valor})
        db.session.commit()

    @staticmethod
    def deletar_by_jogoid(id):
        # Deleta um jogo existente
        # !!! Configurado a ForeignKey com cascade delete !!!
        jogo = Jogo.query.filter_by(JogoID=id).first()
        db.session.delete(jogo)
        db.session.commit()

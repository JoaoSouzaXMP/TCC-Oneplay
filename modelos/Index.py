from main import db
from modelos import Jogo, ImagemJogo

class Index:
    def __init__(self, JogoID=None, Nome=None, ImgIndex=None) -> None:
        self.jogoid = JogoID
        self.nome = Nome
        self.imgindex = ImgIndex

    def atualizar_by_forms(jogo_id, nome_jogo, img_index=None):
        try:
            # Atualizar a tabela Jogo
            jogo = Jogo.query.filter_by(JogoID=jogo_id).first()
            if jogo:
                jogo.Nome = nome_jogo
                db.session.commit()

            # Atualizar a tabela ImagemJogo
            if img_index:
                ImagemJogo.atualizar_imagem_index(jogo_id, img_index)

        except Exception as e:
            db.session.rollback()
            print(f"Erro ao atualizar: {e}")
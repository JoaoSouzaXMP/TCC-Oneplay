from main import db
import base64

class ImagemJogo(db.Model):
    __tablename__ = 'tblImagensJogos'
    ImagemJogoID = db.Column(db.INTEGER, primary_key=True)
    JogoID = db.Column(db.INTEGER, db.ForeignKey('tblJogos.JogoID', ondelete='CASCADE'))
    ImgIndex = db.Column(db.VARBINARY)
    ImgPaginaJogo = db.Column(db.VARBINARY)
    ImgNoticia1 = db.Column(db.VARBINARY)
    ImgNoticia2 = db.Column(db.VARBINARY)
    jogo = db.relationship('Jogo', backref=db.backref('imagens_jogo', cascade='all, delete-orphan'))
    def __repr__(self) -> str:
        return str((
            self.ImagemJogoID,
            self.JogoID,
            self.ImgIndex,
            self.ImgPaginaJogo,
            self.ImgNoticia1,
            self.ImgNoticia2,
        ))

    @classmethod
    def get_imagens_base64_by_jogoid(cls, jogo_id):
        imagens = db.session.query(ImagemJogo).filter(ImagemJogo.JogoID == jogo_id).first()
        if imagens:
            imagens.ImgPaginaJogo = base64.b64encode(imagens.ImgPaginaJogo).decode('utf-8') if imagens.ImgPaginaJogo else None
            imagens.ImgNoticia1 =  base64.b64encode(imagens.ImgNoticia1).decode('utf-8') if imagens.ImgNoticia1 else None
            imagens.ImgNoticia2 =  base64.b64encode(imagens.ImgNoticia2).decode('utf-8') if imagens.ImgNoticia2 else None
            return imagens
        else:
            return None
    
    @classmethod
    def get_imagens_binary_by_id(cls, jogo_id):
        imagens = db.session.query(ImagemJogo).filter(ImagemJogo.JogoID == jogo_id).first()
        if imagens is None:
            linha = ImagemJogo(JogoID=jogo_id)
            db.session.add(linha)
            db.session.commit()
            return linha
        return imagens
        
    @classmethod    
    def get_imagem_index_by_id(cls, jogo_id):
        img = db.session.query(ImagemJogo.ImgIndex).filter(ImagemJogo.JogoID == jogo_id).first()
        if img:
            img = base64.b64encode(img).decode('utf-8') 
            return img
        else:
            return None
    
    def atualizar_imagem_index(jogo_id, img):
        try:
            img_bytes = img.read()
            imagem_jogo = ImagemJogo.query.filter_by(JogoID=jogo_id).first()
            if imagem_jogo is None:
                imagem_jogo = ImagemJogo(JogoID=jogo_id, ImgIndex=img_bytes)
                db.session.add(imagem_jogo)
            else:
                imagem_jogo.ImgIndex = img_bytes
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao atualizar: {e}")

    def atualizar_imagens_pagina_forms(jogo_id, img1=None, img2=None, img3=None):
        try:
            imgs = db.session.query(ImagemJogo).filter_by(JogoID=jogo_id).first()
            if not imgs:
                return
            
            for img, attr in zip([img1, img2, img3], ['ImgPaginaJogo', 'ImgNoticia1', 'ImgNoticia2']):
                if img:
                    setattr(imgs, attr, img.read())
            
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao atualizar: {e}")
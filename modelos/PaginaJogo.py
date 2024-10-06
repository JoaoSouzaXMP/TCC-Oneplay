from main import db

class PaginaJogo(db.Model):
    __tablename__ = 'tblPaginaJogos'
    PaginaJogoID = db.Column(db.INTEGER, primary_key=True)
    JogoID = db.Column(db.INTEGER, db.ForeignKey('tblJogos.JogoID', ondelete='CASCADE'))
    ResumoJogo = db.Column(db.VARCHAR)
    LinkDownload = db.Column(db.VARCHAR)
    DescricaoJogo = db.Column(db.VARCHAR)
    TituloTutorial = db.Column(db.VARCHAR)
    DescricaoTutorial = db.Column(db.VARCHAR)
    TituloNoticia1 = db.Column(db.VARCHAR)
    DescricaoNoticia1 = db.Column(db.VARCHAR)
    TituloNoticia2 = db.Column(db.VARCHAR)
    DescricaoNoticia2 = db.Column(db.VARCHAR)
    TituloVideo = db.Column(db.VARCHAR)
    DescricaoVideo = db.Column(db.VARCHAR)
    LinkVideo = db.Column(db.VARCHAR)
    jogo = db.relationship('Jogo', backref=db.backref('pagina_jogo', cascade='all, delete-orphan'))
    
    def __repr__(self) -> str:
        return str((
            self.PaginaJogoID,
            self.JogoID,
            self.ResumoJogo,
            self.LinkDownload,
            self.DescricaoJogo,
            self.TituloTutorial,
            self.DescricaoTutorial,
            self.TituloNoticia1,
            self.DescricaoNoticia1,
            self.TituloNoticia2,
            self.DescricaoNoticia2,
            self.TituloVideo,
            self.DescricaoVideo,
            self.LinkVideo,
        ))
    
    @classmethod
    def get_pagina_by_jogoid(cls, jogo_id):
        pagina = db.session.query(PaginaJogo).filter(PaginaJogo.JogoID == jogo_id).first()
        if pagina is None:
            print('Criando Pagina !')
            pagina = PaginaJogo(JogoID=jogo_id)
            db.session.add(pagina)
            db.session.commit()
        return pagina
    
    def update_columns(self, updates):
        for key, value in updates.items():
            if hasattr(self, key):
                setattr(self, key, value)
        db.session.commit()
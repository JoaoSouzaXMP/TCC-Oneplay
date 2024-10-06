from main import db

class TutorialJogo(db.Model):
    __tablename__ = 'tblTutorialJogos'
    TutorialJogoid = db.Column(db.INTEGER, primary_key=True)
    JogoID = db.Column(db.INTEGER, db.ForeignKey('tblJogos.JogoID', ondelete='CASCADE'))
    Ordem = db.Column(db.INTEGER)
    Passo = db.Column(db.VARCHAR)
    DescricaoPasso = db.Column(db.VARCHAR)
    jogo = db.relationship('Jogo', backref=db.backref('tutorial_jogo', cascade='all, delete-orphan'))
    
    def __repr__(self) -> str:
        return str((
            self.TutorialJogoid,
            self.JogoID,
            self.Ordem,
            self.Passo,
            self.DescricaoPasso,
        ))
    
    @classmethod
    def get_tutorial_by_jogoid(cls, jogo_id):
        tutorial = db.session.query(TutorialJogo).filter(TutorialJogo.JogoID == jogo_id).all()
        if tutorial is None:
            print('Criando Tutorial !')
            tutorial = TutorialJogo(JogoID=jogo_id)
            db.session.add(tutorial)
            db.session.commit()
        return tutorial
    
    def novo_passo_by_jogoid(jogo_id):
        novo_passo = TutorialJogo(JogoID=jogo_id)
        db.session.add(novo_passo)
        db.session.commit()
    
    def atualizar_passo_forms(tutorial_jogoid,numero_tutorial,titulo_tutorial,descricao_tutorial):
        try:
            tutorial = db.session.query(TutorialJogo).filter_by(TutorialJogoid=tutorial_jogoid).first()
            tutorial.Ordem = numero_tutorial
            tutorial.Passo = titulo_tutorial
            tutorial.DescricaoPasso = descricao_tutorial
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            print(f"Erro ao atualizar: {e}")

    def deletar_passo_tutorialid(tutorial_jogoid):
        tutorial = db.session.query(TutorialJogo).filter_by(TutorialJogoid=tutorial_jogoid).first()
        db.session.delete(tutorial)
        db.session.commit()
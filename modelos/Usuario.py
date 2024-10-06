from main import db

class Usuario(db.Model):
    __tablename__ = 'tblUsuarios'
    UsuarioID = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.VARCHAR)
    Senha = db.Column(db.VARCHAR)
    OP = db.Column(db.BOOLEAN)

    def __repr__(self) -> str:
        return str((
            self.UsuarioID,
            self.Nome,
            self.Senha,
            self.OP,
        ))

    def consultar_by_nome(nome):
        usuario = db.session.query(Usuario).filter(Usuario.Nome == nome).first()
        if usuario:
            return usuario
        else:
            return None
        
    def adicionar_novo(nome,senha):
        usuario = Usuario(Nome=nome, Senha=senha)
        db.session.add(usuario)
        db.session.commit()

    def sobrescrever_senha(nome,senha):
        usuario = db.session.query(Usuario).filter(Usuario.Nome == nome).first()
        if usuario:
            usuario.Senha = senha
            db.session.commit()
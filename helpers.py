from main import app
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,InputRequired,Regexp

# Validação Inputs Jogos
class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo',validators=[DataRequired(),Length(min=2,max=25),InputRequired()])
    salvar = SubmitField('Salvar')
# Validação Inputs Usuarios
class FormularioUsuario(FlaskForm):
    nome = StringField('Nome de Usuário',validators=[DataRequired(),Length(min=4,max=50),InputRequired(),Regexp('^[\\w-]+$')])
    senha = PasswordField('Senha',validators=[DataRequired(),Length(min=4,max=50),InputRequired()])
    login = SubmitField('Login')

SQL_QUERYS = {}
# Comandos Jogos
SQL_QUERYS['SelectJogosAll'] = '''select a.*,b.ImgIndex from tblJogos a left join tblImagensJogos b on b.JogoID = a.JogoID where a.ExibirHome = 1'''
SQL_QUERYS['SelectJogoId'] = '''select * from tblJogos where JogoID = ?'''
SQL_QUERYS['SelectPagina'] = '''select ResumoJogo,LinkDownload,DescricaoJogo,TituloTutorial,DescricaoTutorial,TituloNoticia1,DescricaoNoticia1,TituloNoticia2,DescricaoNoticia2,TituloVideo,DescricaoVideo,LinkVideo from tblPaginaJogos where JogoID = ?'''
SQL_QUERYS['SelectTutorial'] = '''select Ordem,Passo,DescricaoPasso from tblTutorialJogos where JogoID = ?'''
SQL_QUERYS['SelectImagens'] = '''select ImgPaginaJogo,ImgNoticia1,ImgNoticia2 from tblImagensJogos where JogoID = ?'''

SQL_QUERYS['UpdateJogo'] = '''UPDATE tblJogos SET Nome=? WHERE JogoID=?'''

SQL_QUERYS['UpdateImagem'] = '''update tblImagensJogos set ImgIndex = ? where JogoID = ?'''

SQL_QUERYS['InsertImagem'] = '''insert into tblImagensJogos(JogoID,ImgIndex) values(?,?)'''

SQL_QUERYS['DeleteJogo'] = '''DELETE tblJogos WHERE JogoID=?'''

# Comandos Usuarios
SQL_QUERYS['SelectUsuarioNome'] = '''SELECT * FROM tblUsuarios WHERE Nome LIKE ?'''
SQL_QUERYS['InsertUsuario'] = '''INSERT INTO tblUsuarios(Nome,Senha) VALUES(?,?)'''
SQL_QUERYS['UpdateSenhaUsuario'] = '''UPDATE tblUsuarios SET Senha = ? WHERE nome LIKE ?'''
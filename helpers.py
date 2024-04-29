from main import app
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField,HiddenField
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
# Validação Inputs Pagina Jogos
VALIDACAO_PAGINA = [Length(min=0,max=1000)]
class FormularioPagina(FlaskForm):
    ResumoJogo = TextAreaField('Resumo Jogo',validators=VALIDACAO_PAGINA)
    LinkDownload = StringField('Link Download',validators=VALIDACAO_PAGINA)
    DescricaoJogo = TextAreaField('Descricao Jogo',validators=VALIDACAO_PAGINA)
    TituloTutorial = StringField('Titulo Tutorial',validators=VALIDACAO_PAGINA)
    DescricaoTutorial = TextAreaField('Descricao Tutorial',validators=VALIDACAO_PAGINA)
    TituloNoticia1 = StringField('Titulo Noticia 1',validators=VALIDACAO_PAGINA)
    DescricaoNoticia1 = TextAreaField('Descricao Noticia 1',validators=VALIDACAO_PAGINA)
    TituloNoticia2 = StringField('Titulo Noticia 2',validators=VALIDACAO_PAGINA)
    DescricaoNoticia2 = TextAreaField('Descricao Noticia 2',validators=VALIDACAO_PAGINA)
    TituloVideo = StringField('Titulo Video',validators=VALIDACAO_PAGINA)
    DescricaoVideo = TextAreaField('Descricao Video',validators=VALIDACAO_PAGINA)
    LinkVideo = StringField('Link Video',validators=VALIDACAO_PAGINA)
    JogoID = HiddenField()
    salvar = SubmitField('Salvar')
class FormularioTutorial(FlaskForm):
    NumeroTutorial = StringField('Numero Tutorial',validators=VALIDACAO_PAGINA)
    TituloTutorial = StringField('Titulo Tutorial',validators=VALIDACAO_PAGINA)
    DescricaoTutorial = StringField('Descricao Tutorial',validators=VALIDACAO_PAGINA)
    ID = HiddenField()
    salvar = SubmitField('Salvar')

SQL_QUERYS = {}
# Comandos Jogos
SQL_QUERYS['SelectJogosAll'] = '''select a.*,b.ImgIndex from tblJogos a left join tblImagensJogos b on b.JogoID = a.JogoID where a.ExibirHome = 1'''
SQL_QUERYS['SelectJogosAllAdm'] = '''select a.*,b.ImgIndex from tblJogos a left join tblImagensJogos b on b.JogoID = a.JogoID'''
SQL_QUERYS['SelectJogoId'] = '''select * from tblJogos where JogoID = ?'''
SQL_QUERYS['SelectPagina'] = '''select JogoID,ResumoJogo,LinkDownload,DescricaoJogo,TituloTutorial,DescricaoTutorial,TituloNoticia1,DescricaoNoticia1,TituloNoticia2,DescricaoNoticia2,TituloVideo,DescricaoVideo,LinkVideo from tblPaginaJogos where JogoID = ?'''
SQL_QUERYS['SelectTutorial'] = '''select * from tblTutorialJogos where JogoID = ?'''
SQL_QUERYS['SelectImagens'] = '''select ImgPaginaJogo,ImgNoticia1,ImgNoticia2 from tblImagensJogos where JogoID = ?'''

SQL_QUERYS['UpdateJogo'] = '''UPDATE tblJogos SET Nome=? WHERE JogoID=?'''
SQL_QUERYS['UpdateJogoExibir'] = '''UPDATE tblJogos SET ExibirHome=~ExibirHome WHERE JogoID=?'''
SQL_QUERYS['UpdateImgIndex'] = '''update tblImagensJogos set ImgIndex = ? where JogoID = ?'''
SQL_QUERYS['UpdateImgPaginaJogo'] = '''update tblImagensJogos set ImgPaginaJogo = ? where JogoID = ?'''
SQL_QUERYS['UpdateImgNoticia1'] = '''update tblImagensJogos set ImgNoticia1 = ? where JogoID = ?'''
SQL_QUERYS['UpdateImgNoticia2'] = '''update tblImagensJogos set ImgNoticia2 = ? where JogoID = ?'''
SQL_QUERYS['UpdateExibirTodos'] = '''update tblJogos set ExibirHome = 1'''
SQL_QUERYS['UpdateOcultarTodos'] = '''update tblJogos set ExibirHome = 0'''
SQL_QUERYS['UpdatePaginaJogos'] = '''update tblPaginaJogos set ResumoJogo=?, LinkDownload=?, DescricaoJogo=?, TituloTutorial=?, DescricaoTutorial=?, TituloNoticia1=?, DescricaoNoticia1=?, TituloNoticia2=?, DescricaoNoticia2=?, TituloVideo=?, DescricaoVideo=?, LinkVideo =? where JogoID = ?'''
SQL_QUERYS['UpdateTutorialJogos'] = '''update tblTutorialJogos set Ordem=?,Passo=?,DescricaoPasso=? where TutorialJogoid = ?'''

SQL_QUERYS['InsertJogoDefault'] = '''insert into tblJogos default values'''
SQL_QUERYS['InsertTutorialJogos'] = '''insert into tblTutorialJogos(JogoID) values(?)'''
SQL_QUERYS['InserttblImagensJogos'] = '''insert into tblImagensJogos(JogoID) values(?)'''
SQL_QUERYS['InserttblPaginaJogos'] = '''insert into tblPaginaJogos(JogoID) values(?)'''

SQL_QUERYS['DeleteJogo'] = '''DELETE tblJogos WHERE JogoID=?'''
SQL_QUERYS['DeleteTutorialJogos'] = '''delete tblTutorialJogos where TutorialJogoid = ?'''

# Comandos Usuarios
SQL_QUERYS['SelectUsuarioNome'] = '''SELECT * FROM tblUsuarios WHERE Nome LIKE ?'''
SQL_QUERYS['InsertUsuario'] = '''INSERT INTO tblUsuarios(Nome,Senha) VALUES(?,?)'''
SQL_QUERYS['UpdateSenhaUsuario'] = '''UPDATE tblUsuarios SET Senha = ? WHERE nome LIKE ?'''
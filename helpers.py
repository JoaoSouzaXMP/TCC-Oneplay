from main import app
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField,HiddenField
from wtforms.validators import DataRequired,Length,InputRequired,Regexp

# Validação Inputs Jogos
class FormularioJogo(FlaskForm):
    ID = HiddenField()
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

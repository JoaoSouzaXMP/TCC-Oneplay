from main import app
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,InputRequired,Regexp
import os

''' FORMULARIOS '''
# Validação Inputs Jogos
VALIDACAO_JOGO = [DataRequired(),Length(min=2,max=50),InputRequired()]
class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo',validators=VALIDACAO_JOGO)
    categoria = StringField('Categoria',validators=VALIDACAO_JOGO)
    console = StringField('Console',validators=VALIDACAO_JOGO)
    salvar =  SubmitField('Salvar')
# Validação Inputs Usuarios
class FormularioUsuario(FlaskForm):
    nome = StringField('Nome de Usuário',validators=[DataRequired(),Length(min=4,max=50),InputRequired(),Regexp(r'/[\w-]/m')])
    senha = PasswordField('Senha',validators=[DataRequired(),Length(min=4,max=50),InputRequired()])
    login = SubmitField('Login')

''' COMANDOS SQL '''
SQL_QUERYS = {}
# Comandos tblJogos
SQL_QUERYS['SelectJogosAll'] = '''select a.JogoID,a.Nome,a.Frase,b.Home from tblJogos a inner join tblBanners b on b.JogoID = a.JogoID'''
SQL_QUERYS['SelectJogoNome'] = '''SELECT * FROM tblJogos WHERE Nome LIKE ?'''
SQL_QUERYS['SelectJogoId'] = '''select a.JogoID,a.Nome,a.Frase,a.Descricao,b.Home,a.Download,b.Banner,c.Imagem1,c.Titulo1,c.Descricao1,c.Imagem2,c.Titulo2,c.Descricao2,d.Titulo,d.Descricao,d.Link
from tblJogos a
left join tblBanners b on b.JogoID = a.JogoID
left join tblImagens c on c.JogoID = a.JogoID
left join tblVideos d on d.JogoID = a.JogoID
where a.JogoID = ?'''
SQL_QUERYS['InsertJogo'] = '''INSERT INTO tblJogos(Nome,Categoria,Console) VALUES(?,?,?)'''
SQL_QUERYS['UpdateJogo'] = '''UPDATE tblJogos SET Nome=?, Categoria=?, Console=? WHERE JogoID=?'''
SQL_QUERYS['DeleteJogo'] = '''DELETE tblJogos WHERE JogoID=?'''
# Comandos tblImagens
SQL_QUERYS['SelectImagemHomes'] = '''select JogoID,Home from tblBanners'''
SQL_QUERYS['SelectImagemHome'] = '''select Home from tblBanners where JogoID = ?'''
SQL_QUERYS['InsertImagem'] = '''INSERT INTO tblImagens VALUES (?,?)'''
SQL_QUERYS['UpdateImagem'] = '''UPDATE tblImagens SET Imagem = ? WHERE JogoID = ?'''
SQL_QUERYS['DeleteImagem'] = '''DELETE tblImagens WHERE JogoID = ?'''
# Comandos tblUsuarios
SQL_QUERYS['SelectUsuarioNome'] = '''SELECT * FROM tblUsuarios WHERE Nome LIKE ?'''
SQL_QUERYS['InsertUsuario'] = '''INSERT INTO tblUsuarios(Nome,Senha) VALUES(?,?)'''
SQL_QUERYS['UpdateSenhaUsuario'] = '''UPDATE tblUsuarios SET Senha = ? WHERE nome LIKE ?'''
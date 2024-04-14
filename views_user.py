from flask import render_template, request, redirect, session, flash, url_for
from main import app
from models import Usuario
from helpers import FormularioUsuario
from flask_bcrypt import generate_password_hash,check_password_hash

@app.route('/login')
def login():
    return render_template('login.html', url_atual = url_for('login'), titulo='Faça seu login', rota=url_for('autenticar'), proxima=request.form.get('proxima', url_for('index')), form=FormularioUsuario())

@app.route('/autenticar', methods=['POST'])
def autenticar():
    form = FormularioUsuario()
    if form.validate_on_submit():
        consulta_usuario = Usuario.consultarnome(form.nome.data)
        if consulta_usuario and check_password_hash(consulta_usuario[2], form.senha.data):
            session['usuario_logado'] = consulta_usuario[1]
            session['admin'] = consulta_usuario[3]
            flash(f'{consulta_usuario[1]} logado com sucesso !')
            return redirect(request.form.get('proxima', url_for('index')))
        else:
            flash('Credenciais incorretas !')
    return redirect(url_for('login'))

@app.route('/novousuario')
def novousuario():
    return render_template('login.html', url_atual=url_for('novousuario'), titulo='Cadastre seu Usuário', rota=url_for('cadastrarusuario'), proxima=request.form.get('proxima', url_for('index')), form=FormularioUsuario())

@app.route('/cadastrarusuario', methods=['POST'])
def cadastrarusuario():
    form = FormularioUsuario()
    if form.validate_on_submit():
        if Usuario.consultarnome(form.nome.data): 
            flash('Nome de Usuario já utilizado!')
            return redirect(url_for('novousuario'))
        else:
            novo_usuario = Usuario(form.nome.data,generate_password_hash(form.senha.data).decode('utf-8'))
            Usuario.adicionar(novo_usuario)
            flash(f'Usuario {novo_usuario._nome} Cadastrado com Sucesso!')
            return redirect(url_for('login'))
    else:
        flash('Caracteres inválidos !')
        return redirect(url_for('novousuario')) 

@app.route('/esquecisenha')
def esquecisenha():
    return render_template('login.html', url_atual=url_for('esquecisenha'), titulo='Informe o Usuário e a Senha nova', rota=url_for('redefinirsenha'), proxima=request.form.get('proxima', url_for('index')), form=FormularioUsuario())

@app.route('/redefinirsenha', methods=['POST'])
def redefinirsenha():
    form = FormularioUsuario()
    if form.validate_on_submit():
        user = Usuario(form.nome.data,generate_password_hash(form.senha.data).decode('utf-8'))
        consulta_usuario = Usuario.consultarnome(user._nome)
        if consulta_usuario:
            Usuario.redefinirsenha(user)
            flash(f'Senha do Usuário {user._nome} alterada com sucesso !')
            return redirect(url_for('login'))
        else:
            flash('Credenciais incorretas !')
    return redirect(url_for('esquecisenha'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    session['admin'] = None
    flash('Logout efetuado com sucesso !')
    return redirect(url_for('index'))
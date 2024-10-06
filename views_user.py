from flask import render_template, request, redirect, session, flash, url_for
from main import app
from modelos import Usuario
from helpers import FormularioUsuario
from flask_bcrypt import generate_password_hash,check_password_hash

@app.route('/login')
def login():
    return render_template('login.html', url_atual = url_for('login'), titulo='Faça seu login', rota=url_for('autenticar'), proxima=request.form.get('proxima', url_for('index')), form=FormularioUsuario())

@app.route('/autenticar', methods=['POST'])
def autenticar():
    form = FormularioUsuario()
    if form.validate_on_submit():
        consulta_usuario = Usuario.consultar_by_nome(form.nome.data)
        if consulta_usuario and check_password_hash(consulta_usuario.Senha, form.senha.data):
            session['usuario_logado'] = consulta_usuario.Nome
            session['admin'] = consulta_usuario.OP
            flash(f'{consulta_usuario.Nome} logado com sucesso !')
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
        if Usuario.consultar_by_nome(form.nome.data): 
            flash('Nome de Usuario já utilizado!')
            return redirect(url_for('novousuario'))
        else:
            Usuario.adicionar_novo(form.nome.data,generate_password_hash(form.senha.data).decode('utf-8'))
            flash(f'Usuario {form.nome.data} Cadastrado com Sucesso!')
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
        consulta_usuario = Usuario.consultar_by_nome(form.nome.data)
        if consulta_usuario:
            Usuario.sobrescrever_senha(form.nome.data,generate_password_hash(form.senha.data).decode('utf-8'))
            flash(f'Senha do Usuário {form.nome.data} alterada com sucesso !')
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
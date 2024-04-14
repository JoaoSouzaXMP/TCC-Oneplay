from flask import render_template, request, redirect, session, flash, url_for
from main import app
from models import Jogo
from helpers import FormularioJogo

@app.route('/')
def index():
    return render_template('index.html', titulo='HOME', jogos=Jogo.exibir())

@app.route('/jogo/<int:id>')
def jogo(id):
    return render_template('paginajogo.html', titulo='Jogo', jogo=Jogo.consultarid(id), pagina=Jogo.consultarpagina(id), tutorial=Jogo.consultartutorial(id), imagens=Jogo.consultarimagens(id))

@app.route('/info')
def info():
    return render_template('info.html', titulo='Informações')

# Área administrativa
@app.route('/indexadm')
def indexadm():
    return render_template('indexadm.html', jogos=Jogo.exibir(), url_atual = url_for('indexadm'), titulo='Área administrativa', proxima=request.form.get('proxima', url_for('index')), form=FormularioJogo())

@app.route('/atualizar', methods=['POST'])
def atualizar():
    form = FormularioJogo(request.form)
    if form.validate_on_submit():
        Jogo.atualizar(request.form['id'],form.nome.data,request.files['arquivo'])
        flash('Jogo Atualizado com Sucesso!')
    return redirect(url_for('indexadm'))

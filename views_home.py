from flask import render_template, request, redirect, session, flash, url_for
from main import app
from models import Jogo
from helpers import FormularioJogo,FormularioPagina,FormularioTutorial

@app.route('/')
def index():
    return render_template('index.html', jogos=Jogo.exibir())

@app.route('/jogo/<int:id>')
def jogo(id):
    return render_template('paginajogo.html', jogo=Jogo.consultarid(id), pagina=Jogo.consultarpagina(id), tutorial=Jogo.consultartutorial(id), imagens=Jogo.consultarimagens(id))

@app.route('/info')
def info():
    return render_template('info.html')

## Área administrativa
# Index ADM
@app.route('/indexadm')
def indexadm():
    return render_template('indexadm.html', jogos=Jogo.exibiradm(), url_atual = url_for('indexadm'), proxima=request.form.get('proxima', url_for('index')), form=FormularioJogo())

@app.route('/atualizarindex', methods=['POST'])
def atualizarindex():
    form = FormularioJogo(request.form)
    if form.validate_on_submit():
        Jogo.atualizarjogo(request.form['id'],form.nome.data,request.files['arquivo'])
        flash('Jogo Atualizado com Sucesso!')
    return redirect(url_for('indexadm'))

@app.route('/novojogo')
def novojogo():
    Jogo.adicionar()
    flash('Novo Jogo adicionado!')
    return redirect(url_for('indexadm'))

@app.route('/exibirjogo/<int:id>')
def exibirjogo(id):
    Jogo.exibirjogo(id)
    flash('Exibição alterada!')
    return redirect(url_for('indexadm'))

@app.route('/exibirtodos')
def exibirtodos():
    Jogo.exibirtodos()
    flash('Todos os Jogos agora estão sendo exibidos!')
    return redirect(url_for('indexadm'))

@app.route('/ocultartodos')
def ocultartodos():
    Jogo.ocultartodos()
    flash('Todos os Jogos agora estão ocultados!')
    return redirect(url_for('indexadm'))

@app.route('/excluirjogo/<int:id>')
def excluirjogo(id):
    Jogo.deletar(id)
    flash('Jogo Excluido!')
    return redirect(url_for('indexadm'))

# Pagina ADM
@app.route('/jogoadm/<int:id>')
def jogoadm(id):
    jogo = Jogo.consultarid(id)
    pagina = Jogo.consultarpagina(id)
    tutorial = Jogo.consultartutorial(id)
    imagens = Jogo.consultarimagens(id)
    form = FormularioPagina(obj=pagina)
    form2 = FormularioTutorial()
    return render_template('paginajogoadm.html', jogo=jogo, tutorial=tutorial, imagens=imagens, form=form, form2=form2)

@app.route('/atualizarjogoamd/<id>', methods=['POST'])
def atualizarjogoadm(id):
    form = FormularioPagina(request.form)
    form2 = FormularioTutorial(request.form)
    if form.validate_on_submit():
        Jogo.atualizarpagina(*form.data.values(),request.files['arquivo1'],request.files['arquivo2'],request.files['arquivo3'])
        flash('Formulario 1 Validado')
        return redirect(url_for('jogoadm', id=form.JogoID.data))
    if form2.validate_on_submit():
        Jogo.atualizarpasso(*form2.data.values())
        flash('Formulario 2 Validado')
        return redirect(url_for('jogoadm', id=id))
    return redirect(url_for('indexadm'))

@app.route('/novopasso/<id>')
def novopasso(id):
    Jogo.adicionarpasso(id)
    flash('Novo Passo Adicionado!')
    return redirect(url_for('jogoadm', id=id))

@app.route('/deletarpasso/<id>/<idp>')
def deletarpasso(id,idp):
    Jogo.deletarpasso(idp)
    flash('Passo Excluido!')
    return redirect(url_for('jogoadm', id=id))

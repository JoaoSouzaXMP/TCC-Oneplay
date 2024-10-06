from flask import render_template, request, redirect, session, flash, url_for
from main import app
from modelos import Jogo, PaginaJogo, ImagemJogo, TutorialJogo, Index, Pagina
from helpers import FormularioJogo, FormularioPagina, FormularioTutorial
from functools import wraps

# Decorator para verificar se o usuário é administrador
def login_required(rota):
    @wraps(rota)
    def decorated_function(*args, **kwargs):
        try:
            if session['usuario_logado'] == None or session['admin'] == False:
                flash('Logue como Admin para realizar alterações!')
                return redirect(url_for('login'))
            return rota(*args, **kwargs)
        except KeyError:
            flash('Você precisa ser um administrador para acessar esta página!')
            return redirect(url_for('login'))
    return decorated_function

# Home
@app.route('/')
def index():
    return render_template('index.html', jogos=Jogo.get_jogos_boolean(True))

# Página do Jogo
@app.route('/jogo/<int:id>')
def jogo(id):
    jogo = Jogo.get_jogo_by_jogoid(id)
    pagina = PaginaJogo.get_pagina_by_jogoid(id)
    tutorial = TutorialJogo.get_tutorial_by_jogoid(id)
    imagens = ImagemJogo.get_imagens_base64_by_jogoid(id)
    return render_template('paginajogo.html', jogo=jogo, pagina=pagina, tutorial=tutorial, imagens=imagens)

# Sobre
@app.route('/info')
def info():
    return render_template('info.html')

## Área administrativa
# Index ADM
@app.route('/indexadm')
@login_required
def indexadm():
    proxima = request.form.get('proxima', url_for('index'))
    return render_template('indexadm.html', jogos=Jogo.get_jogos_boolean(), url_atual=url_for('indexadm'), proxima=proxima, form=FormularioJogo())

# Atualizar Index
@app.route('/atualizarindex', methods=['POST'])
@login_required
def atualizarindex():
    form = FormularioJogo(request.form)
    if form.validate_on_submit():
        Index.atualizar_by_forms(form.ID.data, form.nome.data, request.files.get('arquivo'))
        flash('Jogo Atualizado com Sucesso!')
    return redirect(url_for('indexadm'))

# Ações do Jogo (ADM)
@app.route('/jogo/<acao>/<int:id>')
@login_required
def jogo_acao(acao, id=None):
    if acao == 'adicionar':
        Jogo.adicionar()
        flash('Novo Jogo adicionado!')
    elif acao == 'exibirjogo':
        Jogo.exibir_by_jogoid(id)
        flash('Exibição do jogo alterada!')
    elif acao == 'excluirjogo':
        Jogo.deletar_by_jogoid(id)
        flash('Jogo Excluido!')
    else:
        flash('Ação inválida para o jogo!')
    return redirect(url_for('indexadm'))

# Exibir/Ocultar Todos os Jogos
@app.route('/<acao>_todos')
@login_required
def acao_todos(acao):
    if acao == 'exibirtodos':
        Jogo.alterar_exibicao_todos_boolean(True)
        flash('Todos os Jogos agora estão sendo exibidos!')
    elif acao == 'ocultartodos':
        Jogo.alterar_exibicao_todos_boolean(False)
        flash('Todos os Jogos agora estão ocultados!')
    return redirect(url_for('indexadm'))

# Página de Edição do Jogo (ADM)
@app.route('/jogoadm/<int:id>')
@login_required
def jogoadm(id):
    jogo = Jogo.get_jogo_by_jogoid(id)
    pagina = PaginaJogo.get_pagina_by_jogoid(id)
    tutorial = TutorialJogo.get_tutorial_by_jogoid(id)
    imagens = ImagemJogo.get_imagens_base64_by_jogoid(id)
    form_pagina = FormularioPagina(obj=pagina)
    form_tutorial = FormularioTutorial()
    return render_template('paginajogoadm.html', jogo=jogo, tutorial=tutorial, imagens=imagens, form_pagina=form_pagina, form_tutorial=form_tutorial)

# Atualizar Jogo/Passo (ADM)
@app.route('/atualizar/<tipo>/<int:id>', methods=['POST'])
@login_required
def atualizar(tipo, id):
    if tipo == 'jogo':
        form = FormularioPagina(request.form)
        if form.validate_on_submit():
            Pagina.atualizar_pagina_forms(*form.data.values())
            ImagemJogo.atualizar_imagens_pagina_forms(form.JogoID.data, request.files.get('arquivo1'), request.files.get('arquivo2'), request.files.get('arquivo3'))
            flash('Página do jogo atualizada!')
    elif tipo == 'passo':
        form = FormularioTutorial(request.form)
        if form.validate_on_submit():
            TutorialJogo.atualizar_passo_forms(form.ID.data,form.NumeroTutorial.data,form.TituloTutorial.data,form.DescricaoTutorial.data)
            flash('Passo do tutorial atualizado!')
    else:
        flash('Tipo de atualização inválido!')
    return redirect(url_for('jogoadm', id=id))

# Ações do Passo do Tutorial (ADM)
@app.route('/passo/<acao>/<int:id>/<int:idp>')
@login_required
def passo_acao(acao, id, idp):
    if acao == 'adicionar':
        TutorialJogo.novo_passo_by_jogoid(id)
        flash('Novo Passo Adicionado!')
    elif acao == 'deletar':
        TutorialJogo.deletar_passo_tutorialid(idp)
        flash('Passo Excluido!')
    else:
        flash('Ação inválida para o passo do tutorial!')
    return redirect(url_for('jogoadm', id=id))
from flask import render_template, request, redirect, session, flash, url_for
from main import app
from models import Jogo,Imagem
from helpers import FormularioJogo

@app.route('/')
def index():
    return render_template('index.html', titulo='HOME', jogos=Jogo.exibir())

@app.route('/jogo/<int:id>')
def jogo(id):
    return render_template('jogo.html', titulo='Jogo', jogo=Jogo.consultarid(id), tutorial=Jogo.tutorial(id), video=Jogo.videos(id))

@app.route('/info')
def info():
    return render_template('info.html', titulo='Informações')
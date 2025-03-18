from django.shortcuts import render, redirect, get_object_or_404
from .models import Jogo, ImagemJogo
#from .forms import 
from django.contrib import messages

def all_games(request):
    jogos = Jogo.objects.order_by('Ordem').filter(ExibirHome=True)
    jogos_com_imagens = []

    for jogo in jogos:
        imagem_index = jogo.imagens.values_list('ImgIndex', flat=True).first()
        jogos_com_imagens.append({
            'jogo': jogo,
            'imagem': imagem_index
        })
    #print(jogos_com_imagens)

    return render(request, 'games/all_games.html', { "cards": jogos_com_imagens })    

def one_game(request, jogo_id):
    try:
        jogo = Jogo.objects.get(pk=jogo_id)
        #imagens = jogo.imagens.values('ImgPaginaJogo', 'ImgNoticia1', 'ImgNoticia2')
        #imagem_detalhada = imagens.first() if imagens else None
        imagens = jogo.imagens.first()
        pagina = jogo.pagina.first()
        tutorial = jogo.tutorial.all()

    except Jogo.DoesNotExist:
        jogo = None
        #imagem_detalhada = None
        imagens = None
        pagina = None
        tutorial = None

    return render(request, 'games/one_game.html', { 
        'jogo': jogo,
        'imagens': imagens,
        'pagina': pagina,
        'tutorial': tutorial,
    })
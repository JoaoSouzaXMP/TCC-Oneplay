from django.contrib import admin
from .models import Jogo, ImagemJogo, Categoria, PaginaJogo, TutorialJogo
#from .forms import ImagemJogoAdminForm

class ListandoJogos(admin.ModelAdmin):
    list_display = ('JogoID','Nome','CategoriaID','Ordem','ExibirHome')
    list_display_links = ('JogoID','Nome')
    search_fields = ('Nome',)
    list_filter = ('CategoriaID',)
    list_editable = ('ExibirHome',)

class ListandoImagens(admin.ModelAdmin):
    #form = ImagemJogoAdminForm
    list_display = ('ImagemJogoID','JogoID')
    list_display_links = ('ImagemJogoID','JogoID')

class ListandoCategorias(admin.ModelAdmin):
    list_display = ('Categoria',)
    list_display_links = ('Categoria',)
    search_fields = ('Categoria',)

class ListandoPaginas(admin.ModelAdmin):
    list_display = ('PaginaJogoID','JogoID',)
    list_display_links = ('PaginaJogoID','JogoID',)
    search_fields = ('JogoID',)

class ListandoTutorial(admin.ModelAdmin):
    list_display = ('TutorialJogoid','JogoID','Ordem','Passo',)
    list_display_links = ('TutorialJogoid','JogoID',)
    search_fields = ('JogoID',)

# Register your models here.
admin.site.register(Jogo, ListandoJogos)
admin.site.register(ImagemJogo, ListandoImagens)
admin.site.register(Categoria, ListandoCategorias)
admin.site.register(PaginaJogo, ListandoPaginas)
admin.site.register(TutorialJogo, ListandoTutorial)
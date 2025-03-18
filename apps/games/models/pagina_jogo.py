from django.db import models
from .jogo import Jogo

class PaginaJogo(models.Model):
    class Meta:
        db_table = 'tblPaginaJogos'

    PaginaJogoID = models.AutoField(primary_key=True)
    JogoID = models.ForeignKey(
        to=Jogo, 
        on_delete=models.CASCADE, 
        related_name='pagina',
        db_column='JogoID'
    )
    ResumoJogo = models.TextField(null=True, blank=True)
    LinkDownload = models.CharField(max_length=255, null=True, blank=True)
    DescricaoJogo = models.TextField(null=True, blank=True)
    TituloTutorial = models.CharField(max_length=255, null=True, blank=True)
    DescricaoTutorial = models.TextField(null=True, blank=True)
    TituloNoticia1 = models.CharField(max_length=255, null=True, blank=True)
    DescricaoNoticia1 = models.TextField(null=True, blank=True)
    TituloNoticia2 = models.CharField(max_length=255, null=True, blank=True)
    DescricaoNoticia2 = models.TextField(null=True, blank=True)
    TituloVideo = models.CharField(max_length=255, null=True, blank=True)
    DescricaoVideo = models.TextField(null=True, blank=True)
    LinkVideo = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.PaginaJogoID)
from django.db import models
from .jogo import Jogo

class TutorialJogo(models.Model):
    class Meta:
        db_table = 'tblTutorialJogos'

    TutorialJogoid = models.AutoField(primary_key=True)
    JogoID = models.ForeignKey(
        to=Jogo, 
        on_delete=models.CASCADE, 
        related_name='tutorial',
        db_column='JogoID'
    )
    Ordem =  models.IntegerField(null=True, blank=False)
    Passo = models.CharField(max_length=255, null=True, blank=True)
    DescricaoPasso = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.TutorialJogoid)
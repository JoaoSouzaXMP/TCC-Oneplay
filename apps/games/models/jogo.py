from django.db import models
from .categoria import Categoria
import base64

# Create your models here.
class Jogo(models.Model):
    class Meta:
        db_table = 'tblJogos'

    JogoID = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=255, null=False, blank=False, unique=True)
    CategoriaID = models.ForeignKey(
        to=Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )
    Ordem = models.IntegerField(null=True, blank=False, unique=True)
    ExibirHome = models.BooleanField(default=True)

    def __str__(self):
        return str(self.Nome)
    
    def get_folder_name(self): return f'jogos/{self.JogoID}'

    @classmethod
    def get_jogos_boolean(cls, exibir_home=None):
        from .jogo import ImagemJogo  # Supondo que exista um modelo relacionado chamado ImagemJogo
        
        query = cls.objects.all()
        if exibir_home is not None:
            query = query.filter(ExibirHome=exibir_home)

        jogos = []
        for jogo in query:
            img_index = ImagemJogo.objects.filter(JogoID=jogo.JogoID).first()
            jogo_list = (
                jogo.JogoID,
                jogo.CategoriaID,
                jogo.ExibirHome,
                jogo.Ordem,
                jogo.Nome,
                base64.b64encode(img_index.ImgIndex).decode('utf-8') if img_index else None,
            )
            jogos.append(jogo_list)
        return jogos

    @classmethod
    def get_jogo_by_jogoid(cls, jogo_id):
        try:
            return cls.objects.get(JogoID=jogo_id)
        except cls.DoesNotExist:
            return None

    @staticmethod
    def adicionar(categoria_id=None, exibir_home=False, ordem=None, nome=None):
        novo_jogo = Jogo(
            CategoriaID=categoria_id,
            ExibirHome=exibir_home,
            Ordem=ordem,
            Nome=nome,
        )
        novo_jogo.save()

    @staticmethod
    def exibir_by_jogoid(jogo_id):
        try:
            jogo = Jogo.objects.get(JogoID=jogo_id)
            jogo.ExibirHome = not jogo.ExibirHome
            jogo.save()
        except Jogo.DoesNotExist:
            pass

    @staticmethod
    def alterar_exibicao_todos_boolean(valor):
        Jogo.objects.update(ExibirHome=valor)

    @staticmethod
    def deletar_by_jogoid(jogo_id):
        try:
            jogo = Jogo.objects.get(JogoID=jogo_id)
            jogo.delete()
        except Jogo.DoesNotExist:
            pass

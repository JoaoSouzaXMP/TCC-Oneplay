from django.db import models
from cloudinary.models import CloudinaryField
from .jogo import Jogo
import base64

class ImagemJogo(models.Model):
    class Meta:
        db_table = 'tblImagensJogos'

    ImagemJogoID = models.AutoField(primary_key=True)
    JogoID = models.ForeignKey(
        to=Jogo, 
        on_delete=models.CASCADE, 
        related_name='imagens',
        db_column='JogoID'
    )

    # Definindo todos os parâmetros comuns em uma variável reutilizável 
    common_cloudinary_options = {'resource_type': 'image', 'transformation': { 'fetch_format': 'auto', 'width': 430, 'height': 430, 'crop': 'limit' }, 'folder': 'user_uploads',  'overwrite': True}

    ImgIndex = CloudinaryField('ImgIndex', blank=True, **common_cloudinary_options)
    ImgPaginaJogo = CloudinaryField('ImgPaginaJogo', blank=True, **common_cloudinary_options)
    ImgNoticia1 = CloudinaryField('ImgNoticia1', blank=True, **common_cloudinary_options)
    ImgNoticia2 = CloudinaryField('ImgNoticia2', blank=True, **common_cloudinary_options)

    def __str__(self):
        return str(self.ImagemJogoID)
    
    
    @classmethod
    def get_imagens_base64_by_jogoid(cls, jogo_id):
        try:
            imagens = cls.objects.get(JogoID=jogo_id)
            imagens.ImgPaginaJogo = base64.b64encode(imagens.ImgPaginaJogo).decode('utf-8') if imagens.ImgPaginaJogo else None
            imagens.ImgNoticia1 = base64.b64encode(imagens.ImgNoticia1).decode('utf-8') if imagens.ImgNoticia1 else None
            imagens.ImgNoticia2 = base64.b64encode(imagens.ImgNoticia2).decode('utf-8') if imagens.ImgNoticia2 else None
            return imagens
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_imagens_binary_by_id(cls, jogo_id):
        imagens, created = cls.objects.get_or_create(JogoID_id=jogo_id)
        return imagens

    @classmethod
    def get_imagem_index_by_id(cls, jogo_id):
        try:
            img = cls.objects.filter(JogoID_id=jogo_id).values_list('ImgIndex', flat=True).first()
            return base64.b64encode(img).decode('utf-8') if img else None
        except cls.DoesNotExist:
            return None

    @staticmethod
    def atualizar_imagem_index(jogo_id, img):
        try:
            img_bytes = img.read()
            imagem_jogo, created = ImagemJogo.objects.get_or_create(JogoID_id=jogo_id)
            imagem_jogo.ImgIndex = img_bytes
            imagem_jogo.save()
        except Exception as e:
            print(f"Erro ao atualizar: {e}")

    @staticmethod
    def atualizar_imagens_pagina_forms(jogo_id, img1=None, img2=None, img3=None):
        try:
            imagens = ImagemJogo.objects.filter(JogoID_id=jogo_id).first()
            if not imagens:
                return None
            
            for img, attr in zip([img1, img2, img3], ['ImgPaginaJogo', 'ImgNoticia1', 'ImgNoticia2']):
                if img:
                    setattr(imagens, attr, img.read())

            imagens.save()
        except Exception as e:
            print(f"Erro ao atualizar: {e}")

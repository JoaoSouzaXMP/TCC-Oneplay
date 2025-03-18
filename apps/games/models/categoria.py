from django.db import models

class Categoria(models.Model):
    class Meta:
        db_table = 'tblCategorias'

    CategoriaID = models.AutoField(primary_key=True)
    Categoria = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self) -> str:
        return self.Categoria
from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imagens/')
    link = models.URLField()

    def __str__(self):
        return self.titulo
    

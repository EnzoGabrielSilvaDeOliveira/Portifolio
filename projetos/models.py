from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='imagens/')
    linkProjeto = models.URLField()
    linkGithub = models.URLField(blank=True, null=True) 

    def __str__(self):
        return self.titulo
    

from django.db import models
from django.conf import settings


class Category(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self):
        return self.nome

class Historia(models.Model):
    name = models.CharField(max_length=255)
    capa = models.URLField(max_length=200, null=True)
    relato =models.CharField(max_length=5000)
    data = models.DateTimeField(auto_now=True)
    categoria = models.ManyToManyField(Category)
    def __str__(self):
        return f'{self.name} ({self.data})'
    
class Comment(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now=True)
    historia = models.ForeignKey(Historia, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.texto}" - {self.autor}'
    
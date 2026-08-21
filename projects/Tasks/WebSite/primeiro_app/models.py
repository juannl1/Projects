from django.db import models

# Create your models here.

class Topicos(models.Model):
    """Topicos"""
    
    text = models.CharField(max_length=255)
    adicionado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representacao em string do modelo"""
        return self.text
Topicos
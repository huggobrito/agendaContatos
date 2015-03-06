from django.db import models
from django.db.models import permalink


# Create your models here.

class Contato(models.Model):
        nome = models.CharField(max_length=100)
        cpf = models.CharField('CPF', max_length=11, unique=True)
        idade = models.IntegerField()
        email = models.EmailField(unique=True)
        telefone = models.CharField(max_length=20, blank=True)
        criado_em = models.DateField(db_index=True, auto_now_add=True)
        foto = models.ImageField(upload_to="fotos")


        def __unicode__(self):
            return '%s' % self.nome

        @permalink
        def get_absolute_url(self):
            return ('view_contato', None, { 'nome': self.nome })
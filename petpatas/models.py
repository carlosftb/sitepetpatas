from django.db import models

class Servicos(models.Model):
    nome_servico = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.CharField(max_length=150, null=False, blank=False)
    valor = models.CharField(max_length=15, null=False, blank=False)
    avaliacao = models.IntegerField(null=False, blank=False)
    foto1 = models.ImageField(upload_to="servicosupload/%Y/%m/%d/", blank=False)
    foto2 = models.ImageField(upload_to="servicosupload/%Y/%m/%d/", blank=False)
    ativo = models.BooleanField(default=False)


def ___str___(self):
    return f"Serviço [nome={self.nome_servico}]"


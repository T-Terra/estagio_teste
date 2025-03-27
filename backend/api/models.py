from django.db import models

class Enterprise(models.Model):
    registro_ans = models.IntegerField(primary_key=True)
    cnpj = models.BigIntegerField(null=False)
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255, null=True)
    modalidade = models.CharField(max_length=100, null=True)
    logradouro = models.CharField(max_length=255, null=True)
    numero = models.CharField(max_length=50, null=True)
    complemento = models.CharField(max_length=255, null=True)
    bairro = models.CharField(max_length=100, null=True)
    cidade = models.CharField(max_length=100, null=True)
    uf = models.CharField(max_length=2, null=True)
    cep = models.BigIntegerField(null=True)
    ddd = models.SmallIntegerField(null=True)
    telefone = models.BigIntegerField(null=True)
    fax = models.BigIntegerField(null=True)
    endereco_eletronico = models.CharField(max_length=255, null=True)
    representante = models.CharField(max_length=255, null=True)
    cargo_representante = models.CharField(max_length=255, null=True)
    regiao_de_comercializacao = models.IntegerField(null=True)
    data_registro_ans = models.DateField(null=True)

    def __str__(self):
        return self.razao_social

from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    redeSocial = models.CharField(max_length=300, default='')

    def __str__(self):
        return f'{self.nome} - {self.email}'
 
class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2) 
    cep = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.rua}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado} - {self.cep}'
        
class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f'{self.nome} - {self.descricao} - R$ {self.valor}'

class FormaPagamento(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.descricao}'

class OrdemServico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    endereco_cliente = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    tipo_servico = models.ManyToManyField(Servico)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    data_realização = models.DateTimeField(auto_now_add=True)
    feito = models.BooleanField(default=False)
    pago = models.BooleanField(default=False)
    cancelado = models.BooleanField(default=False)
    

    def __str__(self): 
        return f'{self.cliente} - {self.tipo_servico} - {self.data_realização}'
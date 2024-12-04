from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Nome: {self.nome} - E-mail: {self.email} - Telefone: {self.telefone} - Data de Cadastro: {self.data_cadastro}'
    
    
class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    edicao = models.CharField(max_length=15)
    autores = models.ManyToManyRel('Autor')

    def __str__(self):
        return f'Titulo: {self.titulo} - Edição: {self.edicao}'
    
class Editora(models.Model):
    nome = models.CharField(max_length=100)
    livros = models.ManyToOneRel(Livro, on_delete=models.CASCADE)

    
    def __str__(self):
        return f'Nome: {self.nome} - Livros: {self.livros}'

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    livros = models.ManyToManyField(Livro, )

    def __str__(self):
        return f'Nome: {self.nome} - Livros: {self.livros}'

class Emprestimo(models.Model):
    data_de_coleta = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField()
    livro = models.ForeignKey(Livro)
    usuario = models.ForeignKey(Usuario)

class Reserva(models.Model):
    data_de_inicio = models.DateTimeField(auto_now_add=True)
    prazo_final = models.DateTimeField()
    livro = models.ForeignKey(Livro)
    usuario = models.ForeignKey(Usuario)